from django.contrib import admin
from .models.announcement import Announcement
from .models.announcementupdate import AnnouncementUpdate


class AnnouncementUpdateInline(admin.TabularInline):
    model = AnnouncementUpdate


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', )
    raw_id_fields = ['creator', 'changed_by', 'parentusergroup']
    search_fields = ['title']
    inlines = [ AnnouncementUpdateInline, ]

admin.site.register(Announcement, AnnouncementAdmin)
