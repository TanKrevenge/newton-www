# -*- coding: utf-8 -*-
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

class PasswordForm(forms.Form):
    password = forms.PasswordInput()
    repassword = forms.PasswordInput()


