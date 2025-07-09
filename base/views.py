from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def type_list (request):
    return render(request, 'type_list.html')