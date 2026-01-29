# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    STATE_CHOICES = [
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CG','Chhattisgarh'),
    ('GA','Goa'),
    ('GJ','Gujarat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JH','Jharkhand'),
    ('KA','Karnataka'),
    ('KL','Kerala'),
    ('MP','Madhya Pradesh'),
    ('MH','Maharashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland'),
    ('OD','Odisha'),
    ('PB','Punjab'),
    ('RJ','Rajasthan'),
    ('SK','Sikkim'),
    ('TN','Tamil Nadu'),
    ('TS','Telangana'),
    ('TR','Tripura'),
    ('UK','Uttarakhand'),
    ('UP','Uttar Pradesh'),
    ('WB','West Bengal'),
    ('DL','Delhi'),
]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    gender = models.CharField(
    max_length=10,
    choices=[('male','Male'),('female','Female'),('other','Other')])
    profile_photo = models.ImageField(upload_to='students/', null=True, blank=True)
    state = models.CharField(max_length=50,choices=STATE_CHOICES,default='MP')
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active_student = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username



# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")

#     # Personal Info
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     gender = models.CharField(
#         max_length=10,
#         choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
#     )
#     date_of_birth = models.DateField(null=True, blank=True)

#     # Professional Info
#     employee_id = models.CharField(max_length=20, unique=True)
#     qualification = models.CharField(max_length=150)
#     experience_years = models.PositiveIntegerField(default=0)
#     department = models.CharField(max_length=100)
#     subjects = models.CharField(max_length=255, help_text="Comma separated subjects")

#     # Contact Info
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()

#     # Address
#     address = models.TextField()

#     # Profile
#     profile_photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

#     # Status
#     is_active = models.BooleanField(default=True)
#     joined_on = models.DateField(auto_now_add=True)

#     # Meta
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.employee_id})"



# from django.db import models
# from django.contrib.auth.models import User

# # ----------------------------
# # Course Model
# # ----------------------------
# class Course(models.Model):
#     course_code = models.CharField(max_length=20, unique=True)
#     course_name = models.CharField(max_length=150)
#     description = models.TextField(blank=True)
#     duration_months = models.PositiveIntegerField()
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.course_name} ({self.course_code})"


# # ----------------------------
# # Student Profile Model
# # ----------------------------
# class StudentProfile(models.Model):
#     STATE_CHOICES = [
#         ('AP','Andhra Pradesh'),('AR','Arunachal Pradesh'),('AS','Assam'),('BR','Bihar'),
#         ('CG','Chhattisgarh'),('GA','Goa'),('GJ','Gujarat'),('HR','Haryana'),('HP','Himachal Pradesh'),
#         ('JH','Jharkhand'),('KA','Karnataka'),('KL','Kerala'),('MP','Madhya Pradesh'),('MH','Maharashtra'),
#         ('MN','Manipur'),('ML','Meghalaya'),('MZ','Mizoram'),('NL','Nagaland'),('OD','Odisha'),('PB','Punjab'),
#         ('RJ','Rajasthan'),('SK','Sikkim'),('TN','Tamil Nadu'),('TS','Telangana'),('TR','Tripura'),
#         ('UK','Uttarakhand'),('UP','Uttar Pradesh'),('WB','West Bengal'),('DL','Delhi'),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.IntegerField(default=18)
#     phone = models.CharField(max_length=15)

#     # Course relationship (Many students -> One course)
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="students"
#     )

#     gender = models.CharField(
#         max_length=10,
#         choices=[('male','Male'),('female','Female'),('other','Other')]
#     )

#     profile_photo = models.ImageField(upload_to='students/', null=True, blank=True)
#     state = models.CharField(max_length=50, choices=STATE_CHOICES, default='MP')
#     city = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_active_student = models.BooleanField(default=True)

#     def __str__(self):
#         return self.user.username


# # ----------------------------
# # Teacher Model
# # ----------------------------
# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")

#     # Personal Info
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     gender = models.CharField(
#         max_length=10,
#         choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
#     )
#     date_of_birth = models.DateField(null=True, blank=True)

#     # Professional Info
#     employee_id = models.CharField(max_length=20, unique=True)
#     qualification = models.CharField(max_length=150)
#     experience_years = models.PositiveIntegerField(default=0)
#     department = models.CharField(max_length=100)

#     # Teacher can teach multiple courses
#     courses = models.ManyToManyField(
#         Course,
#         related_name="teachers",
#         blank=True
#     )

#     subjects = models.CharField(max_length=255, help_text="Comma separated subjects")

#     # Contact Info
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()

#     # Address
#     address = models.TextField()

#     # Profile
#     profile_photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

#     # Status
#     is_active = models.BooleanField(default=True)
#     joined_on = models.DateField(auto_now_add=True)

#     # Meta
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.employee_id})"
