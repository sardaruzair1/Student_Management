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

# Update records
def Update(request,id):
    if request.method == 'POST':
        data= Students.objects.get(pk=id)
        form=StudentsForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:    
        
        data= Students.objects.get(pk=id)
        form = StudentsForm(instance=data)
    contex={
        'form':form
    }
    return render(request,'app/update.html',contex)

# delete records
def delete(request,id):
    a = Students.objects.get(pk=id)
    a.delete()
    return redirect('/')