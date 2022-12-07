from django.shortcuts import render

# todo change the context of the two views
def contact(request):
    contact_info = None
    context = {
        'contact info': contact_info
    }
    return render(request, 'contact.html', context)


def about_me(request):
    about = None
    context = {
        'about me': about
    }
    return render(request, 'about_me.html', context)