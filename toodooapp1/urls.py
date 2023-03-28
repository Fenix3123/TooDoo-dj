from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.get_dashboard, name="dashboard"),
    path('createTooDoo/', views.createTooDoo, name="createtoodoo"),
    path('toodooinfo/<str:pk>', views.updateTooDoo, name="toodooinfo"),
    path('toodoodelete/<str:pk>', views.deleteTooDoo, name="toodoodelete"),
    path('loginRegistration/', views.loginPage, name="loginRegistration"),
    path('register/', views.registerUser, name="registerUser"),
    path('logout/', views.logoutUser, name="logout")
]
