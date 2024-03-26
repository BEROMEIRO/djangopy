from django.shortcuts import render

from contact.models import Contact


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:15]

    context = {
        'contacts': contacts,
    }

    print(contacts.query)

    return render(
        request,
        'contact/index.html',
        context
    )
