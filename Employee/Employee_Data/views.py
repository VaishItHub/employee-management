from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# View to list all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# View to create a new employee
@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect after saving
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

# View to update an existing employee
@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect after updating
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

# View to delete an employee
@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')

# View to register a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log the user in after registering
            return redirect('employee_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# View to log in the user
def user_login(request):  # Renamed to avoid conflict with Django's built-in login
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # Log the user in
            return redirect('employee_list')  # Redirect to employee list after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# View to log out the user
def user_logout(request):  # Renamed to avoid conflict with Django's built-in logout
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout
