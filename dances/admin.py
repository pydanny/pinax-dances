from django.contrib import admin

from dances.models import Dance

class DanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'creator', 'created')

admin.site.register(Dance, DanceAdmin)




