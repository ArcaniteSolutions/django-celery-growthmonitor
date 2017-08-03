from abc import ABCMeta

from django.contrib import admin


class AJobAdmin(admin.ModelAdmin):
    __metaclass__ = ABCMeta

    fields = ('timestamp', 'identifier', 'state', 'status', 'duration', 'slug', 'closure')
    readonly_fields = ('timestamp', 'state', 'status', 'duration')
    list_display = ('__str__', 'timestamp', 'state', 'status', 'duration', 'closure')


class AFieldsForDataFileAdmin:
    __metaclass__ = ABCMeta

    fields = ('data',)
    readonly_fields = ('data',)
    can_delete = False
