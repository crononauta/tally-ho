from django.views.generic import TemplateView
from eztables.views import DatatablesView
from guardian.mixins import LoginRequiredMixin

from tally_system.apps.tally.models.station import Station
from tally_system.libs.permissions import groups
from tally_system.libs.views import mixins
from tally_system.libs.views.pagination import paging


class CenterListDataView(LoginRequiredMixin,
                         mixins.GroupRequiredMixin,
                         mixins.DatatablesDisplayFieldsMixin,
                         DatatablesView):
    group_required = groups.SUPER_ADMINISTRATOR
    model = Station
    fields = (
        'center__office__name',
        'sub_constituency__code',
        'center__name',
        'center__code',
        'gender',
        'registrants',
        'modified_date',
    )
    display_fields = (
        ('center__office__name', 'center_office'),
        ('sub_constituency__code', 'sub_constituency_code'),
        ('center__name', 'center_name'),
        ('center__code', 'center_code'),
        ('gender', 'gender_name'),
        ('registrants', 'registrants'),
        ('modified_date', 'modified_date_formatted'),
    )


class CenterListView(LoginRequiredMixin,
                     mixins.GroupRequiredMixin,
                     TemplateView):
    group_required = groups.SUPER_ADMINISTRATOR
    template_name = "data/centers.html"

    def get(self, *args, **kwargs):
        station_list = Station.objects.all()
        stations = paging(station_list, self.request)

        return self.render_to_response(self.get_context_data(
            stations=stations,
            remote_url='center-list-data'))
