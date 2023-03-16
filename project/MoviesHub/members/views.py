from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy,reverse
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView,CreateView,FormView
from blog.models import profile
from django.views import View

class CreateProfilePageView(CreateView):
    model = profile
    template_name = "registration/create_user_profile_page.html"
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# class CreateProfilePageView(CreateView):
# 	model = profile
# 	form_class = ProfilePageForm
# 	template_name = "registration/create_user_profile_page.html"
# 	#fields = '__all__'

# 	def form_valid(self, form):
# 		form.instance.user = self.request.user
# 		return super().form_valid(form)
        
# class ShowProfilePageView(DetailView):
# 	model=profile
# 	template_name="registration/user_profile.html"

# 	def get_context_data(self, *args,**kwargs):
# 			users=profile.objects.all()
# 			context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
# 			page_user=get_object_or_404(profile,id=self.kwargs['pk'])
# 			context['page_user']=page_user
# 			return context
class EditProfilePageView(generic.UpdateView):
	model = profile
	template_name = 'registration/edit_profile_page.html'
	fields = [ 'profile_pic']
	success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
	model = profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		#users = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		
		page_user = get_object_or_404(profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context

class PasswordsChangeView(PasswordChangeView):
	form_class=PasswordChangingForm
	success_url = reverse_lazy('home')    



class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('home')    

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')  

	def get_object(self):
		return self.request.user