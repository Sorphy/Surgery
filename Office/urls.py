from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('patients', views.patient, name='patients'),
    path('patient_detail/<int:id>', views.patient_detail, name='patient_detail'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('add_drug', views.add_drug, name='add_drug'),
    path('drugs', views.drugs, name='drugs'),
    path('drug_detail/<int:id>', views.drug_detail, name='drug_detail'),
    path('delete_drug/<int:id>', views.delete_drug, name='delete_drug'),
    path('update_drug/<int:id>', views.update_drug, name='update_drug'),
    path('update_patient/<int:id>', views.update_patient, name='update_patient'),
    path('delete_patient/<int:id>', views.delete_patient, name='delete_patient'),
    path('prescriptions', views.prescriptions, name='prescriptions'),
    path('add_prescription', views.add_prescription, name='add_prescription'),
    path('prescription_detail/<int:id>', views.prescription_detail, name='prescription_detail'),
    path('update_prescription/<int:id>', views.update_prescription, name='update_prescription'),
    path('delete_prescription/<int:id>', views.delete_prescription, name='delete_prescription'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

