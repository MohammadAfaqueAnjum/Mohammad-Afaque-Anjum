from django.shortcuts import render
from employee.models import Employee

def empformpage(request):
    try:
        if request.method=="POST":
            mname=request.POST.get('empname')
            mqualification=request.POST.get('empqualification')
            mgender=request.POST.get('empgender')
            mage=request.POST.get('empage')
            
            emp=Employee(
                name=mname,
                qualification=mqualification,
                gender=mgender,
                age=mage
            )
            emp.save()
    except:
            pass
    return render(request,'empform.html')