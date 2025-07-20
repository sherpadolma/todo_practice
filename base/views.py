from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from .AI import create_description_with_ai
import json
# Create your views here.
def home(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', context={'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            name = request.POST.get('name')
            description = request.POST.get('description')
            status = request.POST.get('status')

            Todo.objects.create(
                name = name, 
                description = description, 
                status = status
                )
            # Todo.objects.create(**request.POST)
            return redirect('home') 
        
        elif action == 'generate':
            name = request.POST.get('name')
            generated_description = create_description_with_ai(name)
            dic_generated_description = json.loads(generated_description)  # Convert JSON string to Python dictionary
            status = request.POST.get('status')
            # Call the AI function to generate description
            return render(request, 'create.html', context={'generated_description': dic_generated_description.get('description'), 'name': name, 'status': status})
    
    return render(request, 'create.html', context={"message": "Todo created successfully!"})


def edit_todo(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo_obj)
    if request.method == 'POST':
        form = TodoForm(instance=todo_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'edit.html', context={'form':form})

def delete_todo(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('home')