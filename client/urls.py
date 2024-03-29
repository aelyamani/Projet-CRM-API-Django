from .views import FileUploadView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, NoteViewSet, DocumentViewSet, convert_lead_to_client, delete_note, delete_client

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('notes', NoteViewSet, basename='notes')
router.register('documents', DocumentViewSet, basename='documents')

urlpatterns = [
    path('convert_lead_to_client/', convert_lead_to_client,
         name='convert_lead_to_client'),
    path('clients/delete_client/<int:client_id>/',
         delete_client, name='delete_client'),
    path('documents', FileUploadView.as_view()),
    #     TODO Debug la fonction delete_note
    path('clients/delete_note/:id/',
         delete_note, name='delete_note'),
    path('', include(router.urls)),
]
