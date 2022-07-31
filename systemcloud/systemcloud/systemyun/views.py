from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
import request
import models

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

def db_handle(request):
    user_list_obj = models.Demo.objects.all()
    return render(request, 't1.html', {'li': user_list_obj})

# def login(request):
#     if request.method == 'POST':
#         #获取数据 
#         account = request.POST['name']
#         password=request.POST['password']
#         user_list = models.UserIfo.objects.all()
#         #print(user_list)
#         for row in user_list:
#             if row.name ==  account:
#                 if row.password == password:
#                     """设置cookie"""
#                     response = HttpResponse("设置cookie")
#                     ''' max_age 设置过期时间，单位是秒 '''
#                     # response.set_cookie('name', 'tong', max_age=14 * 24 * 3600)
#                     ''' expires 设置过期时间，是从现在的时间开始到那个时间结束 '''
#                     response.set_cookie(name, password, expires=datetime.now()+timedelta(days=14))
#                     return response
#                 else:
#                     return render(request, 'login.html')
#             else:
#                 continue
#     else:
#         return render(request, 'login.html')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html')
    else:
        name = request.POST['name']
        password = request.POST['password']
        rePassword = request.POST['rePassword']
        if password == rePassword:
            user_list = models.UserIfo.objects.all()
            #print(user_list)
            for row in user_list:
    #通过关联ut字段取关联表----正向操作
                if row.name == name:
                    return HttpResponse('名称已被占用')
                else:
                    continue
            else:
                models.UserType.objects.create(name=name)
                models.UserType.objects.create(password=password)
                return render(request, 'yes.html')
                # """设置cookie"""
                # response = HttpResponse("设置cookie")
                # ''' max_age 设置过期时间，单位是秒 '''
                # # response.set_cookie('name', 'tong', max_age=14 * 24 * 3600)
                # ''' expires 设置过期时间，是从现在的时间开始到那个时间结束 '''
                # response.set_cookie(name, password, expires=datetime.now()+timedelta(days=14))
                # return response

