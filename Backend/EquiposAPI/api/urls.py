from django.urls import path
from .views import PatientView, LaboratoristView, LabResultsView, DashboardCountsView

urlpatterns = [
    # Pacientes
    path('pacientes/', PatientView.as_view(), name='patients_list'),
    path('pacientes/<int:id>/', PatientView.as_view(), name='patient_process'),
]

