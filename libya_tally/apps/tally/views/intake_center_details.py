from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView

from libya_tally.apps.tally import forms
from libya_tally.apps.tally.models.result_form import ResultForm
from libya_tally.libs.permissions import groups
from libya_tally.libs.views import mixins


class ReverseSuccessURLMixin(object):
    def get_success_url(self):
        if self.success_url:
            self.success_url = reverse(self.success_url)
        return super(ReverseSuccessURLMixin, self).get_success_url()


class CenterDetailView(mixins.GroupRequiredMixin,
                       ReverseSuccessURLMixin,
                       FormView):
    form_class = forms.IntakeBarcodeForm
    group_required = groups.INTAKE_CLERK
    template_name = "tally/center_details.html"
    success_url = 'check-center-details'

    def post(self, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            self.request.session['barcode'] = form.cleaned_data['barcode']
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class CheckCenterDetailView(mixins.GroupRequiredMixin,
                            ReverseSuccessURLMixin,
                            FormView):
    form_class = forms.IntakeBarcodeForm
    group_required = groups.INTAKE_CLERK
    template_name = "tally/check_center_details.html"
    success_url = "intake-check-center-details"

    def get(self, *args, **kwargs):
        barcode = self.request.session.get('barcode')
        result_form = get_object_or_404(ResultForm, barcode=barcode)

        return self.render_to_response(
            self.get_context_data(result_form=result_form))
