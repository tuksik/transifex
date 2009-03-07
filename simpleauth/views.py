from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout as auth_logout
from simpleauth.util import clean_next

@login_required
def logout(request, template_name='simpleauth/logged_out.html'):
    """Logout the user from the website and redirect back."""
    next = clean_next(request.GET.get('next'))
    auth_logout(request, next_page=next, template_name=template_name)
    return HttpResponseRedirect(next)

@login_required
def account_settings(request, template_name='simpleauth/settings.html'):
    """Account settings page."""
    msg = request.GET.get('msg', '')
    return render_to_response(template_name,
                  {'msg': msg,},
                  context_instance=RequestContext(request))
