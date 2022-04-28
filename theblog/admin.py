# from django.contrib import admin
# from .models import Post

# admin.site.register(Post)		# blog posts entries will accessible from the admin area now .. 
# 								# http://localhost:8000/admin/ will have the Post file registered ... but we still need to migrate post ... 













# from django.contrib import admin
# from .models import Post, Category


# admin.site.register(Post)
# admin.site.register(Category)						# ADDED ... we want the localhost:8000/admin to have access to the Category clss we created in theblog/models.py 
# 												    # we can add categorys on the http://localhost:8000/admin/theblog/category/ now !! 











from django.contrib import admin
from .models import Post, Profile, Comment     # ADDED profile and comment 
# Category

admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Profile)               # ADDED ... the Profile class from theblog/models.py
admin.site.register(Comment)               # ADDED ... 
