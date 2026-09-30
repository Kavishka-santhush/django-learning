from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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

def add_topic_view(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TopicForm()
    
    context = {'form': form}
    return render(request, 'add_topic.html', context)

# අලුතින් එකතු කළ Signup View එක
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'ගිණුම සාර්ථකව සාදන ලදී: {username}! දැන් ඔබට Login විය හැක.')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'signup.html', context)