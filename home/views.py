from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from home.models import changes, slots, featuredMatches
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,'You have been registered!')
        return redirect("/")
    context={'form': form}
    return render(request, 'registeration.html', context)

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('user')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        Member=authenticate(username=username, email=email, password=password)
        if Member is not None:
            login(request, Member)
            messages.success(request, "You have successfully logged in")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/")

def yourslots(request):
    userId=request.user
    inst=slots.objects.filter(username=userId)
    if inst is not None:
        return render(request, 'yourslots.html', {'inst':inst})
    else:
        messages.warning(request, "No bookings till now")
        return redirect('/')

def bookaslot(request):
    if request.method=='POST':
        username=request.POST['user']
        sport=request.POST['sport']
        ins=slots(username=username, bookedfor=sport)
        ins.save()
    return render(request, 'bookaslot.html')

def featuredmatches(request):
    upcomingmatch=featuredMatches.objects.all()
    return render(request, 'upcomingmatches.html', {'upcomingmatches': upcomingmatch})

def bookedslots(request):
    slot=slots.objects.all()
    return render(request, 'bookedslots.html', {'slot': slot})

def badminton(request):
    change=changes.objects.filter(sportsname='Badminton')
    data={
        'changes':change
    }
    return render(request, 'badminton.html', data)

def basketball(request):
    change=changes.objects.filter(sportsname='Basketball')
    data={
        'changes':change
    }
    return render(request,'basketball.html', data)

def squash(request):
    change=changes.objects.filter(sportsname='Squash')
    data={
        'changes':change
    }
    return render(request, 'squash.html', data)

def volleyball(request):
    change=changes.objects.filter(sportsname='Volleyball')
    data={
        'changes':change
    }
    return render(request, 'volleyball.html', data)