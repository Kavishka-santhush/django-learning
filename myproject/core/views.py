from django.shortcuts import render

def home_view(request):
    # HTML එකට යවන්න ඕන දත්ත (Data) Dictionary එකක් විදිහට හැදීම
    context = {
        'name': 'සන්තුෂ්',
        'course': 'Django මූලික සිට උසස් මට්ටමට (Beginner to Advanced)',
        'technologies': ['Python', 'Django', 'HTML/CSS', 'Database'],
    }
    
    # render කරනකොට context එකත් එකතු කරලා යැවීම
    return render(request, 'index.html', context)