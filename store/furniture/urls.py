from django.urls import path, re_path
from . import views


app_name = 'furniture'
urlpatterns = [
    re_path('^all/$', views.FurnitureList.as_view(), name='all'),
    path('all/<int:furniture_id>/', views.get_furniture, name='furniture'),
    path('all/wooden/', views.get_all_wooden, name='wooden'),
    path('all/ordered/', views.order_furniture, name='ordered'),
    re_path('^create/$', views.FurnitureCreate.as_view(), name='create'),
    re_path('^edit/(?P<pk>\d+)/$', views.FurnitureUpdate.as_view(), name='edit'),
    re_path('details/(?P<pk>[-\w]+)/', views.FurnitureDetail.as_view(), name='details'),
    re_path('update/(?P<pk>[-\w]+)/', views.FurnitureUpdate.as_view(), name='update'),
    re_path('delete/(?P<pk>\d+)/', views.DeleteFurniture.as_view(), name='delete'),
]