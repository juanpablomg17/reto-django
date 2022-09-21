from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'gestionUser.html', {"users": users})


def registerUser(request):
    name = request.POST['txtName']
    lastname = request.POST['txtLastname']
    age = request.POST['txtAge']
    weight = float(request.POST['txtWeight'].replace(',', '.'))
    hearRate = float(request.POST['txtHearRate'].replace(',', '.'))
    oxygenSaturation = float(request.POST['txtOxygenSaturation'].replace(',', '.'))
    stressLevel = float(request.POST['txtStressLevel'].replace(',', '.'))
    

    user = User.objects.create(
        name=name,
        lastname=lastname,
        age=age,
        weight=weight,
        hearRate=hearRate,
        oxygenSaturation=oxygenSaturation,
        stressLevel=stressLevel
    )
    messages.success(request, '¡Heal metrics registred!')
    return redirect('/')


def editingUser(request, id):
    user = User.objects.get(id=id)
    return render(request, "editingUser.html", {"user": user})


def editUser(request, id):
    name = request.POST['txtName']
    lastname = request.POST['txtLastname']
    age = request.POST['txtAge']
    weight = float(request.POST['txtWeight'].replace(',', '.'))
    hearRate = float(request.POST['txtHearRate'].replace(',', '.'))
    oxygenSaturation = float(request.POST['txtOxygenSaturation'].replace(',', '.'))
    stressLevel = float(request.POST['txtStressLevel'].replace(',', '.'))

    user = User.objects.get(id=id)
    user.name = name
    user.lastname = lastname
    user.age = age
    user.weight = weight
    user.hearRate = hearRate
    user.oxygenSaturation = oxygenSaturation
    user.stressLevel = stressLevel
    user.save()

    messages.success(request, '¡User updated!')

    return redirect('/')


def deleteUser(request, id):
    user = User.objects.get(id=id)
    user.delete()

    messages.success(request, '¡User was deleted!')

    return redirect('/')




