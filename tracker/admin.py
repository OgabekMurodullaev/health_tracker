from django.contrib import admin

from tracker.models import MoodEntry


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mood_with_emoji', 'stress_level', 'sleep_quality', 'note_short')
    list_filter = ('date', 'mood', 'sleep_quality')
    search_fields = ('user__username', 'note')
    list_per_page = 20

    def mood_with_emoji(self, obj):
        mood_dict = dict(MoodEntry.MOOD_CHOICES)
        return mood_dict[obj.mood]
    mood_with_emoji.short_description = 'Kayfiyat'

    def note_short(self, obj):
        return obj.note[:50] + '...' if obj.note and len(obj.note) > 50 else obj.note
    note_short.short_description = 'Eslatma'
