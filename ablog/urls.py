"""ablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('theblog.urls')),                           # ADDED ... this path is for all the urls inside theblog app
#     path('members/', include('django.contrib.auth.urls')),       # ADDED ... this path .. django.contrib.auth.urls will "handle" urls in member app ..
#                                                                  # login page is automatically included so we dont have to make a url for login in our members project !! 
#     path('members/', include('members.urls'))                    # ADDED ... this path added same time as previous members path .. this path is a requirements for our members app 
# ]












from django.contrib import admin
from django.urls import path, include
from django.conf import settings                                # ADDED .. imported ablog/settings.py 
from django.conf.urls.static import static                      # ADDED .. importing static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),                           
    path('members/', include('django.contrib.auth.urls')),       
    path('members/', include('members.urls'))                   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ADDED..this is saying the urlspatterns are bound to the list [] plus (+) static() .. static accessing settings.py which contains the MEDIA_URL
                                                                  # the docuemnt_root bound to the settings.py which contains thw MEDIA ROOT variable 
                                                                  # so now our media is connected to the our website !! 