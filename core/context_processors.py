from django.contrib.auth.models import User

def user_count(request):
    total_users = User.objects.count()
    return {
        'total_users': total_users,
    }
