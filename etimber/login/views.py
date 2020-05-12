from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import mill,User1,sell,usell,timber,bank,bkdetails,usdetails
 

# Create your views here.

def home(request):
    return render(request, 'index.html')
def login1(request):
    return render(request, 'login1.html')
def login(request):
    return render(request, 'login.html')
def user_sign(request):
    return render(request, 'usersign.html')

def usersign(request):
    return render(request, 'user_sign1.html')   

def loginuser(request):
    if request.method == 'POST':
        uname =request.POST['email']
        pswd = request.POST['pass']
        if uname=='anjana' and pswd=='1234':
            return redirect('adminhome')
        else:

            user = auth.authenticate(username=uname, password=pswd)
            if user is not None:
               auth.login(request, user)
               if User.objects.filter(username=uname,last_name="mill").exists():
                   return render(request, 'homemill.html')
               else:
                    return render(request, 'homeuser.html')    
            else:
                messages.info(request, 'Invalid username/password')
            return render(request, 'login.html')    
    else:
        return render(request, 'login.html')        


def homeuser(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['email']
        email = request.POST['email']
        mob = request.POST['mob']
        loc = request.POST['loc'] 
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if(pass1 == pass2):
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return render(request, 'user_sign1.html')
            else:    
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname, last_name=lname)
                user.save()
                myuser = User1(fname=fname,lname=lname,email=email,mob=mob,loc=loc)
                myuser.save()
                return render(request, 'homeuser.html') 
        else:
            messages.info(request, 'Password Missmatch')
            return render(request, 'user_sign1.html')    
            #return render(request, 'homeuser.html')   
    else:
        return render(request, 'user_sign1.html')        
        
def mill_reg(request):
    if request.method == 'POST':
        mill_name = request.POST['millname']
        username = request.POST['email']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        mill_loc = request.POST['millloc']
        mob = request.POST['millmob']
        if(password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return render(request, 'mill_sign.html')    
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=mill_name,last_name="mill")      
            user.save() 
            mill1=mill(muname=email,mill_name=mill_name,mill_loc=mill_loc,mob=mob,email=email ) 
            mill1.save() 
            return render(request, 'login.html')
            
        else:
            messages.info(request,'Password Missmatch')
            return render(request, 'mill_sign.html')


def selectmill(request):
    u = User.objects.filter(last_name="mill")
    return render(request, 'selectmill.html',{'u':u})
def adddetails(request,username):
    u=mill.objects.get(email=username)
    return render(request, 'adddetails.html',{'u':u})


def sell_mill(request):
    if request.method == 'POST':
        
        uname = request.POST['uname']
        name=request.POST['name']
        wid=request.POST['wid']
        type_wd = request.POST['t1']
        length = request.POST['t2']
        width = request.POST['t3']
        rate = request.POST['t4']
    msell=sell(user="null",usname="null",uname=uname,m_name=name,wood_id=wid,type_of_wood= type_wd,length=length,width=width,rate=rate,status="not booked")
    msell.save()    
    return render(request, 'adddetails.html')       

def mill1(request):
    if request.method == 'POST':
        mill = request.POST['mill']
        loc = request.POST['loc']
        
        m = mill.objects.filter(uname=mill)
        return render(request, 'mill1.html',{'m': m})

    else:
        return render(request,'selectmill.html') 

def mill_list(request):
    m = mill.objects.filter()
    return render(request,'mill_list.html',{'m':m})

def millhome(request,muname):
    m = mill.objects.filter(uname=muname)
    return render(request,'mill1.html',{'m': m})    
def expression(request):
    a=int(request.GET['t2'])
    b=int(request.GET['t3'])
    c=b*b*a/2304
    return render(request,'rate.html',{'result':c}) 
def rate(request):
     return render(request, 'rate.html')  

def usersell1(request):    
    return render(request, 'usersell1.html')
def ursell(request):
    if request.method == 'POST':
       uname = request.POST['u1']
       umail = request.POST['u2'] 
       type_wd = request.POST['s2']
       length = request.POST['t2']
       width = request.POST['t3']
       rate = request.POST['t14']
    usersell=usell(mill="null",mname="null",user=uname,umail=umail,wood=type_wd,length=length,width=width,rate=rate,status="Not booked")
    usersell.save()    
    return render(request, 'usersell1.html')

