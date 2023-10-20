from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page,name='start-page'),
    path("posts",views.post_page,name='post-page'),
    path("posts/<slug:slug>",views.postdetail_page,name='detail-page')
]