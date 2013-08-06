from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^ajax_report_view/$', 'toesaver.views.ajax_report_view', name="toesaver-ajax-report-view"),
    url(r'^ajax_get_views/$', 'toesaver.views.ajax_get_views', name="toesaver-ajax-get-views"),
)