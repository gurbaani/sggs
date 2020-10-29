from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from pages import forms


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'pages/contact.html'
    form_class = forms.ContactForm
    success_message = 'Message sent successfully!'
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
