from django.http import Http404
from django.shortcuts import render
from requests import request
from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import Client
from .models import Note
from team.models import Team
from lead.models import Lead

from .serializers import ClientSerializer, NoteSerializer


# Pagination des clients
class ClientPagination (PageNumberPagination):
    page_size = 5


# Vue api ressource client
class ClientViewSet (viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    pagination_class = ClientPagination
    queryset = Client.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'contact_person']

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team=team)


# Vue api ressource note
class NoteViewSet (viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id']
        serializer.save(team=team, created_by=self.request.user,
                        client_id=client_id)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')
        return self.queryset.filter(team=team).filter(client_id=client_id)


# Fonction api de suppresion note
# TODO a revoir
@api_view(['POST'])
def delete_note(request, note_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    note = team.clients.filter(pk=note_id)
    note.delete()

    return Response({'message': 'La note a bien été supprimer'})


# Fonction de suppression client
@api_view(['POST'])
def delete_client(request, client_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    client = team.clients.filter(pk=client_id)
    client.delete()

    return Response({'message': 'Le client a bien été supprimer'})


# Fonction de convertion lead en client
# TODO Revoir la partie front pour supprimer le lead une fois convertit
@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']

    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404

    client = Client.objects.create(team=team, name=lead.company, contact_person=lead.contact_person,
                                   email=lead.email, phone=lead.phone, website=lead.website, created_by=request.user)

    return Response()
