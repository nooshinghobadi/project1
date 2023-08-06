from django.urls import path
from . import views


urlpatterns=[
    path('info/',views.info),
    path('hello/',views.hello),
    path('info/detail/<int:personalinfo_id>',views.detail),

]