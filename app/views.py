
from http.client import HTTPResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from random import randint, random

# Create your views here.

def index1(request):
    return render(request,"app\index\index.html")


def index(request):
    return render(request,"app\index.html")

def index2(request):
    return render(request,"app\index2.html")

def signup(request):
    return render(request,"app\signup.html")


def registration(request):
    if request.POST['role'] == "candidate":
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message="user alredy exsists"
            return render(request,"app\signup.html",{'msg':message})
        else :
            if password == cpassword:
                otp = randint(10000,99999)
                send_mail(
                    'Your OTP',
                    f'Your OTP is: {otp}',
                    'vitthalgarule113@gmail.com',  # Sender's email
                    [email],  # List of recipients
                    fail_silently=False,
                )
                newuser=UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand=candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
            return render(request,"app\otpverify.html",{'email':email})
    else:
        print("company registration")
        if request.POST['role'] == "company":
            role=request.POST['role']
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']

            user = UserMaster.objects.filter(email=email)

            if user:
                message="user alredy exsists"
                return render(request,"app\signup.html",{'msg':message})
            else :
                if password == cpassword:
                    otp = randint(1000,9999)
                    send_mail(
                    'Your OTP',
                    f'Your OTP is: {otp}',
                    'vitthalgarule113@gmail.com',  # Sender's email
                    [email],  # List of recipients
                    fail_silently=False,
                )
                    newuser=UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcand=company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app\otpverify.html",{'email':email})
       

                

def otppage(request):
    return render(request,"app\otpverify.html")

def otpverifiy(request):
    email=request.POST['email']
    otp=int(request.POST['otp'])
    
    user=UserMaster.objects.get(email=email)

    if user:
        if user.otp==otp:
            message="otp verify successfully...."
            return render(request,"app\login.html",{'msg':message})
        else:
            message="wrong otp"
            return render(request,"app\otpverify.html",{'msg':message})

    else:
        message="no user"
        return render(request,"app\signup.html",{'msg':message})
    
def login(request):
    return render(request,"app\login.html")

    

def LoginUser(request):
    if request.POST['role']=="candidate":
        email=request.POST['email']
        password=request.POST['password']

        user=UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="candidate":
                can=candidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['firstname']=can.firstname
                request.session['lastname']=can.lastname
                request.session['email']=user.email
                request.session['password']=user.password
                return redirect('index')
            else:
                message="password dosent match"
                return render(request,"app\login.html",{'msg':message})
        else:
            message="user not found"
            return render(request,"app\login.html",{'msg':message})
    else:
            
        if request.POST['role']=="company":
            email=request.POST['email']
            password=request.POST['password']

            user=UserMaster.objects.get(email=email)
            if user:
                if user.password==password and user.role=="company":
                    comp=company.objects.get(user_id=user)
                    request.session['id']=user.id
                    request.session['role']=user.role
                    request.session['id1']=comp.id
                    request.session['company_name']=comp.company_name
                    request.session['firstname']=comp.firstname
                    request.session['lastname']=comp.lastname
                    request.session['email']=user.email
                    request.session['password']=user.password
                    return redirect('companyindex')
                else:
                    message ="password dosent match"
                    return render(request,"app\login.html",{'msg':message})
            else:
                message="user not found"
                return render(request,"app\login.html",{'msg':message})
            
        else:
            message="select role"
            return render(request,"app\login.html",{'msg':message})
        
def profile(request,pk):
    user=UserMaster.objects.get(pk=pk)
    can=candidate.objects.get(user_id=user)
    return render(request,"app\profile.html",{'user':user,'can':can})


def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "candidate":
        can = candidate.objects.get(user_id=user)
        can.firstname = request.POST['firstname']
        can.lastname = request.POST['lastname']
        can.city = request.POST['city']
        can.state = request.POST['state']
        can.contatct = request.POST['contact']
        can.address = request.POST['address']
        can.dob = request.POST['dob']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['image']
        can.save()
        url = f'/index/{pk}'  # formatting url
        return redirect(url)  # corrected redirect method
    else:
        return render(request, "app\login.html")
    
def candidatejobtable(request):
   jobs=jobposttable.objects.all()
   return render(request,"app\joblist.html",{'alljob':jobs})

def candidatejobdetail(request):
   
   jobdetail=jobposttable.objects.all()
   return render(request,"app\job-detail.html",{'jobdetail':jobdetail})

def apply(request):
    return render(request,"app\jobapply.html")

