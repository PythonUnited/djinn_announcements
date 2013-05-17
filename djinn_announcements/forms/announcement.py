from django import forms
from django.utils.translation import ugettext_lazy as _
from djinn_contenttypes.forms.base import BaseForm
from djinn_announcements.models.announcement import Announcement


class AnnouncementForm(BaseForm):

    text = forms.CharField(label=_("Announcement"),
                           help_text="Maximaal 150 karakters",
                           widget=forms.Textarea(
            attrs={'class': 'full count_characters', 'data-maxchars': '150', 'rows': '5'})
    )

    @property
    def labels(self):

        return {'submit': _('Save'),
                'cancel': _('Cancel'),
                'header': _('Add announcement')}

    class Meta(BaseForm.Meta):
        model = Announcement
        fields = ("title", "text")
