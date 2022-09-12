from django.urls import path
from phone_book_app import views, views_contacts, views_phones

urlpatterns = [
    path("", views.list_users, name="users"),
    path("users/<int:user_id>", views.user_details, name="detail"),
    path("users/delete/<int:user_id>", views.delete_user, name="delete"),
    path("users/update/<int:user_id>", views.update_user, name="update"),
    path("create/", views.create_user, name="create"),
    path("contacts/<int:user_id>", views_contacts.list_user_contacts, name="list_contacts"),
    path("contacts/details/<int:pk>", views_contacts.contact_details, name="contact_details"),
    path("contacts/delete/<int:pk>", views_contacts.delete_contact, name="delete_contact"),
    # path("users/update/<int:user_id>", views.update_user, name="update"),
    path("contacts/create/<int:user_id>", views_contacts.create_contact, name="create_contact"),
    path("add-phone/<int:contact_id>", views_phones.add_phone, name="add_phone"),
    path("phones/delete/<int:pk>", views_phones.delete_phone, name="delete_phone"),
    path("phones/update/<int:phone_id>", views_phones.update_phone_number, name="update_phone"),
]