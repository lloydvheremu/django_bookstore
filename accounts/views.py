from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomeUserCreationForm


class SignUpPageView(generic.CreateView):
	form_class = CustomeUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

