
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('qreventmanager/',views.qreventmanager,name="qreventmanager"),
    path('qreventmanager_create/',views.qreventmanager_create,name="qreventmanager_create"),
    path('qreventmanager_edit/<int:id>/',views.qreventmanager_edit,name="qreventmanager_edit"),
    path('qreventmanager_delete/<int:id>/',views.qreventmanager_delete,name="qreventmanager_delete"),
    path('qreventmanager_manger/<int:id>/',views.qreventmanager_manger,name="qreventmanager_manger"),
    path('qreventmanager_dwn/<int:id>/',views.qreventmanager_dwn,name="qreventmanager_dwn"),
    path('qrevent_createform/<int:id>/',views.qrevent_createform,name="qrevent_createform"),
    path('client/<int:id>/',views.qrevent_client,name="qrevent_client"),
    
    # path('login/',views.login,name="login")
] 
