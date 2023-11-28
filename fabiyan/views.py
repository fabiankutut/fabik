from django.shortcuts import render

# Create your views here.


def get_page1(request):
    return render(request, 'page1.html')
