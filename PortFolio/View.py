from django.shortcuts import HttpResponse,HttpResponseRedirect,render,redirect
from django.db import models
from ADDmodel.models import monelN,skill,project


def Home(request):


    aa=monelN.objects.all()
    
    page={
        'item':aa
    }
    print(aa.__dict__)
    
    return render(request,'Home.html',page)

# def AddLanguage(request):
#     try:
#         if request.method=='POST':
#             name=request.POST['name']
#             Photo=request.FILES['Photo']
#             subTitle=request.POST['subTitle']
#             print(name,Photo,subTitle,'---')
#     except:
#         pass
    
#     return render(request,'AddLanguage.html')

def SKILL(request):
    Modeldata=skill.objects.all()
    SkillDatabase={
        "skill":Modeldata
    }

    return render(request,'SKILL.html',SkillDatabase)


def WORKEXPERIENCE(request):
    return render(request,'WORKEXPERIENCE.html')

def EDUCATION(request):
    return render(request,'EDUCATION.html')

def STRENGTH(request):
    return render(request,'STRENGTH.html')

def PROJECTS(request):
    Project=project.objects.all()
    projectdata={
        'data':Project
    }

    return render(request,'PROJECTS.html',projectdata)


def HOBBY(request):
    return render(request,'HOBBY.html')
