from django.shortcuts import render

# Create your views here.
def homemenu(request):
    return render(request,'common/homemenu.html')
    
def getmenu(request):
    return render(request,'common/menu.html')       

