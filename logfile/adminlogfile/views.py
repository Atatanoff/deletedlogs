from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import TrackDel
from django.core.paginator import Paginator

from loguru import logger


def index(request):
    data_list = None
    if request.method == "POST":
        post = dict()
        for key in request.POST:
            item = request.POST.get(key)
            if item and key in ('server', 'file_name', 'dt_time', 'user_name'): post[key+"__icontains"] = item
        data_list = TrackDel.objects.filter(**post)
        logger.debug(post)
        #paginator = Paginator(data_list, 10)
        #page_number = request.GET.get('page')
        #page_obj = paginator.get_page(page_number)
        userform = UserForm()
        return render(request, "adminlogfile/index.html", {
            "form": userform,
            'page_obj': data_list
            })
    
    else:
        userform = UserForm()
        return render(request, "adminlogfile/index.html", {"form": userform})

