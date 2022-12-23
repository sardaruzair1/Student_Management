from django.shortcuts import render 
from django.shortcuts import redirect
from .forms import StudentsForm
from .models import Students
# Create your views here.

def Home(request):
    form = StudentsForm()
    if request.method == 'POST':
        form=StudentsForm(request.POST)
        form.save()
        StudentsForm()
        
    data = Students.objects.all()    
        
    contex={
        'form':form,
        'data':data
    }
    return render(request,'app/index.html',contex)


def Update(request):
    return render(request,'app/update.html')