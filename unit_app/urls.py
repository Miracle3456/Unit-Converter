from django.urls import path
from .views import UnitView

urlpatterns = [
path('' , UnitView.as_view() , name = 'calculate_url')
]