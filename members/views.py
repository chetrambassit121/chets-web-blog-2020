# from django.shortcuts import render
# from django.views import generic 							# generic is for the different types of views like in theblog/views .. different code same concept 
# from django.contrib.auth.forms import UserCreationForm     # djaongo.contrib.auth.forms is for authentication systems like login / register pages .. 
# 															# UserCreationForm is an inbuilt feature from the Django ModelForm class and is used for creating a new user form. 
# from django.urls import reverse_lazy                        # reverse lazy will help us redirect to another url  



# class UserRegisterView(generic.CreateView):                  # this class will be creating a user (member) so we use create view 
# 	form_class = UserCreationForm                            # use djangos form to create a new user (member)
# 	template_name = 'registration/register.html'             # template for our registration 
# 	success_url = reverse_lazy('login')                      # after user registers will be redirected to login 



# !!! THE LOGIN CLASS is not needed because of ... ablog/ablog/pycache/urls.py line path('members/', include('django.contrib.auth.urls')) .. this includes a class already
# !!! THE LOGIN CLASS needs to still be redirected ... go to ablog/ablog/pycache/settings.py ... scroll to the bottom of page and type in the following codings
# LOGIN_REDIRECT_URL = 'home'     and           LOGOUT_REDIRECT_URL = 'home'            ...... this will redirect our login / logout to home 















# from django.shortcuts import render
# from django.views import generic 							
# from django.contrib.auth.forms import UserCreationForm     				
# from django.urls import reverse_lazy                       
# from .forms import SignUpForm   



# class UserRegisterView(generic.CreateView):                  
# 	form_class = SignUpForm                              		# EDITED .. changed to our signupform that we created .. so now the register page will be our own one and not djangos default form                         
# 	template_name = 'registration/register.html'             
# 	success_url = reverse_lazy('login')       



























# from django.shortcuts import render
# from django.views import generic 							
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm                  # ADDED ... UserChangeForm ... this will provde us with a Django form for users to change information .. edit profile form ..   				
# from django.urls import reverse_lazy                       
# from .forms import SignUpForm, EditProfileForm                                          # ADDED ... we added the editprofile form after we created it in members/forms.py ... so now we wont use the djangos Userchangeform  



# class UserRegisterView(generic.CreateView):                  
# 	form_class = SignUpForm                              		                       
# 	template_name = 'registration/register.html'             
# 	success_url = reverse_lazy('login')       


# class UserEditView(generic.UpdateView):                  							# ADDED .. the following class ... with an UpdateView 
# 	# form_class = UserChangeForm                         		                    # REMOVED !! variable form class bound to the Django User change form that we imported ... 
# 	form_class = EditProfileForm													# ADDED .. instead of the djanog form we created our own form .. same concept as above !!      
# 	template_name = 'registration/edit_profile.html'                                # same concept as user register view              
# 	success_url = reverse_lazy('home')                                              # user will be redirected to home page after they edit profile 

# 	def get_object(self):															# ADDED .. defining the following method 
# 		return self.request.user                                                    # we want this method to return the current logged in user ... we use self.request on the user 



# NOW add this view to members/urls.py 






















# from django.shortcuts import render
# from django.views import generic 							
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm                       # EDITED ... ADDED djangos passwordchangeform 
# from django.contrib.auth.views import PasswordChangeView                                                         #  ADDED ... we want to import djangos passwordchangeview              
# from django.urls import reverse_lazy                       
# from .forms import SignUpForm, EditProfileForm                                           


# class PasswordsChangeView(PasswordChangeView):                                    # ADDED ... the following class with the passwordchangeform as a parameter 
# 	form_class = PasswordChangeForm                                               # variable form-class bound to the following form .. 
# 	success_url = reverse_lazy('home')                                            # variable sucess url bound to reverse lazy .. will redirect to the home page basically same concept as below classes !
# 																				  # after user changes password will redirect to home page  


# class UserRegisterView(generic.CreateView):                  
# 	form_class = SignUpForm                              		                       
# 	template_name = 'registration/register.html'             
# 	success_url = reverse_lazy('login')       


# class UserEditView(generic.UpdateView):                  							
	
# 	form_class = EditProfileForm													    
# 	template_name = 'registration/edit_profile.html'                                          
# 	success_url = reverse_lazy('home')                                              

# 	def get_object(self):															
# 		return self.request.user        



# NOW we will go to members/urls.py to edit some coding there                

















# from django.shortcuts import render
# from django.views import generic 							
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm                      
# from django.contrib.auth.views import PasswordChangeView                                                                      
# from django.urls import reverse_lazy                       
# from .forms import SignUpForm, EditProfileForm, PasswordChangingForm           # ADDED ... passwordchangingform                                            


# def password_success(request):                                                  # ADDED .. defining the follwoing method with request as paraM
# 	return render(request, 'registration/password_success.html', {})             # we want this method to do the following .. return the following render template .. contains the context dictionary as well


# class PasswordsChangeView(PasswordChangeView):                                   
# 	# form_class = PasswordChangeForm                                          # REMOVED !  
# 	form_class = PasswordChangingForm 										   # ADDED ... the passwordchaningform is the form we made using bootstrap styling   
# 	success_url = reverse_lazy('password_success')                             # EDITED ... instead of redirecting to home will redirect to password_success.html instead     


