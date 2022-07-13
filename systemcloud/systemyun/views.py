from django.shortcuts import render

# Create your views here.
def hello(request):

    return render(request,'index.html')
    #return render(request,'dddd.html')

def add_account(request):
    return render(request, 'add_account.html')

def del_account(request):
    return render(request, 'del_account.html')

def revise(request):
    return render(request, 'revise.html')

def purchase_admin(request):
    return render(request, 'purchase_admin.html')

def donate(request):
    return render(request, 'donate.html')

def human_services(request):
    return render(request, 'human_services.html')

