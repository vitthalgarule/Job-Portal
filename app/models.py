from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    otp=models.IntegerField()
    role=models.CharField(max_length=50)
    is_activate = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class candidate(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    contatct=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="app/img/candidate/")

class company(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=100,default='Default Address')
    company_description=models.CharField(max_length=100,default='Default Address')

    logo=models.ImageField(upload_to="app/img/company/")

class jobposttable(models.Model):
    company_id=models.ForeignKey(company,on_delete=models.CASCADE)
    jobname=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    jobdescription=models.CharField(max_length=100)
    expirience=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    qulification=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    website=models.CharField(max_length=50)
    responsibility=models.CharField(max_length=300,default="")
    address=models.CharField(max_length=100,default="")
    logo=models.ImageField(upload_to="app/img/job/") 


class candidatedetail(models.Model):
    jobid=models.ForeignKey(jobposttable,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    qulification=models.CharField(max_length=150)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    image=models.ImageField(upload_to="app/img/candidate/profile/")
    resume=models.ImageField(upload_to="app/img/candidate/resume/")