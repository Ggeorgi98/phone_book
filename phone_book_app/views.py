from django.utils.timezone import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.paginator import Paginator
from phone_book_app.forms import UserFormModel
from phone_book_app.models import User

# Create your views here.

def user_details(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User not found")
    return render(request, 'phone_book_app/detail.html', {'user': user})

def list_users(request):
    users = User.objects.order_by('-created_date')
    
    paginator = Paginator(users, 2)
    page_number = request.GET.get('page')
    paged_users = paginator.get_page(page_number)
    
    context = {
        'users': paged_users,
    }

    return render(request, 'phone_book_app/users.html', context)

def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form = UserFormModel(request.POST or None, instance=user)
        if form.is_valid():
            form.instance.created_date = user.created_date
            form.save()
            return HttpResponseRedirect(reverse('detail', args=(user.id,)))
    else:        
        form = UserFormModel(instance=user)
        return render(request, 'phone_book_app/update.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user:
        user.delete()
    return redirect("users")

def create_user(request):
    form = UserFormModel(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.created_date = datetime.now()
            user.save()
            return redirect("users")
    else:
        return render(request, "phone_book_app/create.html", {"form": form})