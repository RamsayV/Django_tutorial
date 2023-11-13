from django.shortcuts import render
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
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })