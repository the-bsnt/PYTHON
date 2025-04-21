from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import *
from django.urls import reverse


def index(request):

    return HttpResponse("hwllo this is index from app")


# def index(request):
#     question_list = Question.objects.all()
#     return render(request, "index.html", {"questions": question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "myapp/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST.get("choice"))
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "myapp/detail.html",
            {
                "question": question,
                "error_message": "Either You didn't select a choice",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("myapp:results", args=(question_id,)))


def search(request):
    q = request.GET.get("q")
    print(request.GET)
    print(q)
    return HttpResponse("this is WSGI request")


# employee;
def employee_dashboard(request):
    employees = Employee.objects.all()
    # if not employees.exists():
    #     raise Http404(f"No employees are register.")
    context = {
        "employees": employees,
    }
    return render(request, "myapp/employee_dashboard.html", context)


def employee_register_form(request):
    return render(request, "myapp/employee_register_form.html")


def employee_create(request):
    if request.method == "POST":
        e_name = request.POST.get("e_name")
        e_email = request.POST.get("e_email")
        d_name = request.POST.get("d_name")
        department, created = Department.objects.get_or_create(d_name=d_name)
        new_emp = Employee(e_name=e_name, e_email=e_email, d_id_id=department.d_id)
        new_emp.save()

        return HttpResponseRedirect(reverse("myapp2:employee_dashboard"))


def employee_profile(request, employee_id):
    emp = get_object_or_404(Employee, e_id=employee_id)
    return render(request, "myapp/employee_profile.html", {"employee": emp})


def employee_delete(request, employee_id):
    emp = get_object_or_404(Employee, e_id=employee_id)
    depart = emp.d_id
    emp.delete()
    if not Employee.objects.filter(d_id=depart).exists():
        depart.delete()
    return HttpResponseRedirect(reverse("myapp:employee_dashboard"))


def employee_edit(request, employee_id):
    emp = get_object_or_404(Employee, e_id=employee_id)
    return render(request, "myapp/employee_edit.html", {"employee": emp})


def employee_update(request, emp_id):
    if request.method == "POST":
        emp = get_object_or_404(Employee, e_id=emp_id)
        name = request.POST.get("e_name", "")
        email = request.POST.get("e_email", "")
        d_name = request.POST.get("d_name", "")
        if name:
            emp.e_name = name
        if email:
            emp.e_email = email
        if d_name:
            depart, create = Department.objects.get_or_create(d_name=d_name)
            emp.d_id = depart
        emp.save()
        return HttpResponseRedirect(reverse("myapp:employee_dashboard"))
