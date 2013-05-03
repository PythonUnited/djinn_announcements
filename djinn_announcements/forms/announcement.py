from django import forms
from django.utils.translation import ugettext_lazy as _
from djinn_contenttypes.forms.base import BaseForm
from djinn_announcements.models.announcement import Announcement


class AnnouncementForm(BaseForm):

    text = forms.CharField(label=_("Announcement"),
                           widget=forms.Textarea(
            attrs={'rows': '5'})
                           )

    @property
    def labels(self):

        return {'submit': _('Save'),
                'cancel': _('Cancel'),
                'header': _('Add announcement')}

    class Meta:

        model = Announcement
        fields = ("title", "text", "creator")
