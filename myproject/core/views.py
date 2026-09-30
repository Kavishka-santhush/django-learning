from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

def home_view(request):
    all_topics = Topic.objects.all()
    context = {
        'name': 'සන්තුෂ්',
        'course': 'Django මූලික සිට උසස් මට්ටමට (Beginner to Advanced)',
        'topics': all_topics,
    }
    return render(request, 'index.html', context)

# අලුත් Topic එකක් එකතු කිරීම සඳහා View එක
def add_topic_view(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()  # ඩේටාබේස් එකේ සේව් වීම
            return redirect('home')  # සාර්ථක වුණාම මුල් පිටුවට යැවීම
    else:
        form = TopicForm()
    
    context = {'form': form}
    return render(request, 'add_topic.html', context)