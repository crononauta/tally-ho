from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from tally_ho.apps.tally.forms.login_form import LoginForm
from tally_ho.apps.tally.forms.password_change import PasswordChangeForm
from tally_ho.apps.tally.views import archive, audit, clearance,\
    corrections, data_entry, home, intake, quality_control,\
    super_admin, profile, tally_manager
from tally_ho.apps.tally.views.data import center_list_view, form_list_view,\
    candidate_list_view, race_list_view, tally_list_view
from tally_ho.apps.tally.views.reports import offices
from tally_ho.apps.tally.views.reports import races

admin.autodiscover()

accounts_urls = patterns(
    '',
    url(r'^login/$',
        profile.login,
        {
            'template_name': 'registration/login.html',
            'authentication_form': LoginForm
        },
        name='login'),
    url(r'^password_change/$',
        'django.contrib.auth.views.password_change',
        {
            'password_change_form': PasswordChangeForm,
            'post_change_redirect': '/'},
        name='password_change'),
    url(r'^password_change/done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
)

handler403 = 'tally_ho.apps.tally.views.home.permission_denied'
handler404 = 'tally_ho.apps.tally.views.home.not_found'
handler400 = 'tally_ho.apps.tally.views.home.bad_request'
handler500 = 'tally_ho.apps.tally.views.home.server_error'

urlpatterns = patterns(
    '',
    url(r'^$', home.HomeView.as_view(), name='home'),
    url(r'^locale$', home.LocaleView.as_view(), name='home-locale'),

    url(r'^data/center-list/(?P<tally_id>(\d+))/$',
        center_list_view.CenterListView.as_view(),
        name='center-list'),
    url(r'^data/center-list-data/(?P<tally_id>(\d+))/$',
        center_list_view.CenterListDataView.as_view(),
        name='center-list-data'),
    url(r'^data/race-list/(?P<tally_id>(\d+))/$',
        race_list_view.RaceListView.as_view(),
        name='races-list'),
    url(r'^data/candidate-list$',
        candidate_list_view.CandidateListView.as_view(),
        name='candidate-list'),
    url(r'^data/candidate-list-data$',
        candidate_list_view.CandidateListDataView.as_view(),
        name='candidate-list-data'),
    url(r'^data/form-list/(?P<tally_id>(\d+))/$',
        form_list_view.FormListView.as_view(),
        name='form-list'),
    url(r'^data/form-list/(?P<tally_id>(\d+))/(?P<state>.*)/$',
        form_list_view.FormListView.as_view(),
        name='form-list'),
    url(r'^data/form-list-data/(?P<tally_id>(\d+))/$',
        form_list_view.FormListDataView.as_view(),
        name='form-list-data'),
    url(r'^data/form-not-received.(?P<format>(csv))$',
        form_list_view.FormNotReceivedListView.as_view(),
        name='form-not-received-view'),
    url(r'^data/form-not-received$',
        form_list_view.FormNotReceivedListView.as_view(),
        name='form-not-received-view'),
    url(r'^data/form-not-received-data$',
        form_list_view.FormNotReceivedDataView.as_view(),
        name='form-not-received-data'),
    url(r'^data/forms-for-race/(?P<ballot>.*)/$',
        form_list_view.FormsForRaceView.as_view(),
        name='forms-for-race'),
    url(r'^data/forms-for-race-data/(?P<ballot>.*)/$',
        form_list_view.FormListDataView.as_view(),
        name='forms-for-race-data'),

    url(r'^super-administrator/tallies$',
        super_admin.TalliesView.as_view(), name='super-administrator-tallies'),
    url(r'^super-administrator/(?P<tally_id>(\d+))/$',
        super_admin.DashboardView.as_view(), name='super-administrator'),
    url(r'^super-administrator/form-progress$',
        super_admin.FormProgressView.as_view(),
        name='form-progress'),
    url(r'^super-administrator/form-duplicates$',
        super_admin.FormDuplicatesView.as_view(),
        name='form-duplicates'),
    url(r'^super-administrator/form-clearance$',
        super_admin.FormClearanceView.as_view(),
        name='form-clearance'),
    url(r'^super-administrator/form-audit$',
        super_admin.FormAuditView.as_view(),
        name='form-audit'),
    url(r'^super-administrator/form-results-duplicates$',
        super_admin.FormResultsDuplicatesView.as_view(),
        name='form-results-duplicates'),
    url(r'^super-administrator/form-action-list$',
        super_admin.FormActionView.as_view(),
        name='form-action-view'),
    url(r'^super-administrator/form-progress-data$',
        super_admin.FormProgressDataView.as_view(),
        name='form-progress-data'),
    url(r'^super-administrator/form-duplicates-data$',
        super_admin.FormDuplicatesDataView.as_view(),
        name='form-duplicates-data'),
    url(r'^super-administrator/form-clearance-data$',
        super_admin.FormClearanceDataView.as_view(),
        name='form-clearance-data'),
    url(r'^super-administrator/form-audit-data$',
        super_admin.FormAuditDataView.as_view(),
        name='form-audit-data'),
    url(r'^super-administrator/results-(?P<report>.*).csv$',
        super_admin.ResultExportView.as_view(),
        name='result-export'),
    url(r'^super-administrator/results$',
        super_admin.ResultExportView.as_view(),
        name='result-export'),
    url(r'^super-administrator/remove-centre/(?P<tally_id>(\d+))/$',
        super_admin.RemoveCenterView.as_view(),
        name='remove-center'),
    url(r'^super-administrator/remove-centre/(?P<tally_id>(\d+))/(?P<centerCode>(\d+))$',
        super_admin.RemoveCenterConfirmationView.as_view(),
        name='remove-center-confirmation'),
    url(r'^super-administrator/edit-centre/(?P<tally_id>(\d+))/(?P<centerCode>(\d+))$',
        super_admin.EditCentreView.as_view(),
        name='edit-centre'),
    url(r'^super-administrator/disable/(?P<tally_id>(\d+))/(?P<centerCode>(\d+))/(?P<stationNumber>(\d+))?$',
        super_admin.DisableEntityView.as_view(),
        name='disable'),
    url(r'^super-administrator/enable/(?P<tally_id>(\d+))/(?P<centerCode>(\d+))/(?P<stationNumber>(\d+))?$',
        super_admin.EnableEntityView.as_view(),
        name='enable'),
    url(r'^super-administrator/disablerace/(?P<tally_id>(\d+))/(?P<raceId>(\d+))$',
        super_admin.DisableRaceView.as_view(),
        name='disable-race'),
    url(r'^super-administrator/enablerace/(?P<tally_id>(\d+))/(?P<raceId>(\d+))$',
        super_admin.EnableRaceView.as_view(),
        name='enable-race'),
    url(r'^super-administrator/candidate-disable/(?P<candidateId>(\d+))$',
        super_admin.DisableCandidateView.as_view(),
        name='candidate-disable'),
    url(r'^super-administrator/candidate-enable/(?P<candidateId>(\d+))$',
        super_admin.EnableCandidateView.as_view(),
        name='candidate-enable'),
    url(r'^super-administrator/remove-station/(?P<tally_id>(\d+))/$',
        super_admin.RemoveStationView.as_view(),
        name='remove-station'),
    url(r'^super-administrator/quarantine-checks$',
        super_admin.QuarantineChecksListView.as_view(),
        name='quarantine-checks'),
    url(r'^super-administrator/quarantine-checks/config/(?P<checkId>(\d+))$',
        super_admin.QuarantineChecksConfigView.as_view(),
        name='quarantine-checks-config'),
    url(r'^super-administrator/remove-station/(?P<tally_id>(\d+))/(?P<centerCode>(\d+))/(?P<stationNumber>(\d+))$',
        super_admin.RemoveStationConfirmationView.as_view(),
        name='remove-station-confirmation'),
    url(r'^super-administrator/edit-station/(?P<tally_id>(\d+))/(?P<centerCode>(\d+))/(?P<stationNumber>(\d+))$',
        super_admin.EditStationView.as_view(),
        name='edit-station'),

    url(r'^data-entry$', data_entry.DataEntryView.as_view(),
        name='data-entry'),
    url(r'^data-entry/enter-center-details$',
        data_entry.CenterDetailsView.as_view(),
        name='data-entry-enter-center-details'),
    url(r'^data-entry/enter-results',
        data_entry.EnterResultsView.as_view(),
        name='enter-results'),
    url(r'^data-entry/success',
        data_entry.ConfirmationView.as_view(),
        name='data-entry-success'),

    url(r'^intake/center-details$', intake.CenterDetailsView.as_view(),
        name='intake'),
    url(r'^intake/enter-center', intake.EnterCenterView.as_view(),
        name='intake-enter-center'),
    url(r'^intake/check-center-details$',
        intake.CheckCenterDetailsView.as_view(),
        name='check-center-details'),
    url(r'^intake/printcover$',
        intake.PrintCoverView.as_view(),
        name='intake-printcover'),
    url(r'^intake/clearance$',
        intake.ClearanceView.as_view(),
        name='intake-clearance'),
    url(r'^intake/intaken',
        intake.ConfirmationView.as_view(),
        name='intaken'),
    url(r'^intake/intake-printed/(?P<resultFormPk>(\d+))$',
        intake.IntakePrintedView.as_view(),
        name='intake-printed'),

    url(r'^quality-control/home$',
        quality_control.QualityControlView.as_view(),
        name='quality-control'),
    url(r'^quality-control/dashboard$',
        quality_control.QualityControlDashboardView.as_view(),
        name='quality-control-dashboard'),
    url(r'^quality-control/reject$',
        TemplateView.as_view(
            template_name='quality_control/reject.html'),
        name='quality-control-reject'),

    url(r'^corrections$',
        corrections.CorrectionView.as_view(),
        name='corrections'),
    url(r'^corrections/match$',
        corrections.CorrectionMatchView.as_view(),
        name='corrections-match'),
    url(r'^corrections/required$',
        corrections.CorrectionRequiredView.as_view(),
        name='corrections-required'),
    url(r'^corrections/success$',
        corrections.ConfirmationView.as_view(),
        name='corrections-success'),

    url(r'^archive/print$',
        archive.ArchivePrintView.as_view(),
        name='archive-print'),
    url(r'^archive/success$',
        archive.ConfirmationView.as_view(),
        name='archive-success'),

    url(r'^audit$',
        audit.DashboardView.as_view(),
        name='audit'),
    url(r'^audit/new',
        audit.CreateAuditView.as_view(),
        name='audit-new'),
    url(r'^audit/print',
        audit.PrintCoverView.as_view(),
        name='audit-print'),
    url(r'^audit/review$',
        audit.ReviewView.as_view(),
        name='audit-review'),

    url(r'^clearance$',
        clearance.DashboardView.as_view(),
        name='clearance'),
    url(r'^clearance/new',
        clearance.NewFormView.as_view(),
        name='clearance-new'),
    url(r'^clearance/print',
        clearance.PrintCoverView.as_view(),
        name='clearance-print'),
    url(r'^clearance/review$',
        clearance.ReviewView.as_view(),
        name='clearance-review'),
    url(r'^clearance/create',
        clearance.CreateClearanceView.as_view(),
        name='clearance-create'),
    url(r'^clearance/check-center-details$',
        clearance.CheckCenterDetailsView.as_view(),
        name='clearance-check-center-details'),
    url(r'^clearance/add$',
        clearance.AddClearanceFormView.as_view(),
        name='clearance-add'),
    url(r'^clearance/clearance-printed/(?P<resultFormPk>(\d+))$',
        clearance.ClearancePrintedView.as_view(),
        name='clearance-printed'),

    url(r'^reports/internal/offices$',
        offices.OfficesReportView.as_view(),
        name='reports-offices'),
    url(r'^reports/internal/offices/(?P<option>.*)/$',
        offices.OfficesReportDownloadView.as_view(),
        name='reports-offices-export'),
    url(r'^reports/internal/race',
        races.RacesReportView.as_view(),
        name='reports-races'),

    url(r'^tally-manager$',
        tally_manager.DashboardView.as_view(), name='tally-manager'),
    url(r'^tally-manager/create-tally$',
        tally_manager.CreateTallyView.as_view(), name='create-tally'),
    url(r'^tally-manager/update-tally/(?P<tally_id>(\d+))/$',
        tally_manager.TallyUpdateView.as_view(), name='update-tally'),
    url(r'^tally-manager/tally-files/(?P<tally_id>(\d+))/$',
        tally_manager.TallyFilesFormView.as_view(), name='tally-files-form'),
    url(r'^tally-manager/remove-tally/(?P<tally_id>(\d+))/$',
        tally_manager.TallyRemoveView.as_view(), name='remove-tally'),
    url(r'^tally-manager/create-tally/batch-view/(?P<tally_id>.*)/'
        '(?P<subconst_file>.*)/(?P<subconst_file_lines>(\d+))/'
        '(?P<centers_file>.*)/(?P<centers_file_lines>(\d+))/'
        '(?P<stations_file>.*)/(?P<stations_file_lines>(\d+))/'
        '(?P<candidates_file>.*)/(?P<candidates_file_lines>(\d+))/'
        '(?P<ballots_order_file>.*)/'
        '(?P<result_forms_file>.*)/(?P<result_forms_file_lines>(\d+))/$',
        tally_manager.BatchView.as_view(), name='batch-view'),
    url(r'^tally-manager/data/tally-list$',
        tally_list_view.TallyListView.as_view(),
        name='tally-list'),
    url(r'^tally-manager/data/tally-list-data$',
        tally_list_view.TallyListDataView.as_view(),
        name='tally-list-data'),

    url(r'^operation-not-allowed',
        home.suspicious_error, name='suspicious-error'),

    url(r'^accounts/', include(accounts_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracking/', include('tracking.urls')),
    url(r'^djangojs/', include('djangojs.urls')),
)
