from django.shortcuts import render,redirect
from userapp.forms import userform,userprofile,UserUpdatedform,rate_of_int
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request,"base.html")

@login_required(login_url="user_login")
def home(request):
    return render(request,"home.html")

def interest(request):
    form=rate_of_int(request.POST,request.FILES)
    senior_citizen=False
    if request.method =="POST":
        noof_year=int(request.POST.get("noof_year"))
        amount=int(request.POST.get("amount"))
        age=int(request.POST.get("age"))
        total_months=noof_year*12
        total_investment = amount * total_months
        if  age >=60 and amount>1000 and noof_year==1 or noof_year==3 or noof_year==5:
            if noof_year==3 and age >=60:
                rate_of_interest="8.3%"
                interest_amount=total_investment*0.083
                total_returns=total_investment + interest_amount
                senior_citizen=True
            elif noof_year==1 and age >=60 :
                rate_of_interest="9.7%"
                interest_amount=total_investment*0.097
                total_returns=total_investment + interest_amount
                senior_citizen=True
            elif noof_year==5 and age >=60:
                rate_of_interest="7.0%"
                interest_amount=total_investment*0.070
                total_returns=total_investment + interest_amount
                senior_citizen=True

        if age <60 and amount>1000 and noof_year==1 or noof_year==3 or noof_year==5:
            if noof_year==1 and age <60:
                rate_of_interest="8.2%"
                interest_amount=total_investment*0.082
                total_returns=total_investment + interest_amount
            elif noof_year==3 and age <60:
                rate_of_interest="6.8%"
                interest_amount=total_investment*0.068
                total_returns=total_investment + interest_amount
            elif noof_year==5 and age <60:
                rate_of_interest="5.5%"
                interest_amount=total_investment*0.055
                total_returns=total_investment + interest_amount

        else:
            return HttpResponse(" <h1> Not applicable for even numbers of year and amount should be greater than 1000... </h1>")
        
    context={
        'form':form,
        'age':age,
        'total_months':total_months,
        'noof_year':noof_year,
        'total_investment':total_investment,
        'amount':amount,
        'rate_of_interest':rate_of_interest,
        'total_returns':total_returns,
        'interest_amount':interest_amount,
        'senior_citizen':senior_citizen,
       
    }   
    return render(request,"interest.html",context)

def adin(request):
    return render(request,"adin.html")

def register(request):
    registred= False
    if request.method == "POST":
        form=userform(request.POST)
        profile=userprofile(request.POST,request.FILES)
        if form.is_valid() and profile.is_valid():
           user= form.save()
           user.set_password(user.password)
           user.save()


           profileform = profile.save(commit=False)
           profileform.user=user
           profileform.save()
           registred=True
        
    else:
        form=userform()
        profile=userprofile()
        
    context={
        "form":form,
        "profile":profile,
        "registred":registred,
    }

    return render(request,"register.html",context)

def user_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect("home")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("please check your creds...")
        
    return render(request,"user_login.html")

def user_logout(request):
    logout(request)
    
    return redirect(user_login)

@login_required(login_url='user_login')
def  User_update(request):
    if request .method == "POST":
        form = UserUpdatedform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserUpdatedform(instance=request.user)

    return render(request,"user_update.html",{'form':form})
    