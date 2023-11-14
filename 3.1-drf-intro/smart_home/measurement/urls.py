from django.urls import path

from .views import SensorCreateAPIView, MeasurementCreateAPIView, SensorRetrieveUpdateAPIView

urlpatterns = [
    path('sensors/', SensorCreateAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
