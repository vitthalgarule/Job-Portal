from django.urls import path,include
from .import views
urlpatterns = [
   path("",views.index1,name="index1"),
   path("index/",views.index,name="index"),
   path("sign/",views.signup,name="sign"),
   path("registration/",views.registration,name="registration"),
   path("otp/",views.otppage,name="otp"),
   path("otpverify/",views.otpverifiy,name="otpverify"),
   path("login/",views.login,name="login"),
   path("LoginPage/",views.LoginUser,name="LoginPage"),
   path("profile/<int:pk>",views.profile,name="profile"),
   path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
   path("candidatejobtable/",views.candidatejobtable,name="candidatejobtable"),
   path("candidatejobdetail/",views.candidatejobdetail,name="candidatejobdetail"),
   path("apply/",views.apply,name="apply"),
   path("applyjob/<int:pk>",views.applyjob,name="applyjob"),
   path("canlogout/",views.canlogout,name="canlogout"),


#####################################################################################

   path("companyindex/",views.companyindex,name="companyindex"),
   path("cprofile/<int:pk>",views.cprofile,name="cprofile"),
   path("cprofileUpdate/<int:pk>",views.cprofileUpdate,name="cprofileUpdate"),
   path("jobpost/",views.jobpost,name="jobpost"),
   path("jobposting/<int:pk>",views.jobposting,name="jobposting"),
   path("jobtable/",views.jobtable,name="jobtable"),
   path("canlist/",views.canlist,name="canlist"),
   path("companylogout/",views.complogout,name="companylogput"),



   ################################################################################
   path('send_otp/', views.send_otp, name='send_otp'),




   ##################################ADMIN################################################

   path("login1/",views.login1,name="login1"),
   path("indexadmin/",views.adindex,name="indexadmin"),
   path("adminlogin/",views.adminlogin,name="adminlogin"),
   path("companylist/",views.companylist,name="companylist"),
   path("candidatelist/",views.candidatelist,name="candidatelist"),
   path("comptable/",views.comptable,name="comptable"),
   path("cantable/",views.cantable,name="cantable"),
   path("udelete/<int:pk>",views.userdelete,name="udelete"),
   
     
   
]
