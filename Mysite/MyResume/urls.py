from MyResume import views
from django.urls import path


app_name='MyResume'

urlpatterns=[

    path('',views.index_view,name='index')

]