from string import Template
from django.views.generic import TemplateView, View
from django.core.mail import EmailMessage
from django.http import JsonResponse

from .forms import ContactForm

HTML_MESSAGE = """
<div id="sendmessage" class="alert alert-{} alert-dismissible fade show" role="alert">
    {} {}.
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
</div>"""


class IndexPageView(TemplateView):
    template_name = 'layouts/default/index.html'


def contact_us(request):
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                first_name = form.cleaned_data['name'].split(' ')[0]
                main_msg = "Name: {0}\nEmail: {1}\nSubject: {2}\nMessage:\n\n{3}".format(
                    form.cleaned_data['name'],
                    form.cleaned_data['email'],
                    form.cleaned_data['subject'],
                    form.cleaned_data['message'])
                email = EmailMessage('Services Inquiry', main_msg, to=[
                    'zach@blackanvil.io'])
                email.send()
                return JsonResponse(
                    {'status': 'OK',
                     'message': HTML_MESSAGE.format('success',
                                                    'Email Successfully Sent! Thank you',
                                                    first_name)
                     })
            except Exception as e:
                return JsonResponse(
                    {'status': 'NOT_OK',
                     'message': HTML_MESSAGE.format(
                         'success', 'Error: Failed to send message. Please try again in 5 min.', '')
                     })
        return JsonResponse(
            {'status': 'NOT_OK',
             'message': 'Invalid Request!'
             })
    return JsonResponse(
        {'status': 'NOT_OK',
         'message': 'Invalid Request!'
         })
