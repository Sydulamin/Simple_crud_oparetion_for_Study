from django.shortcuts import render, redirect
from .models import Human
import os


def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        if image:
            human = Human.objects.create(name=name, email=email, age=age, gender=gender, image=image, address=address)
            human.save()
            print('Done')
        else:
            human = Human.objects.create(name=name, email=email, age=age, gender=gender, address=address)
            human.save()
            print('Done')
    return render(request, 'Nafi_temp/index.html')


def all_prof(request):
    human = Human.objects.all()
    return render(request, 'Nafi_temp/all_profile.html', locals())


def delete_prof(request, id):
    prof = Human.objects.get(id=id)
    if prof.image != 'def.jpg':
        os.remove(prof.image.path)
    prof.delete()
    return redirect('all_prof')


def Update(request, id):
    prof = Human.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        if image:
            prof.name = name
            prof.email = email
            prof.age = age
            prof.gender = gender
            if prof.image != 'def.jpg':
                os.remove(prof.image.path)
            prof.image = image
            prof.address = address
            prof.save()
            return redirect('all_prof')
        else:
            prof.name = name
            prof.email = email
            prof.age = age
            prof.gender = gender
            prof.address = address
            prof.save()
            return redirect('all_prof')

    return render(request, 'Nafi_temp/update.html', locals())


def test(request):
    return 0
