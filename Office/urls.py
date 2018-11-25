from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients', views.patient, name='patients'),
    path('patient_detail/<int:id>', views.patient_detail, name='patient_detail'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('add_drug', views.add_drug, name='add_drug'),
    path('drugs', views.drugs, name='drugs'),
    path('drug_detail/<int:id>', views.drug_detail, name='drug_detail'),
]
