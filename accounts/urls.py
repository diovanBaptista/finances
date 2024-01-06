from django.urls import path, include
from .api import viewsets
from rest_framework import routers

accouts_routers = routers.DefaultRouter()

accouts_routers.register(
    "accounts",
    viewsets.AccountViewSet,
    basename="accounts"
)

accouts_routers.register(
    "installments",
    viewsets.InstallmentViewSet,
    basename="installments"
)

urlpatterns = [
    path('accounts/', include(accouts_routers.urls)),
]
