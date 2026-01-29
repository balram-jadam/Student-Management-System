# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class StudentRegistrationForm(forms.Form):
    # User fields
    # username = forms.CharField(max_length=150)
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    

    # # StudentProfile fields
    # phone = forms.CharField(max_length=15)
    # course = forms.CharField(max_length=100)
    # gender = forms.ChoiceField(choices=StudentProfile._meta.get_field('gender').choices)
    # state = forms.ChoiceField(choices=StudentProfile.STATE_CHOICES)
    # city = forms.CharField(max_length=50)
    # profile_photo = forms.ImageField(required=False)
    # password = forms.CharField(widget=forms.PasswordInput)
    
    
    from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile


class StudentRegistrationForm(forms.Form):

    # ----------------
    # User fields
    # ----------------
    
    # username = forms.CharField(
    #     max_length=150,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter username'
    #     })
    # )

    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter first name'
        })
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter last name'
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email address'
        })
    )

    

    # ----------------
    # StudentProfile fields
    # ----------------
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter phone number'
        })
    )

    course = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter course name'
        })
    )

    gender = forms.ChoiceField(
        choices=StudentProfile._meta.get_field('gender').choices,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    state = forms.ChoiceField(
        choices=StudentProfile.STATE_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    city = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city'
        })
    )

    profile_photo = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )
    
    confirm_password = forms.CharField(
    required=True,
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm password'
    })
)


from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class StudentUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = StudentProfile
        fields = ['age', 'phone', 'course', 'gender', 'state', 'city', 'profile_photo']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
