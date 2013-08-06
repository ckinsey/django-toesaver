from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest

import json

from toesaver.utils import ViewCounter


def ajax_report_view(request):
    """
    Javascript will report to this view the current user and the page he is browsing
    """

    if not request.is_ajax():
        return HttpResponseBadRequest()

    if request.POST:
        print request.POST
        vc = ViewCounter(path=request.POST.get('current_page'))
        vc.set_viewer(request.user)
        return HttpResponse(json.dumps(True))

    return HttpResponse(json.dumps(False))


def ajax_get_views(request):
    """
    Javascript will request the users currently browsing this page
    """

    if not request.is_ajax():
        return HttpResponseBadRequest()

    if request.GET:
        vc = ViewCounter(path=request.GET.get('current_page'))
        viewers = vc.get_viewers()
        return HttpResponse(json.dumps(viewers))

    return HttpResponse(json.dumps(False))