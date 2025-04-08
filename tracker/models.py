from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('xafa', '😢 Xafa'),
        ('yaxshi', '😐 Yaxshi'),
        ('quvnoq', '😊 Quvnoq'),
        ('hayajonli', '😁 Hayajonli'),
        ('g\'azablangan', '😠 G\'azablangan'),
    ]

    SLEEP_QUALITY_CHOICES = [
        ('yomon', 'Yomon'),
        ('o\'rtacha', 'O\'rtacha'),
        ('yaxshi', 'Yaxshi'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=15, choices=MOOD_CHOICES)
    stress_level = models.PositiveIntegerField()
    sleep_quality = models.CharField(max_length=10, choices=SLEEP_QUALITY_CHOICES)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.mood}"

