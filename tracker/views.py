from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import json
import datetime

from tracker.forms import MoodEntryForm
from tracker.models import MoodEntry


def home_page(request):
    return render(request, 'home.html')


@login_required
def add_mood_entry(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user  # Foydalanuvchi bilan bog'lash
            mood_entry.save()
            messages.success(request, "Yangi kayfiyat yozildi!")
            return redirect('list-entry')
    else:
        form = MoodEntryForm()
    return render(request, 'mood/add_mood_entry.html', {'form': form})

@login_required
def edit_mood_entry(request, pk):
    mood_entry = get_object_or_404(MoodEntry, pk=pk)
    if request.method == 'POST':
        form = MoodEntryForm(request.POST, instance=mood_entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Kayfiyat ma'lumotlari yangilandi!")
            return redirect('list-entry')
    else:
        form = MoodEntryForm(instance=mood_entry)
    return render(request, 'mood/edit_mood_entry.html', {'form': form})

@login_required
def delete_mood_entry(request, pk):
    mood_entry = get_object_or_404(MoodEntry, pk=pk)
    if request.method == 'POST':
        mood_entry.delete()
        messages.success(request, "Kayfiyat yozuvi o'chirildi!")
        return redirect('list-entry')
    return render(request, 'mood/delete_mood_entry.html', {'mood_entry': mood_entry})


from datetime import datetime
from itertools import groupby
from operator import attrgetter


@login_required
def mood_entry_list(request):
    mood_entries = MoodEntry.objects.filter(user=request.user).order_by('-date')

    # Filtrlash parametrlarini olish
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    mood_filter = request.GET.get('mood')

    # Kalendar bo'yicha filtr
    if start_date:
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            mood_entries = mood_entries.filter(date__gte=start_date)
        except ValueError:
            pass
    if end_date:
        try:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            mood_entries = mood_entries.filter(date__lte=end_date)
        except ValueError:
            pass

    # Kayfiyat bo'yicha filtr
    if mood_filter:
        mood_entries = mood_entries.filter(mood=mood_filter)

    # Kunlar bo'yicha guruhlash
    grouped_entries = {}
    for date, group in groupby(mood_entries, key=attrgetter('date')):
        grouped_entries[date] = list(group)

    context = {
        'grouped_entries': grouped_entries,
        'mood_choices': MoodEntry.MOOD_CHOICES,  # Agar modelda MOOD_CHOICES mavjud bo'lsa
    }
    return render(request, 'mood/mood_entry_list.html', context)

def dashboard(request):
    entries = MoodEntry.objects.filter(user=request.user).order_by('-date')

    # Har bir omil uchun qiymatlarni ajratamiz
    mood_values = {'xafa': 1, 'yaxshi': 2, 'quvnoq': 3, 'hayajonli': 4, 'g\'azablangan': 5}
    stress_levels = [int(entry.stress_level) for entry in entries]
    moods = [mood_values[entry.mood] for entry in entries]
    sleep_quality_values = {'yomon': 1, 'o\'rtacha': 2, 'yaxshi': 3}
    sleep_qualities = [sleep_quality_values[entry.sleep_quality] for entry in entries]
    dates = [entry.date.strftime('%Y-%m-%d') for entry in entries]

    return render(request, 'mood/dashboard.html', {
        'stress_levels': json.dumps(stress_levels),
        'moods': json.dumps(moods),
        'sleep_qualities': json.dumps(sleep_qualities),
        'dates': json.dumps(dates)
    })