from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import (HttpResponseRedirect, HttpResponse, 
            HttpResponseForbidden, Http404)
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from dances.forms import DanceForm
from dances.models import Dance

@login_required
def add(request, 
                form_class=DanceForm, 
                template_name='dances/form.html'):
                
    if request.method == "POST":
        if request.user.is_authenticated():
            form = form_class(request.user, request.POST)
            if form.is_valid():
                dance = form.save(commit = False)
                dance.save()
                redirect_to = reverse("your_dances")
                return HttpResponseRedirect(redirect_to)
    else:
        form = form_class(request.user)                
                
    return render_to_response(template_name, {
        "form": form,
    }, context_instance=RequestContext(request))
    


@login_required
def your_dances(request, template_name="dances/your_dances.html"):
    return render_to_response(template_name, {
        "groups": Dance.objects.filter(members=request.user).order_by("name"),
    }, context_instance=RequestContext(request))
    
def dances(request, template_name="dances/dances.html"):
    
    dances = Dance.objects.filter()
    
    return render_to_response(template_name, {
        'dances': dances,
    }, context_instance=RequestContext(request))    