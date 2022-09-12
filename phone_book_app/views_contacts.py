from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from phone_book_app.forms import ContactFormModel
from phone_book_app.models import Contact

# Create your views here.

def contact_details(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/details.html', {'contact': contact})

def list_user_contacts(request, user_id):
    if user_id:
        contacts = Contact.objects.filter(user=user_id).order_by('-first_name').order_by('-last_name')[:5]
    else:
        contacts = Contact.objects.order_by('-first_name').order_by('-last_name')[:5]
    
    context = {
            'contacts': contacts,
            'user_id': user_id
        }
    return render(request, 'contacts/contacts.html', context)

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    user_id = contact.user_id
    if contact:
        contact.delete()
    return redirect("list_contacts", user_id)

def create_contact(request, user_id):
    form = ContactFormModel(request.POST or None)
    form.user_id = user_id
    if request.method == "POST":
        if form.is_valid():
            contact = Contact(user_id = user_id)
            contact.first_name = form["first_name"].data
            contact.last_name = form["last_name"].data
            contact.save()
            return HttpResponseRedirect(reverse('list_contacts', args=(user_id,)))
    else:
        return render(request, "contacts/create.html", {"form": form})

def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactFormModel(request.POST or None, instance=contact)
        if form.is_valid():
            form.instance.user_id = contact.user_id
            form.save()
            return HttpResponseRedirect(reverse('contact_details', args=(contact.id,)))
    else:        
        form = ContactFormModel(instance=contact)
        return render(request, 'contacts/update.html', {'form': form})