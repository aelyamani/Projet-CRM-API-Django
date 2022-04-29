from datetime import datetime
import email
from unicodedata import name
from venv import create
from django.test import TestCase
from .models import Client, Note
from django.contrib.auth.models import User

# Test Note:
# Voir combien de note sont présentes dans notre DB
# Ajout, modification et suppression d'une note


class NoteTestCase(TestCase):

    # Constance nom de la note
    TEST_NOTE_NAME = "Je test une note"

    # Methode de d'initialisation
    def setUp(self):
        self.user = User.objects.create(
            username='aelyamani', email="testg@est.fr")
        self.client = Client.objects.create(name="Test client", contact_person="ddsd", email="tre@gsj.com",
                                            phone="0762804444", website='tstt.com', created_by=self.user, created_at=datetime.now())
        self.noteTestElement = Note()
        self.noteTestElement.client = self.client
        self.noteTestElement.name = self.TEST_NOTE_NAME
        self.noteTestElement.body = "Je fais des test unitaire pour les notes upd"
        self.noteTestElement.created_by = self.user
        self.noteTestElement.save()

    # Creation d'une note
    def test_create_note(self):
        nbr_of_note_before_add = Note.objects.count()

        new_note = Note()
        new_note.client = self.client
        new_note.name = "Test unit Note"
        new_note.body = "Je fais des test unitaire pour les notes"
        new_note.created_by = self.user
        new_note.save()

        nbr_of_note_after_add = Note.objects.count()

        self.assertTrue(nbr_of_note_after_add == nbr_of_note_before_add + 1)

    # Mise à jour d'une note
    def test_update_note(self):

        self.assertEqual(self.noteTestElement.name, self.TEST_NOTE_NAME)

        self.noteTestElement.name = 'Nom changer'
        self.noteTestElement.save()

        tempElement = Note.objects.get(
            pk=self.noteTestElement.pk)

        self.assertEqual(tempElement.name, 'Nom changer')

    # Suppression d'une note
    def test_delete_note(self):

        nbr_of_notes_before_delete = Note.objects.count()

        self.noteTestElement.delete()

        nbr_of_notes_after_delete = Note.objects.count()

        self.assertTrue(nbr_of_notes_after_delete ==
                        nbr_of_notes_before_delete - 1)
