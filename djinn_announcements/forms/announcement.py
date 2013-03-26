from django import forms
from djinn_announcements.models.announcement import Announcement


class AnnouncementForm(forms.ModelForm):

    @property
    def labels(self):

        return {'submit': 'Plaats mededeling', 
                'cancel': 'Annuleren',
                'header': 'Voeg mededeling toe'}

    class Meta:
        widgets = {'creator': forms.HiddenInput(),
                   'changed_by': forms.HiddenInput()}
        model = Announcement
        fields = ('title', 'text', 'creator', 'changed_by')
