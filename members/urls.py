# after creating the members app from the git bash terminal ... we had to create this url.py file .. will be the paths for the members app 

# from django.urls import path         
# from .views import UserRegisterView                     

# urlpatterns = [
#    path('register/', UserRegisterView.as_view(), name='register')    
#    # the path for the login page is not needed .. check ablog/ablog/pycache/urls.py .. this line path('members/', include('django.contrib.auth.urls')) includes a path for login already !                                                               
#    ]
















# from django.urls import path         
# from .views import UserRegisterView, UserEditView                           # ADDED the Usereditview                     

# urlpatterns = [
#    path('register/', UserRegisterView.as_view(), name='register'),    
#    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),       # ADDED the usereditview as a path                                                                                                                               
#    ]



# NOW we will ADD this new path as an <a> link into our theblog/templates/base.py nav bar section !! 





















# from django.urls import path         
# from .views import UserRegisterView, UserEditView        
# from django.contrib.auth import views as auth_views                         # ADDED .. we will access authentications views with this import                          

# urlpatterns = [
#    path('register/', UserRegisterView.as_view(), name='register'),    
#    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),     
#    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),             # ADDED .. new path .. this path will use the django password change view as a form 

#    ]




# NOW we will create the change-password.html file in our templates/registration folder AND create a new view in members/view.py !! 

















# from django.urls import path         
# from .views import UserRegisterView, UserEditView, PasswordsChangeView                                               # ADDED the passwords changeview         
# from django.contrib.auth import views as auth_views  


# urlpatterns = [
#    path('register/', UserRegisterView.as_view(), name='register'),    
#    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),     
#    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),             # REMVOED !!!!
#    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),      # ADDED .. added a new password path  ... using our PasswordsChangeView that we created in views.py

#    ]

















# from django.urls import path         
# from .views import UserRegisterView, UserEditView, PasswordsChangeView                                                     
# from django.contrib.auth import views as auth_views  
# from . import views                                                                                  # ADDED .. from . which means everything .. import views ..

# urlpatterns = [
#    path('register/', UserRegisterView.as_view(), name='register'),    
#    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),     
#    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),             
#    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')), 
#    path('password_success/', views.password_success, name='password_success')                                 # ADDED .. another new different path .. this will be a page for user to see the password change was a a success 
#    ]




# NOW we have to create a view for our new path in views.py !!! 
# ALSO have to convert the django change password form into bootstrap style in our forms.py file !!! 





















from django.urls import path         
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView  # ADDED ... showprofilepageview, editprofilepage, createprofilepage                                     
from django.contrib.auth import views as auth_views  
from . import views                                                                                  

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='register'),    
   path('edit_profile/', UserEditView.as_view(), name='edit_profile'),     
   # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),             
   path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')), 
   path('password_success/', views.password_success, name='password_success'),   
   path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),                      # ADDED .. the pth that will disply a users profile 
   path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),            # ADDED .. the pth that will disply the edit users profile form ! 
   path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),               # ADDED .. this path will display the create profile form for a user that doesnt have a profile yet !
   ] 