def applyjob(request,pk): 
    
    if request.method=="POST":
        comp=jobposttable.objects.get(pk=pk)
        name=request.POST['name']
        email=request.POST['email']
        qulification=request.POST['qualification']
        contact=request.POST['contact']
        address=request.POST['address']
        image=request.FILES['image']
        resume=request.FILES['resume']

        apply=candidatedetail.objects.create(jobid=comp,name=name,email=email,qulification=qulification,contact=contact,address=address,image=image,resume=resume)

        message="applyed"
        return render(request,"app\jobapply.html",{'msg':message})
    else:
       
        return render(request,"app\jobapply.html")
    

def canlogout(request):
    del request.session['email']
    del request.session['password']

    return redirect('index1')
    

    
########################################## company side ########################################
    
def companyindex(request):
   return render(request,"company\index.html")

def cprofile(request,pk):
    user=UserMaster.objects.get(pk=pk)
    comp=company.objects.get(user_id=user)
    return render(request,"company\cprofile.html",{'user':user,'comp':comp})

def cprofileUpdate(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user.role == 'company':
        comp=company.objects.get(user_id=user)
        comp.firstname=request.POST['firstname']
        comp.lastname=request.POST['lastname']
        comp.company_name=request.POST['companyname']
        comp.state=request.POST['state']
        comp.city=request.POST['city']
        comp.contact=request.POST['contact']
        comp.address=request.POST['address']
        comp.company_description=request.POST['description']
        comp.logo=request.FILES['image']
        comp.save()
        url = f'/companyindex/{pk}'
        return redirect(url)
    else:
        return render(request,"app\login.html")
    
def jobpost(request):
    return render(request,"company\jobpost.html")

def jobposting(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if request.method=="POST":
        comp=company.objects.get(user_id=user)
        jobname=request.POST['jobname']
        companyname=request.POST['companyname']
        jobdescription=request.POST['jobdescription']
        experience=request.POST['experience']
        qulification=request.POST['qualification']
        salary=request.POST['salary']
        contact=request.POST['contact']
        email=request.POST['email']
        address=request.POST['address']
        website=request.POST['website']
        responsibility=request.POST['responsibility']
        logo=request.FILES['logo']

        newjob=jobposttable.objects.create(company_id=comp,
                                            jobname=jobname,
                                            companyname=companyname,
                                            jobdescription=jobdescription,
                                            expirience=experience,
                                            salary=salary,
                                            qulification=qulification,
                                            contact=contact,
                                            email=email,
                                            website=website,
                                            address=address,
                                            responsibility=responsibility,
                                            logo=logo)
        message="data save "
        return render(request,"company\jobposttable.html",{'msg':message})
    else:
        
        return render(request,"company\jobpost.html")
    
def jobtable(request):
   jobs=jobposttable.objects.all()
   return render(request,"company\jobposttable.html",{'alljob':jobs})

def canlist(request):
   can=candidatedetail.objects.all()
   return render(request,"company\candidatelist.html",{'allcan':can})



def complogout(request):
    del request.session['email']
    del request.session['password']

    return redirect('index1')


def send_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email:
            # Generate OTP
            otp = randint(10000,99999)

            # Send OTP to the email
            send_mail(
                'Your OTP',
                f'Your OTP is: {otp}',
                'vitthalgarule113@gmail.com',  # Sender's email
                [email],  # List of recipients
                fail_silently=False,
            )

            return JsonResponse({'status': 'success', 'message': 'OTP sent successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Email not provided.'})
    else:
        return render(request,"app\otp.html")
    




###################################ADMIN#   #############################################
    
def login1(request):
    return render(request,"panel\login.html")

def adindex(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"panel\index.html")
    else:
        return render(request,"panel\login.html")


def adminlogin(request):
    username = request.POST['name']
    password = request.POST['pass']
 
    if username=="jobportal" and password=="vitt@1234":
        request.session['username']= username
        request.session['password']=password
        return redirect('indexadmin')
    else:
        return render(request,"panel\login.html")
    
def companylist(request):
    return render(request,"panel\companylist.html")

def candidatelist(request):
    return render(request,"panel\candidatelist.html")

def comptable(request):
    allcomp=UserMaster.objects.filter(role="company")
    return render(request,"panel\companylist.html",{'allcomp':allcomp})

def cantable(request):
    allcan=UserMaster.objects.filter(role="candidate")
    return render(request,"panel\candidatelist.html",{'allcan':allcan})

def userdelete(request,pk):
    user=UserMaster.objects.get()
    user.delete()
    return redirect('indexadmin')


