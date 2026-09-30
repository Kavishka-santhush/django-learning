from django.shortcuts import render
from .models import Topic  # අපි හදපු Topic Model එක ගෙන්වා ගැනීම

def home_view(request):
    # ඩේටාබේස් එකේ තියෙන සියලුම Topics ටික ලබා ගැනීම
    all_topics = Topic.objects.all()
    
    context = {
        'name': 'සන්තුෂ්',
        'course': 'Django මූලික සිට උසස් මට්ටමට (Beginner to Advanced)',
        'topics': all_topics,  # ඩේටාබේස් ඩේටා මෙහි ඇතුළත් වේ
    }
    
    return render(request, 'index.html', context)