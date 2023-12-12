from django.shortcuts import render, redirect
from .models import Example

# Create your views here.
def home(request):
    return render(request,'home.html')

def viewport(request):
    if request.method=='POST':
        #access values from form
        n=request.POST['name']
        inco=request.POST['inc']
        inv=request.POST['invest']
        expen=request.POST['exp']
        sav=request.POST['savings']
        m=Example.objects.create(name=n,expenses=expen,savings=sav,investment=inv,income=inco)
        m.save()
        return redirect('/seechart')
        #return HttpResponse('data inserted successfully')
    else:
            #print('request is:',request.method)
            return render(request,'home.html')


def seechart(request):
    m=Example.objects.all()
    #return HttpResponse('data fetched')
    for x in m:
         s=x.income
         l=(x.savings / s) * 100
         a=(x.expenses / s) * 100
         b=(x.investment / s) * 100
    context={}
    context['det'] = m
    context['sav'] = l
    context['exp'] = a
    context['inv'] = b
    return render(request,'viewportfolio.html', context)