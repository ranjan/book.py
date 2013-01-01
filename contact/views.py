from django.shortcuts import render_to_response
from demoapp.contact.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def thanks(request):
  return render_to_response('thanks.html')

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      send_mail(
        cd['subject'],
        cd['message'],
        cd.get('email', 'noreply@example.com'),
        ['siteowner@example.com'],
      )
      return HttpResponseRedirect('/contact/thanks/')
  else:
    form = ContactForm()
  return render_to_response('contact_form.html', {'form': form})