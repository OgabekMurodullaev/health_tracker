from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'avatar_preview')
    list_filter = ('birth_date',)
    search_fields = ('user__username', 'bio')
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        return f'<img src="{obj.avatar.url}" style="width: 50px; height: 50px; border-radius: 50%;" />'
    avatar_preview.allow_tags = True
    avatar_preview.short_description = 'Avatar'