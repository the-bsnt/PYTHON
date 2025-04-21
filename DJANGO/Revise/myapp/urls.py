from django.urls import path
from .views import *

app_name = "myapp"
urlpatterns = [
    path("", index, name="index"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("search/", search, name="search"),
    # employee register crud operations
    path("employee_dashboard/", employee_dashboard, name="employee_dashboard"),
    path(
        "employee_dashboard/<int:employee_id>/",
        employee_profile,
        name="employee_profile",
    ),
    path(
        "employee_register_form/", employee_register_form, name="employee_register_form"
    ),
    # register new employee
    path("employee_create/", employee_create, name="employee_create"),
    # delete employee
    path(
        "employee_dashboard/<int:employee_id>/delete",
        employee_delete,
        name="employee_delete",
    ),
    path(
        "employee_dashboard/<int:employee_id>/edit",
        employee_edit,
        name="employee_edit",
    ),
    path(
        "employee_dashboard/<int:emp_id>/update",
        employee_update,
        name="employee_update",
    ),
]
