from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=100)
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(), max_length=1000)