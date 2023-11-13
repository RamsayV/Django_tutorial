from django.shortcuts import render
from .models import Finch
finches = [
  {'name': 'Finchley', 'breed': 'House Finch', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'Red crossbill', 'description': 'gentle and loving', 'age': 2},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })
