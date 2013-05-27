from django import forms
from django.utils.translation import ugettext_lazy as _
from djinn_contenttypes.forms.base import BaseForm
from djinn_announcements.models.serviceannouncement import ServiceAnnouncement
from djinn_announcements.settings import SERVICEANNOUNCEMENT_STATUS_VOCAB, \
    ANNOUNCEMENT_PRIORITY_VOCAB


class ServiceAnnouncementForm(BaseForm):
    
    start_date = forms.DateTimeField(label=_("Start date"),
                                     widget=forms.DateTimeInput(
            attrs={'class': 'datetime'},
            format="%d-%m-%Y %H:%M"
            )
                                     )

    end_date = forms.DateTimeField(label=_("(Expected) end date"),
                                     required=False,
                                     widget=forms.DateTimeInput(
            attrs={'class': 'datetime'},
            format="%d-%m-%Y %H:%M"
            )
                                     )
    
    status = forms.IntegerField(label=_("Status"),
                                required=False,
                                initial=-1,
                                widget=forms.Select(
            choices=SERVICEANNOUNCEMENT_STATUS_VOCAB)
                                )

    priority = forms.IntegerField(label=_("Priority"),
                                  initial=0,
                                  widget=forms.Select(
            choices=ANNOUNCEMENT_PRIORITY_VOCAB)
                                  )

    text = forms.CharField(label=_("Description"),
                           max_length=150,
                           help_text="Maximaal 150 karakters",
                           widget=forms.Textarea(
            attrs={'class': 'full wysiwyg',
                   'data-maxchars': 150,
                   'rows': '5'})
    )

    class Meta(BaseForm.Meta):
        model = ServiceAnnouncement
