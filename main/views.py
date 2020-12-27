from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, AppointmentForm
from django.contrib.auth import authenticate, login, logout
from .decorators import already_login, doctor_only, allowed_user
from .models import Doctor, Patient, Appointment
from django.contrib.auth.models import User, Group
# Create your views here.

@login_required(login_url='login')
@doctor_only
def homePage(request):
    appoints = request.user.doctor.appointment_set.all().order_by('-date_created')
    total_appoint = appoints.count()
    completed = appoints.filter(status="DONE").count()
    pending = appoints.filter(status="PENDING").count()
    context = {
        'appoints': appoints,
        'total_appoint': total_appoint,
        'completed': completed,
        'pending': pending
    }
    return render(request, 'home.html', context=context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['patient'])
def patientPage(request):
    doctors = Doctor.objects.all()
    appoints = request.user.patient.appointment_set.all().order_by('-date_created')
    total_appoint = appoints.count()
    completed = appoints.filter(status="DONE").count()
    pending = appoints.filter(status="PENDING").count()
    context = {
        'doctors': doctors,
        'appoints': appoints,
        'total_appoint': total_appoint,
        'completed': completed,
        'pending': pending
    }
    return render(request, 'patient.html', context)

@already_login
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account Created Successfully.. for "+ username)
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'register.html', context=context)

@already_login
def loginPage(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is Incorrect!")

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def create_appointment(request, pk):
    # patient_id = request.user.patient.get(id)
    # doctor = Doctor.objects.get(id=pk)
    time_range = range(0, 8)
    time = Appointment.objects.values('time')
    times = []
    for t in time:
        times.append(t['time'])
    print(f'times : {times}')
    print(f'time_range : {time_range}')
    # form = AppointmentForm()
    # if request.method == 'POST':
    #     form = AppointmentForm()
    #     if form.is_valid():
    #         form.save()
    #         messages.info(request, "Appointment has Added Successfully!")
    context = {
        'time_range' : time_range,
        'times': times,
        'begin' : 9
    }
    return render(request, 'create_appoint.html', context)

@login_required(login_url='login')
def update_appointment(request, pk):
    appoint = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appoint)
    if request.method == 'POST':
        form = AppointmentForm(request.POST,instance=appoint)
        if form.is_valid():
            form.save()
            messages.info(request, "Appointment has Added Successfully!")
            return redirect('home')
    context = {'form': form}
    return render(request, 'update_appoint.html', context)

@login_required(login_url='login')
def delete_appointment(request,pk):
    item = Appointment.objects.get(id=pk)
    if request.method =="POST":
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'delete_appoint.html', context)

def prescription(request, pk):
    appoint = Appointment.objects.get(id=pk)
    prescript = appoint.prescription
    context = {'prescript': prescript}
    return render(request, 'prescription.html', context)
