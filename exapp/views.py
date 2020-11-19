from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import Quote, User


def index (request):
    return render(request, 'log_reg.html')

def register(request):
    if request.method =="POST":
        errors=User.objects.validate_user(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        user_pw=request.POST['password']
        hash_pw=bcrypt.hashpw(user_pw.encode(),bcrypt.gensalt()).decode()
    
        log_user=User.objects.create(
            f_name=request.POST['f_name'],
            l_name=request.POST['l_name'],
            email=request.POST['email'],
            password=hash_pw,
        )

        request.session['user_id']=log_user.id
        request.session['user_name']=f"{log_user.f_name} {log_user.l_name}"
        return redirect('/success')
    return redirect('/')

def login (request):
    if request.method=='POST':
        log_user=User.objects.filter(email=request.POST['email'])
        if log_user:
            log_user=log_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['user_id']=log_user.id
                request.session['user_name']=f"{log_user.f_name} {log_user.l_name}"
                return redirect('/success')
            else:
                messages.error(request, "Password was incorrect.")
        else:
            messages.error(request, "Email was not found.") 
    return redirect('/')

def success(request):
    if "user_id" not in request.session:
        return redirect('/')
    context={
        'all_quotes':Quote.objects.all()
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/') 

def create_quote(request):
    if request.method=="POST":
        error=Quote.objects.valadator_quote(request.POST)
        if error:
            messages.error(request, error)
            return redirect('/success')
        Quote.objects.create(
            author=request.POST['author'],
            quote=request.POST['quote'], 
            poster=User.objects.get(id=request.session["user_id"]))
        return redirect('/success')
    return redirect('/')

def get_user(request, user_id):
    context={
        'edit_user':User.objects.get(id=user_id)
    }
    return render(request, 'edit_user.html', context)


def edit_user(request, user_id):
    c=User.objects.get(id=user_id)
    c.f_name=request.GET['f_name']
    c.save()

    c.l_name=request.GET['l_name']
    c.save()

    c.email=request.GET['email']
    c.save()

    context={
        'log_user':User.objects.get(id=user_id),
        'all_quotes':Quote.objects.all()
    }
    return render(request,'dashboard.html', context)

def user_page(request, user_id):
    context={
        'quoter':User.objects.get(id=user_id)
    }
    return render(request, 'user_page.html', context)

def delete_quote(request, post_id):
    Quote.objects.get(id=post_id).delete()
    return redirect('/success')

    