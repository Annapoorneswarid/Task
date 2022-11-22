
from . models import Services,Form
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def demo(request):
    obj=Services.objects.all()

    return render(request,"index.html",{'result':obj})



def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
            user.save();
            return redirect('login')
        else:
            messages.info(request,"Password Not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def forms(request):
    if request.method =='POST':
        name = request.POST.get('name', )
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        district = request.POST.get('district', )
        branch = request.POST.get('branch', )
        account_type = request.POST.get('account_type', )

        form=Form(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,district=district,branch=branch,account_type=account_type)
        form.save();

    return render(request,"form.html")

def msg(request):
    obj2 = Form.objects.all()
    return render(request, 'msg.html', {'result2':obj2})