def uname(request):
    srv=sell.objects.filter( status="mill")
    return render(request, 'userbuy.html',{'srv':srv})
def sell_user(request):
    if request.method == 'POST':
    #  uname = request.POST['uname'] 
       type_wd = request.POST['t1']
       length = request.POST['t2']
       width = request.POST['t3']
       rate = request.POST['t4']
        
    usell=sell(type_of_wood= type_wd,length=length,width=width,rate=rate,status="user")
    usell.save()    
    return render(request, 'usersell.html')
  
def mill_sign(request):
    return render(request, 'mill_sign.html')
def homemill(request):
    return render(request, 'homemill.html')
def userhome(request):
    return render(request, 'homeuser.html')    
def elements(request):
    return render(request, 'elements.html')
def elements1(request):
    return render(request, 'elements1.html')

def contact1(request):
    return render(request, 'contact1.html')
def request(request):
    return render(request, 'request.html')
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def contact11(request):
    return render(request, 'contact11.html')
def contactmill(request):
    return render(request, 'contactmill.html')
def elements11(request):
    return render(request, 'elements11.html')
def aboutmill1(request):
    return render(request, 'aboutmill1.html')
def editprofile(request,muname):
    m = mill.objects.filter(muname=muname) 
    return render(request, 'editprofile.html',{'m':m})



def saveprofile(request,muname):
    if request.method == 'POST':
        mname = request.POST['t1']  
        loc = request.POST['t2'] 
        mmob = request.POST['t3'] 
        memail = request.POST['t4']  
        m = mill.objects.get(muname = muname) 
        m.mill_name = mname
        m.save()
        m.mill_loc = loc
        m.save()
        m.mob = mmob
        m.save()
        m.email =memail
        m.save()
        return redirect('editprofile',muname)

    else:
        return redirect('editprofile',muname)

def view(request):
    m=sell.objects.filter()
    return render(request,'one.html',{'m':m})
def view1(request):
    m=sell.objects.filter()
    return render(request,'one1.html',{'m':m})   
def newfun(request,id):
    s=sell.objects.get(id=id)
    return render(request, 'status.html',{'s': s})  
# def newfun1(request,id):
#     s=sell.objects.get(id=id)
#     return render(request, 'premiumpay.html',{'s': s})  
def status1(request,id):
    if request.method=='POST':
       sta=request.POST['status']
       u=request.POST['email']
       v=request.POST['name']
       s=sell.objects.get(id=id)
       s.status=sta
       s.save()
       s.user=u
       s.save()
       s.usname=v
       s.save()

       messages.info(request,'success')
       return redirect('newfun',id)
       
    else:
        return render(request,'status.html')   

def notification(request):
    no = usell.objects.filter()
    return render(request, 'noti.html',{'no':no})
def notification1(request):
    no = usell.objects.filter()
    return render(request, 'noti1.html',{'no':no})
def notific(request):
    no = usell.objects.filter()
    return render(request, 'notifi.html',{'no':no})    
def millfun(request,id):
    s = usell.objects.get(id=id)
    return render(request, 'mstatus.html',{'s': s})
def mstatus(request,id):
    if request.method=='POST':
       sta=request.POST['status']
       u=request.POST['email']
       v=request.POST['name']
       s=usell.objects.get(id=id)
       s.status=sta
       s.save()
       s.mill=u
       s.save()
       s.mname=v
       s.save()
       messages.info(request,'success')
       return redirect('millfun',id)
    else:
        return render(request,'mstatus.html')     
def payment(request):
    # s=sell.objects.get(id=id)
    return render(request, 'pay.html')   
def membership(request):
    a=bank.objects.filter()
    return render(request, 'membership.html',{'a':a})  
def membership2(request):
    a=bank.objects.filter()
    return render(request, 'membership2.html',{'a':a})      
def credit(request):
    return render(request, 'credit.html')
def debit(request):
    return render(request, 'debit.html')