# class UserRegisterView(generic.CreateView):                  
# 	form_class = SignUpForm                              		                       
# 	template_name = 'registration/register.html'             
# 	success_url = reverse_lazy('login')       


# class UserEditView(generic.UpdateView):                  							
	
# 	form_class = EditProfileForm													    
# 	template_name = 'registration/edit_profile.html'                                          
# 	success_url = reverse_lazy('home')                                              

# 	def get_object(self):															
# 		return self.request.user     



# NOW we have to create the password_success.html template in the regisration folder !!! 




               



























# from django.shortcuts import render, get_object_or_404													# ADDED .. get boject or 404 for our showprofilepageview .. get context data .. 
# from django.views import generic 							
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm                      
# from django.contrib.auth.views import PasswordChangeView                                                                      
# from django.urls import reverse_lazy                       
# from .forms import SignUpForm, EditProfileForm, PasswordChangingForm      
# from django.views.generic import DetailView        															# ADDED .. importing the detail view 
# from theblog.models import Profile                                       


# def password_success(request):                                                  
# 	return render(request, 'registration/password_success.html', {})             


# class PasswordsChangeView(PasswordChangeView):                                   
# 	# form_class = PasswordChangeForm                                         
# 	form_class = PasswordChangingForm 										    
# 	success_url = reverse_lazy('password_success')                             

# class UserRegisterView(generic.CreateView):                  
# 	form_class = SignUpForm                              		                       
# 	template_name = 'registration/register.html'             
# 	success_url = reverse_lazy('login')       


# class UserEditView(generic.UpdateView):                  							
	
# 	form_class = EditProfileForm													    
# 	template_name = 'registration/edit_profile.html'                                          
# 	success_url = reverse_lazy('home')                                              

# 	def get_object(self):															
# 		return self.request.user     


# class ShowProfilePageView(DetailView):                                  # ADDED ..creating class ... this class is for our users profile !!! 
# 	model = Profile 													# variabl model bound to Profile class from theblog/models.py
# 	template_name = 'registration/user_profile.html'                    # create user_profile.html page in templates directory ... also create the path in urls.py .. !!!!!!!!

# 	def get_context_data(self, *args, **kwargs):                        # ADDED .. defining the following method .. same coding from theblog/views.py from our homeview ...                               
# 		# users = Profile.objects.all()                                  # REMOVED THIS LINE DONT NEED IT # variable users bound to Profile model .. accessing the objects from Profile .. and returning all of them .. so returning the profile of all the users !!
# 		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])    # variable page user bound to the get object 404 method .. method being used on Profile model .. we want the Profiles pk primary key !         					  
# 		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)	   
# 		context['page_user'] = page_user							          
# 		return context




#  NOW ... go back to user_profile.html and add more html code to display the usrs profile !!! 
























from django.shortcuts import render, get_object_or_404													
from django.views import generic 							
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm                      
from django.contrib.auth.views import PasswordChangeView                                                                      
from django.urls import reverse_lazy                       
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm     # ADDED ... ProfilePageform       
from django.views.generic import DetailView, CreateView        															 
from theblog.models import Profile                                                  # ADDED ... Profile class                                      


def password_success(request):                                                  
	return render(request, 'registration/password_success.html', {})             


class PasswordsChangeView(PasswordChangeView):                                   
	# form_class = PasswordChangeForm                                         
	form_class = PasswordChangingForm 										    
	success_url = reverse_lazy('password_success')                             

class UserRegisterView(generic.CreateView):                  
	form_class = SignUpForm                              		                       
	template_name = 'registration/register.html'             
	success_url = reverse_lazy('login')       


class UserEditView(generic.UpdateView):                  							
	
	form_class = EditProfileForm													    
	template_name = 'registration/edit_profile.html'                                          
	success_url = reverse_lazy('home')                                              

	def get_object(self):															
		return self.request.user     


class ShowProfilePageView(DetailView):                                  
	model = Profile 													
	template_name = 'registration/user_profile.html'                    

	def get_context_data(self, *args, **kwargs):                                                    
		
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])             					  
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)	   
		context['page_user'] = page_user							          
		return context


class EditProfilePageView(generic.UpdateView):                                      # ADDED ... created class .... using same parameter as usereditview since we want user to be able to edit there profile
	model = Profile                                                                                                             
	template_name = 'registration/edit_profile_page.html'
	fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']    # all the fields user can edit 
	success_url = reverse_lazy('home')                                                                                 # after editing will redirect to home page 


class CreateProfilePageView(CreateView):											# ADDED ... the following class ... for user to create a profile page 
	model = Profile 
	form_class = ProfilePageForm                                                    # created our own profile form for user to fill out 
	template_name = 'registration/create_user_profile_page.html'
	# fields = '__all__'																# using all for fields ... so the fields in our create_profile_page link will be in django form 

	def form_valid(self, form):                                                     # ADDED ... the following method .. this method will basically do the following 
																					# when a new user registers .. they have no profile page at the moment .. so when they so create a profile page 
																					# that profile page will be saved under that same current new user ! 
		form.instance.user = self.request.user 
		return super().form_valid(form)


