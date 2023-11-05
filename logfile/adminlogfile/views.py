from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import TrackDel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from loguru import logger

@login_required
def index(request):
    data_list = None
    if request.method == "POST":
        post = dict()
        for key in request.POST:
            item = request.POST.get(key)
            if item and key in ('server', 'file_name', 'user_name'): post[key+"__icontains"] = item
            if item and key == 'dt_time': post['dt_time__icontains'] = request.POST.get(key)
            if item and key == 'to_dt_time':
                post['dt_time__range'] = [post['dt_time__icontains'], item]
                post.pop('dt_time__icontains')

        # удалить слайс
        data_list = TrackDel.objects.filter(**post).order_by('dt_time')[:50]
        
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

