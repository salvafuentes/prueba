from django.urls import include, path
from . import views

urlpatterns=[
    path('homepage/', views.homepageView, name="homepage"),
    path('subirauto/', views.subirauto, name="subirauto"),
    path('verautos/', views.verautos, name="verautos")
]