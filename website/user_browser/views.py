from django.shortcuts import render
from django.views.generic import TemplateView
#from django.template import Context, Template

def home_page_view(request):
    from user_browser.models import PostsModel
    data = PostsModel.objects.all()

    context = {
        "post_info": data,
    }

    return render(request, "index.html", context)
