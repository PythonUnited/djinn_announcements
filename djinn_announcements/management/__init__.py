from django.contrib.contenttypes.models import ContentType
from django.db.models import signals
from django.contrib.auth.models import Permission
from djinn_announcements import models


def init_djinn_announcements(**kwargs):

    announcement_contenttype = ContentType.objects.get(
        app_label='djinn_announcements', model='announcement')
    add_pressquestion, created = Permission.objects.get_or_create(
        codename="add_announcement",
        content_type=announcement_contenttype,
        defaults={'name': 'Can add announcement'})

    serviceannouncement_contenttype = ContentType.objects.get(
        app_label='djinn_announcements', model='serviceannouncement')
    add_pressquestion, created = Permission.objects.get_or_create(
        codename="add_serviceannouncement",
        content_type=serviceannouncement_contenttype,
        defaults={'name': 'Can add serviceannouncement'})


#signals.post_syncdb.connect(init_djinn_announcements, sender=models)
