from django.shortcuts import render

def home_view(request):
    # index.html ෆයිල් එක බ්‍රව්සර් එකට යැවීම
    return render(request, 'index.html')