from django.urls import path, include
from .views import DashboardView, KPIDetailView, Ibyakozwe, District_chartView, Sector_chartView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('kpi/<int:pk>', KPIDetailView.as_view(), name='kpi-detail'),
    path('ibyakozwe/<int:pk>', Ibyakozwe.as_view(), name='ibyakozwe'),
    path('ibisigaye/<int:pk>', Ibyakozwe.as_view(), name='ibisigaye'),
    path('ibyakozwe_sector/<int:pk>', Ibyakozwe.as_view(), name='ibyakozwe_sector'),
    path('ibisigaye_sector/<int:pk>', Ibyakozwe.as_view(), name='ibisigaye_sector'),
    path('kpi/charts/<int:pk>', District_chartView.as_view(), name='kpi_charts'),
    path('sector_chart/charts', Sector_chartView.as_view(), name='sector_charts'),
]