from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterUser
from django.contrib import messages

# Create your views here.
def admin_view(request):
    users=User.objects.all()
    return render(request,'admin.html',{'users':users})


def user_detail_page(request,id):
    user=User.objects.get(id=id)
    return render(request,'detail.html',{'user':user})


def delete_user(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('admin_view')


def user_creation(request):
    form=RegisterUser()
    if request.method =="POST":
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user created successfully!!")
            return redirect("admin_view")
        else:
            messages.error(request,form.errors)
            return redirect("register")
    return render(request,"register.html",{'form':form})
