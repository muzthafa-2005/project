from django.shortcuts import render,redirect
from.models import shirt
from.forms import shirtform


# Create your views here.
#def home_page(request):
   # shirts=["hennis","pitavo","us polo"]
#     pants=["levis","adam hills","gucci"]
#     shorts=["black batton","jocky","cruzo"]
#     tshirts=["nike","adidas","puma"]
#     return render(request,"home.html",{"a":shirts,"b":pants,"c":shorts,"d":tshirts})


# def gents(request):
#     return render(request,"gents.html")

# def kids(request):
#     return render(request,"kids.html")

#listil ullathine html kaanaan return nte ullil oru varible ndaki athilk store iyaa

def home (request):
    return render(request,"home.html")

def shirts(request):
    s=shirt.objects.all()
    return render(request,"shirts.html",{"shirts":s})



def add_shirts(request):
    s=shirtform(request.POST or None)
    if s.is_valid():
        s.save()
        return redirect('shirts')
    return render(request,'add_shirts.html',{"form":s})
#texting git hub



