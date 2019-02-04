from django.views.generic import TemplateView, View
from django.core.mail import EmailMessage
from django.http import HttpResponse

from .forms import ContactForm

class IndexPageView(TemplateView):
    template_name = 'layouts/default/index.html'

class ContactFormView(View):

    def post(self, request):
        if request.is_ajax():
            form = ContactForm(request.POST)
            if form.is_valid():
                MSG = "Name: {0}\nEmail: {1}\nSubject: {2}\nMessage:\n\n{3}".format(
                    form.cleaned_data['name'],
                    form.cleaned_data['email'],
                    form.cleaned_data['subject'],
                    form.cleaned_data['message'])
                email = EmailMessage('Penetration Test Inquiry', MSG, to=[
                                     'zach@blackanvil.io'])
                email.send()
                return HttpResponse('OK')
            return HttpResponse('NOTOK')