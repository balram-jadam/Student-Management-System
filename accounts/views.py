# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import StudentRegistrationForm
from django.contrib.auth.models import User
from .models import StudentProfile
from .forms import StudentUpdateForm
import math


# Create your views here.

def home(request):
    return render(request,'home.html')


def login_view(request):
    return render(request,'login.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # redirect based on role (optional)
            if user.is_staff:
                return redirect('/admin_dashboard')
            else:
                return redirect('/student_dashboard')

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def admin_dashboard(request):
    total_students = StudentProfile.objects.count()
    return render(request,"admin_dashboard.html", {
        'total_students': total_students})



def add_student(request):

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, request.FILES)

        if form.is_valid():

            # -------- Get data manually from POST --------
            first_name = request.POST.get('first_name')
            last_name  = request.POST.get('last_name')
            email      = request.POST.get('email')
            password   = request.POST.get('password')

            phone   = request.POST.get('phone')
            course  = request.POST.get('course')
            gender  = request.POST.get('gender')
            state   = request.POST.get('state')
            city    = request.POST.get('city')

            profile_photo = request.FILES.get('profile_photo')

            # -------- Create User --------
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            # -------- Create Student Profile --------
            StudentProfile.objects.create(
                user=user,
                phone=phone,
                course=course,
                gender=gender,
                state=state,
                city=city,
                profile_photo=profile_photo
            )

            messages.success(request, "Student added successfully!")
            return redirect('viewallstudentlist')

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = StudentRegistrationForm()

   
    return render(request, 'add_student.html', {'form': form})

# Student Dashboard

def student_dashboard(request):
    return render(request,'student_dashboard.html')


def view_all_students(request):
    students = StudentProfile.objects.select_related('user').all()
    return render(request, 'view_all_students.html', {'students': students})

# def update_student(request):
#     return render(request,'update_student.html')


def update_student(request, id):
    profile = get_object_or_404(StudentProfile, id=id)
    user = profile.user

    if request.method == "POST":
        form = StudentUpdateForm(
            request.POST,
            request.FILES,
            instance=profile,
            user=user
        )

        if form.is_valid():
            # Update User table
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.username = form.cleaned_data.get('email')
            user.save()

            # Update StudentProfile table
            form.save()

            return redirect('student_dashboard')

    else:
        form = StudentUpdateForm(instance=profile, user=user)

    return render(request, 'update_student.html', {
        'profile': profile,
        'form': form
    })
    
    
    
def student_profile(request, id):
    profile = get_object_or_404(StudentProfile, id=id)

    return render(request, 'student_profile.html', {'profile': profile})

    

# def student_attandance(request):
#     return render(request,'student_attandance.html')




# @login_required
def student_attendance(request):
    profile = get_object_or_404(StudentProfile, user=request.user)

    semester_name = "Semester 2"

    # Fixed semester data
    total_classes = 120
    attended_classes = 78
    missed_classes = 20

    classes_done = attended_classes + missed_classes
    remaining_classes = max(total_classes - classes_done, 0)

    attendance_percent = round((attended_classes / total_classes) * 100, 2)

    required_for_75 = math.ceil(0.75 * total_classes)
    max_possible_attendance = attended_classes + remaining_classes

    if max_possible_attendance >= required_for_75:
        can_reach_75 = True
        required_classes = max(required_for_75 - attended_classes, 0)
    else:
        can_reach_75 = False
        required_classes = 0

    context = {
        'profile': profile,
        'semester_name': semester_name,
        'total_classes': total_classes,
        'attended_classes': attended_classes,
        'missed_classes': missed_classes,
        'remaining_classes': remaining_classes,
        'attendance_percent': attendance_percent,
        'required_classes': required_classes,
        'can_reach_75': can_reach_75,
    }

    return render(request, 'student_attendance.html', context)


def studentfeedetails(request):
    return render(request,'student_fee_details.html')

def studentsubjects(request):
    return render(request,'student_subjects.html')

def studentresults(request):
    return render(request,'student_results.html')


#   Logout
def logout_view(request):
    logout(request)
    return redirect("login")