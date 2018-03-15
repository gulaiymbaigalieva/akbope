from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Job Index View")


from django.template import Context, loader
from django.http import HttpResponse
from jobs.models import Job


def index(request):
    object_list = Job.objects.order_by('-pub_date')[:10]
    t = loader.get_template('jobs/job_list.html')
    c = Context({
        'object_list': object_list,
    })
    return HttpResponse(t.render(c))


from django.shortcuts import get_object_or_404, render_to_response
from jobs.models import Job


def index(request):
    object_list = Job.objects.order_by('-pub_date')[:10]
    return render_to_response('jobs/job_list.html',
                              {'object_list': object_list})


def detail(request, object_id):
    job = get_object_or_404(Job, pk=object_id)
    return render_to_response('jobs/job_detail.html',
                              {'object': job})
