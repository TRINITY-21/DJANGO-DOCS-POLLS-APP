from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        listing_id = request.POST['listing_id']
        listing_id = request.POST['listing_id']

    # if user has inquiry

    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(
            listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error(
                request, "You have already made an inquiry for this listing")
            return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)

        contact.save()

        # EMAIL
        send_mail(
            'Property Listing Inquiry',
            'There has been an   inquiry for ' + listing +
            '. Sign into the admin panel for more info',
            'agyemanjoseph@gmail.com',
            [realtor_email, 'agyemanjoseph12@gmail.com'],
            fail_silently=False
        )

        messages.success(
            request, "Your request has been submitted, will get back to you")
        return redirect('/listings/'+listing_id)
