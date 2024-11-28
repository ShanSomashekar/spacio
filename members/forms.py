from django import forms
from .models import Member
from django.contrib.auth.hashers import make_password
import os
import hashlib

class MemberRegistrationForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ['Name', 'ContactNumber', 'Email', 'Address', 'Company', 'GST', 'AadharID', 'Password']

    def save(self, commit=True):
        member = super().save(commit=False)
        salt = os.urandom(16).hex()
        password_hash = hashlib.pbkdf2_hmac('sha256', self.cleaned_data['Password'].encode(), salt.encode(), 100000).hex()
        member.PasswordSalt = salt
        member.PasswordHash = password_hash
        if commit:
            member.save()
        return member
