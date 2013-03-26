from django import forms
from django.utils.translation import ugettext_lazy as _
from pgcontent.fields import NoScriptCharField
from djinn_announcements.models.announcementupdate import AnnouncementUpdate


class AnnouncementUpdateForm(forms.ModelForm):

    date = forms.DateTimeField(label=_("Date"),
                                     widget=forms.DateTimeInput(
            attrs={'class': 'datetime'},
            format="%d-%m-%Y %H:%M"
            )
                                     )    
    text = NoScriptCharField(label=_("Description"),
                             widget=forms.Textarea(
            attrs={'class': 'full wysiwyg', 'id': 'update_text',
                   'rows': '5'})
    )

    @property
    def labels(self):

        return {'submit': 'Opslaan', 'cancel': 'Annuleren'}

    class Meta:
        model = AnnouncementUpdate
        widgets = {'announcement': forms.HiddenInput()}
