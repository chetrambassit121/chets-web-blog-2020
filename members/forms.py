# we created this file in the members project because we actually want to edit forms like the register / login forms !!! 

# from django.contrib.auth.forms import UserCreationForm                  #  required to edit authentication forms like register / login 
# from django.contrib.auth.models import User                             #  this code will help check credentials of a user ... etc ... 
# from django import forms 											    # this code will help with the forms we want to create

# class SignUpForm(UserCreationForm):                                                                                 # creating class with user creation form as arguement 
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              # CV email bound to the forms method .. forms method using the Email Field class
# 																													# widgets bound to forms method .. forms using emailinput class ..
# 																													# attrs (attributes) accessing the following bootstrap dictionary class : form-control .. 
# 																													# now the email field will be displayed in bootstrap form 
# 																												# this is the same concept as our theblog/forms.py  
# 	first_name = forms.CharField(max_length=100)                                            	                        # first name same concept as email 
# 	last_name = forms.CharField(max_length=100)                                                                     # last name same concept as firs tname 


# 	class Meta:                                                                                         # created class Meta
# 		model = User                                                                                    # model method bound to the User class
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')             # fields bound to the following strings .. each string will be a field  for the user in our registration form




# NOW we have created our own unique register form and we will go back to our members/views.oy file to change   



























# from django.contrib.auth.forms import UserCreationForm                  
# from django.contrib.auth.models import User                             
# from django import forms 											    
# class SignUpForm(UserCreationForm):                                                                                 
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
# 	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))         # EDITED  ... same concept as email and theblog/forms.py                                                            
# 	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))          # EDITED ... same conccept as email and theblog.forms.py                                                          


# 	class Meta:                                                                                         
# 		model = User                                                                                    
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  



# NOW all three of our created feilds are in bootstrap form similar to theblog/forms.py 
# we still have to change the django feilds (username, password, reenter password) to bottstrap form    

























# from django.contrib.auth.forms import UserCreationForm                  
# from django.contrib.auth.models import User                             
# from django import forms 											    
# class SignUpForm(UserCreationForm):                                                                                 
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
# 	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
# 	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))          

# 	class Meta:                                                                                         
# 		model = User                                                                                    
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  


# 	def __init__(self, *args, **kwargs):                                     # ADDED .. defining the init method with the following paramemters ..
# 		super(SignUpForm, self).__init__(*args, **kwargs)                    # ADDED .. using the super method which allows us access methods from the Signupform class ..
# 																			 # we then will use init method with the args kwrags arguemnts and pass them through to Signupform !!  

# 		self.fields['username'].widget.attrs['class'] = 'form-control'       # ADDED .. this format is how we change the django default feilds into bootstrap styled 
# 		self.fields['password1'].widget.attrs['class'] = 'form-control'      # ADDED ..
# 		self.fields['password2'].widget.attrs['class'] = 'form-control'      # ADDED ..




# now our regisration form is styled with the new fields and the existing django feilds 
































# from django.contrib.auth.forms import UserCreationForm, UserChangeForm                                    # ADDED ... userchangeform from members/views.py            
# from django.contrib.auth.models import User                             
# from django import forms 				


# class SignUpForm(UserCreationForm):                                                                                 
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
# 	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
# 	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))          

# 	class Meta:                                                                                         
# 		model = User                                                                                    
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  


# 	def __init__(self, *args, **kwargs):                                    
# 		super(SignUpForm, self).__init__(*args, **kwargs)                    
# 		self.fields['username'].widget.attrs['class'] = 'form-control'       
# 		self.fields['password1'].widget.attrs['class'] = 'form-control'      
# 		self.fields['password2'].widget.attrs['class'] = 'form-control'      


# class EditProfileForm(UserChangeForm):                                  										# ADDED .. creating the editprofileclass ... using userchangeform from members/views.py 
# 																												# so we are creating our wn unque edit profile form
# 																												# same concept we did with our signupform 
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
# 	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
# 	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})) 
# 	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                              																						
# 	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
# 	is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))       # Checkboxinput will literally be a checkbox ... so the 'class' we have to find will be 'form-check' 
# 	is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))          
# 	is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))          
# 	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))          

         

# 	class Meta:                                                                                         
# 		model = User                                                                                    
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')      # ADDED .. the new variables from above to our fields variable   


	
# NOW we have our own created edit profile form with the follwoing fields 






















from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm                           # ADDED ... the passwordchangeform                                           
from django.contrib.auth.models import User                             
from django import forms 
from theblog.models import Profile                                                                                    # ADDED ... importing Profile 				


class SignUpForm(UserCreationForm):                                                                                 
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))          

	class Meta:                                                                                         
		model = User                                                                                    
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  


	def __init__(self, *args, **kwargs):                                    
		super(SignUpForm, self).__init__(*args, **kwargs)                    
		self.fields['username'].widget.attrs['class'] = 'form-control'       
		self.fields['password1'].widget.attrs['class'] = 'form-control'      
		self.fields['password2'].widget.attrs['class'] = 'form-control'      


class EditProfileForm(UserChangeForm):                                  										
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))                              																						
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})) 
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                              																						
	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))                                                                    
	is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))       
	is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))          
	is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))          
	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))          

         

	class Meta:                                                                                         
		model = User                                                                                    
		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')      



class PasswordChangingForm(PasswordChangeForm):                                                                                          # ADDED ... the following class ... with the following passwordchangeform                                                                              
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))                      # old password variable using passwordinput and type:password      																						
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))     #  newpassword1 variable using passwordinput and type:password                                                             
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))      # newpassword2 variable using passwordinput and type:password    

	class Meta:                                                                                                                                      
		model = User                                                                                     
		fields = ('old_password', 'new_password1', 'new_password2')                                                                        # the three fields for pur passwordchangeform 


class ProfilePageForm(forms.ModelForm):		
	class Meta:																							# ADDED .. form for user to create a profile page ! 
		model = Profile 
		fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
		widgets = {
			'bio': forms.Textarea(attrs={'class': 'form-control'}),                                                                    
			# 'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'website_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
			'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),                                                                    
		}


# AFTER creatig profilepageform import it to members/views.py

