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

accouts_routers.register(
    "tipo_conta",
    viewsets.TipoContaViewSet,
    basename="tipo_conta"
)

accouts_routers.register(
    "conta_mensais",
    viewsets.ContaMensaisViewSet,
    basename="conta_mensais"
)

urlpatterns = [
    path('accounts/', include(accouts_routers.urls)),
]
