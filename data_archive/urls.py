from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # path('export_csv/', HomeView.as_view(), name="export-csv"),
    path('<str:discoverer>/', ObjectView.as_view(), name="objectpage"),
]
