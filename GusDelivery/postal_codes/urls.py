from django.urls import path
from .views import FileUploadView

app_name = 'postal_codes'

urlpatterns = [
    path('cargar-archivo/<str:filename>', FileUploadView.as_view(), name='upload-data'),    
]