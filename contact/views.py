from django.shortcuts import render

from django.views import View
from django.contrib import messages
from .forms import ContactForm


class Contact(View):
    """ View to allow users to send messages """

    def get(self, request, *args, **kwargs):
        """Return data"""
        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm()
            }
        )

    def post(self, request, *args, **kwargs):
        """Send data"""
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for your message!')

        else:
            contact_form = ContactForm()
            
        return render(
                request,
                'contact.html',
                {
                    'contact_form': ContactForm()
                }
            )
