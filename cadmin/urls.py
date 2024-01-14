from django.urls import path
from . import views
urlpatterns=[
    path('',views.admin_view,name='admin_view'),
    path('detail/<int:id>',views.user_detail_page,name='detail'),
    path('delete/<int:id>',views.delete_user,name='delete'),
    path('register',views.user_creation,name='register'),
   
]