from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control mb-2'}),
            'description' : forms.Textarea(attrs={'class':'form-control mb-2'}),
            'status' : forms.Select(choices=[('Done','Done'),('In progress','In progress'),('Not done','Not done')],attrs={'class':'form-control mb-2'})
        }