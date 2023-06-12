from django.shortcuts import render,HttpResponse,redirect
from .models import employee,testimonial
from .forms import feedbackform
from django.contrib import messages


# Create your views here.

def emp_home(request):
    show = employee.objects.all()
    return render(request,"emp1/base.html",{'show':show})

def add_emp(request):

#Data Fetch
    if request.method == "POST":
        print("yes")

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        # print(emp_name,emp_id,emp_address,emp_department)
#Create model object and set the data
        e=employee()

        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
    

        e.save()

        print("request is coming")
        return redirect("/emp/view-emp/#view")
    return render(request,"emp1/add_emp.html",{})

def view_emp(request):
    show = employee.objects.all()
    return render(request,"emp1/view_emp.html",{'show':show})



def only_view(request):
    show = employee.objects.all()
    return render(request,"emp1/only_view.html",{'show':show})


def delete_emp(request,emp_id):
    e=employee.objects.get(pk=emp_id)
    e.delete()
    return redirect("/emp/view-emp/#view")


def update_emp(request,emp_id):
    e=employee.objects.get(pk=emp_id)
    return render(request,"emp1/update_emp1.html",{'e':e})

def do_update_emp(request,emp_id):
    if request.method == "POST":

        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e=employee.objects.get(pk=emp_id)

        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
    

        e.save()
    return redirect("/emp/view-emp/#view")

def testimonial_fu(request):
    test=testimonial.objects.all()
    return render(request,"emp1/testimonial.html",{'t1':test})

def feedback_emp(request):
    if request.method == "POST":
        return render(request,"emp1/contact.html")
    return render(request,"emp1/contact.html")

def feedback_fu(request):
    if request.method == "POST":
        print("done")
        messages.warning(request,"We will get back soon")
        return render(request,'emp1/base.html')
    else:
        pass
    #     form=feedbackform()
    # return render(request,"emp1/feedback.html",{'form':form})