def nbank(request):
    return render(request, 'nbank.html')
def paypal(request):
    return render(request, 'paypal.html')                         
def product(request):
    m=sell.objects.filter()
    return render(request,'product.html',{'m':m})
def adminhome(request):
    return render(request, 'adminhome.html')    
def mview(request):
    srv=User.objects.filter(last_name="mill")
    return render(request, 'mview.html',{'srv':srv})
def uview(request):
    srv=User1.objects.filter()
    return render(request, 'uview.html',{'srv':srv})
def premium(request):
    if request.method == 'POST':
        amt = request.POST['amt']
        aaa=request.POST['amt1']
        amount=bank(amt=amt,status=aaa)
        amount.save()
    return render(request, 'premium.html')     
 

def notifi(request,uname):
    s = sell.objects.filter(uname=uname,status="booked")
    return render(request, 'notification.html',{'s':s})  
def svisit(request,user,id):
    m=sell.objects.get(user=user,id=id)
    return render(request, 'sitevisit.html',{'m':m}) 
def site(request):
    if request.method == 'POST':
        wid = request.POST['a1']
        user = request.POST['d1']
        umail=request.POST['d2']
        mill=request.POST['d3']
        mmail=request.POST['d4']
        timber=request.POST['d5']
        lenn=request.POST['d6']
        cir=request.POST['d7']
        rate=request.POST['d8']
        sdate=request.POST['date22']
        stime=request.POST['d10']
        site1=bkdetails(wo_id=wid,user=user,uemail=umail,mill=mill,memail=mmail,timber=timber,leng=lenn,cirf=cir,price=rate,svdate=sdate,svtime=stime)
        site1.save()
    return render(request, 'sitevisit.html')
        
def usersite(request,name):
    m = bkdetails.objects.filter(uemail=name)
    return render(request, 'usersite.html',{'m':m}) 


def urnoti(request,uname):
    s = usell.objects.filter(umail=uname,status="booked")
    return render(request, 'urnoti.html',{'s':s})      
def ursite(request,u,id):
    m=usell.objects.get(mill=u,id=id)
    return render(request, 'sitevisit1.html',{'m': m}) 
def site1(request):
    if request.method == 'POST':
    
        user = request.POST['d3']
        umail=request.POST['d4']
        mill=request.POST['d1']
        mmail=request.POST['d2']
        timber=request.POST['d5']
        lenn=request.POST['d6']
        cir=request.POST['d7']
        rate=request.POST['d8']
        sdate=request.POST['date22']
        stime=request.POST['d10']
        sitee=usdetails(user=user,uemail=umail,mill=mill,memail=mmail,timber=timber,leng=lenn,cirf=cir,price=rate,svdate=sdate,svtime=stime)
        sitee.save()
    return render(request, 'sitevisit1.html') 
      
        
def millsite(request,name):
    m = usdetails.objects.filter(memail=name)
    return render(request, 'millsite.html',{'m':m})     
def ueditprofile(request,email):
    m = User1.objects.filter(email=email) 
    return render(request, 'ueditprofile.html',{'m':m})



def usaveprofile(request,email):
    if request.method == 'POST':
        fname = request.POST['t1']  
        lname = request.POST['t2'] 
        memail = request.POST['t3'] 
        mmob = request.POST['t4'] 
        mloc = request.POST['t5'] 
        m = User1.objects.get(email = email) 
        m.fname = fname
        m.save()
        m.lname = lname
        m.save()
        m.email = memail
        m.save()
        m.mob = mmob
        m.save()
        m.loc = mloc
        m.save()
        return redirect('ueditprofile',email)

    else:
        return redirect('ueditprofile',email) 

#  def wood(request):
#     n = timber.objects.filter() 
#     return render(request, 'usersell1.html',{'n':n})


def premiumpay(request):
     if request.method == 'POST':
         ano=request.POST['d1']
         mon=request.POST['d2']
         year=request.POST['d3']
         cvv=request.POST['d4']
         book=timber(cno=ano,month=mon,year=year,cvv=cvv,status="null")
         book.save()
                
         return render(request, 'credit.html')




        








        















