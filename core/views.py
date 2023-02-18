from django.shortcuts import render
from .models import*
from .forms import*
def home(request):
    info = Info.objects.all()

    context={
       
        "info":info,
    
    }

    return render(request,'index.html',context)

def form(request):
    context = {}
    if request.method == 'GET':
        context['form']=InfoForm
        return render(request,'form.html',context=context)
    else:
        forms=InfoForm(request.POST)
        if forms.is_valid():

            forms.save()
            context['form']=InfoForm
            return render(request,'form.html',context=context)



