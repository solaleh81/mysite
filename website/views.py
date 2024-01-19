from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from .forms import NameForm, ContactForm, NewsLetterForm


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/contact.html', context={'form': form})

def news_letter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:home')
        else:
            return HttpResponse('form is invalid')
    else:
        return redirect('website:home')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('done')
        else:
            return HttpResponse("Not valid")


    form = ContactForm()
    return render(request, 'test.html', context={'form': form})
