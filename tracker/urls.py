from django.urls import path

from tracker.views import home_page, add_mood_entry, edit_mood_entry, delete_mood_entry, mood_entry_list, dashboard

urlpatterns = [
    path('', home_page, name='home'),
    path('list/', mood_entry_list, name='list-entry'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-entry/', add_mood_entry, name='add-entry'),
    path('<int:pk>/edit-entry/', edit_mood_entry, name='edit-entry'),
    path('<int:pk>/delete/', delete_mood_entry, name='delete-entry'),
]