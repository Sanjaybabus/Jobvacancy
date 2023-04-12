from django.urls import path

from JObPP import views

urlpatterns = [
    path('', views.login_fun, name='log'),
    path('logdata',views.logdata_fun),

    path('reg', views.reg_fun, name='reg'),
    path('regdata', views.regdata_fun),

    path('home', views.home_fun,name='home'),
    path('applied', views.applied_fun,name='applied'),

    path('add_job',views.addjob_fun,name='add'),
    path('readdata',views.readdata_fun),

    path('display', views.display_fun, name='display'),
    path('apply/<int:id>', views.apply_fun, name='apply'),

    path('log_out', views.log_out_fun, name="log_out")

]