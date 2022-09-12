from django import forms
from phone_book_app.models import User, Contact, Phone

class UserFormModel(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password",)   # NOTE: the trailing comma is required

class ContactFormModel(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", )   # NOTE: the trailing comma is required

class PhoneFormModel(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ("PhoneNumber", )   # NOTE: the trailing comma is required