from django.urls import path
from .views import login_view,home,admin_dashboard,add_student,student_dashboard,logout_view,view_all_students,update_student,student_profile,student_attendance,studentfeedetails,studentsubjects,studentresults

urlpatterns = [
    path("",home,name="home"),
    path('login/',login_view,name="login"),
    path("admin_dashboard",admin_dashboard,name="admin_dashboard"),
    path("add_student/",add_student,name="add_student"),
    path("student_dashboard/",student_dashboard,name="student_dashboard"),
    path("viewallstudentlist/",view_all_students,name="viewallstudentlist"),
    path("update_student/<int:id>/",update_student,name="update_student"),
    path("studentprofile/<int:id>/",student_profile,name="studentprofile"),
    # path("studentattandance/",student_attandance,name="studentattandance"),
    path('studentattendance/',student_attendance, name='studentattendance'),
    path("studentfeedetails",studentfeedetails,name="studentfeedetails"),
    path("studentsubject/",studentsubjects,name="studentsubject"),
    path("studentresults/",studentresults,name="studentresults"),
    # path('student/attendance/<int:id>/', views.student_attendance_admin, name='student_attendance_admin'),
    path("logout/",logout_view,name="logout"),
]

