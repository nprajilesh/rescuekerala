from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('request/', views.CreateRequest.as_view(), name='requestview'),
    path('volunteer/', views.RegisterVolunteer.as_view(), name='registerview'),
    path('requests/', views.request_list, name='requestlistview'),
    path('contactus/', views.districtmanager_list, name='contactus'),
    path('reg_success/', views.RegSuccess.as_view(), name='reg_successview'),
    path('req_sucess/', views.ReqSuccess.as_view(), name='req_sucessview'),
    path('district_needs/', views.DistNeeds.as_view(), name='distneedsview'),
    path('reg_contrib/', views.RegisterContributor.as_view(), name='reg_contribview'),
    path('contrib_success/', views.ContribSuccess.as_view(), name='contribsucessview'),
]
