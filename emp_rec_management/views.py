from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from emp_rec_management.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'emp_rec_management/home.html')

def employee_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exist!")
            return redirect('employee_signup')

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect('employee_signup')

        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('employee_signup')

        if pass1 != pass2:
            messages.error(request,"Password didn't match!!")
            return redirect('employee_signup')

        if not username.isalnum():
            messages.error(request,"Username must be Alpha-Numeric!")
            return redirect('employee_signup')

        
        myuser = User.objects.create_user(username,email,pass1)

        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        employee_details= EmployeeDetails(user = myuser)
        employee_details.save()
        messages.success(request,"Your Account has been successfully created.")
        return redirect('employee_login')

    return render(request,'emp_rec_management/employee_signup.html')

def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            lname=user.last_name
            return render(request,"emp_rec_management/dashboard.html",{'fname':fname,'lname':lname})

        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')
    return render(request,'emp_rec_management/employee_login.html')

def employee_signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('home')

@login_required
def dashboard(request):
    return render(request,'emp_rec_management/dashboard.html')


@login_required
def emp_profile(request):
    
    context = {}
    data = EmployeeDetails.objects.get(user__id=request.user.id)
    context["data"]=data
    
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        emp_dept = request.POST['emp_dept']
        emp_desig = request.POST['emp_desig']
        start_date = request.POST['start_date']

        user = User.objects.get(id=request.user.id)
        user.first_name = fname
        user.lname_name = lname
        user.email = email
        user.save()

        data.contact_no = contact_no
        data.emp_dept = emp_dept
        data.emp_desig = emp_desig
        data.start_date = start_date
        data.save()

        context["status"] = "Saved changes successfully"


    return render(request,'emp_rec_management/emp_profile.html',context)

def emp_experience(request):
    return render(request,'emp_rec_management/emp_experience.html')

def emp_education(request):
    return render(request,'emp_rec_management/emp_education.html')  

def emp_edit_profile(request):
    return render(request, 'emp_rec_management/emp_edit_profile.html')
    