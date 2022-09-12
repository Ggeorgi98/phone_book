from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from phone_book_app.forms import PhoneFormModel
from phone_book_app.models import Phone

def add_phone(request, contact_id):
    form = PhoneFormModel(request.POST or None)
    form.contact_id = contact_id
    if request.method == "POST":
        if form.is_valid():
            phone = Phone(contact_id = contact_id)
            phone.PhoneNumber = form["PhoneNumber"].data
            phone.save()
            return HttpResponseRedirect(reverse('contact_details', args=(contact_id,)))
    else:
        return render(request, "contacts/add_phone.html", {"form": form})

def delete_phone(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    contact_id = phone.contact_id
    if phone:
        phone.delete()
    return redirect("contact_details", contact_id)

def update_phone_number(request, phone_id):
    phone = get_object_or_404(Phone, pk=phone_id)
    if request.method == "POST":
        form = PhoneFormModel(request.POST or None, instance=phone)
        if form.is_valid():
            form.instance.contact_id = phone.contact_id
            form.save()
            return HttpResponseRedirect(reverse('contact_details', args=(phone.contact_id,)))
    else:        
        form = PhoneFormModel(instance=phone)
        return render(request, 'contacts/add_phone.html', {'form': form})