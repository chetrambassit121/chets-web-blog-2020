# from django.db import models
# from django.contrib.auth.models import User             # this is the User that we created

# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    # if we create posts under the chetram bassit user .. 
# 																  # then we want to be able to delete (CASCADE) all posts if we delete the chetram bassit user account .. this line will do that  
# 	body = models.TextField()

# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)










# from django.db import models
# from django.contrib.auth.models import User 



# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255, default="title_tag")  # ADDED .. a title tag with a default .. default will display title_tag if we dont make our own title tag as a user           
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()

# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)
















# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse							#ADDED .. will redirect from one view to another 


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()

# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     # ADDED created the following method
# 		return reverse('article-detail', args=(str(self.id)))     # return the following .. using the reverse function .. to return article-detail url 
# 																 # .. arguments are a string that is the self.id .. so if we create a new post it will get a new unique id 


# # test out the add_post url .. fill out the post form click post and this will redirect you to the artcle-detail urls 


















# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse							


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()

# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         # EDITED ... will now just redirect to home after we create a new post 















# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                                            # ADDED .. datetime modeule importing datetime class for dates and times etc ... 						


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()
# 	post_date = models.DateField(auto_now_add=True)                    # ADDED .. CV post data bound to the django models .. models using DateField .. Datefield using autonowadd ..
# 																	    # ... which will auto add the current date that the post was created 

# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         
















# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                                            					


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')               # ADDED ... category for our posts .. defualt category will be coding 

# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   # ADDED a class called Category .. this will better make the catergories better for the users 
# 	name = models.CharField(max_length=255)                                     # name of category .. 

# 	def __str__(self):                                                          
# 		return self.name                                                        # returning the name of the categroy 

# 	def get_absolute_url(self):								                    # if we need to redirect 
# 		return reverse('home')         


















# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                                            					


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')            
# 	likes = models.ManyToManyField(User, related_name='blog_posts')  		# ADDED .. CV likes .. bound to .. models using the manytomanyfield on our User ..
# 																		    # related name is a requirement .. its bound to .. the string we created 'blog_posts' .. this is needed 
# 																		    # EX: a post can have MANY likes and a user can like MANY posts so we use this type of field for this purpose .. 
																		    									
																		   
# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   
# 	name = models.CharField(max_length=255)                                     
# 	def __str__(self):                                                          
# 		return self.name                                                        

# 	def get_absolute_url(self):								                    
# 		return reverse('home')      



























# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                                            					


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')            
# 	likes = models.ManyToManyField(User, related_name='blog_posts')
	  		


# 	def total_likes(self):                                                  # ADDED .. defining our total_likes method self as argument 
# 		return self.likes.count()                                           # we want to return the likes with its count() .. 
# 																		    # count will return the total amount of our (variable we created) likes

																		    									
																		   
# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   
# 	name = models.CharField(max_length=255)                                     
# 	def __str__(self):                                                          
# 		return self.name                                                        

# 	def get_absolute_url(self):								                    
# 		return reverse('home')         


























# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                          
             					


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)    														  
# 	body = models.TextField()
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')            
# 	likes = models.ManyToManyField(User, related_name='blog_posts')
# 	dislikes = models.ManyToManyField(User, related_name='dislike_blog_posts')  		


# 	def total_likes(self):                                                  # ADDED .. defining our total_likes method self as argument 
# 		return self.likes.count()                                           # we want to return the likes with its count() .. 
# 																		    # count will return the total amount of our (variable we created) likes

# 	def total_dislikes(self):                                               # ADDED .. defining our total_dislikes method self as argument .. same concept as total likes .. added this myself 
# 		return self.dislikes.count()        
																		    									
																		   
# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   
# 	name = models.CharField(max_length=255)                                     
# 	def __str__(self):                                                          
# 		return self.name                                                        

# 	def get_absolute_url(self):								                    
# 		return reverse('home')         





























# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                          
# from ckeditor.fields import RichTextField                                               # ADDED ... Rich text is the text that is formatted with common formatting options,
# 																						# go to gitbash terminal .. pip install ckeditor .. now we can use it in our coding
# 																						# such as bold, italics, images, URLs that are unavailable with plain text.   ..
# 																						# in this case we want to add a editor on our body for the add_posts template              					


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)
# 	body = RichTextField(blank=True, null=True)    										# ADDED .. we want our body to be the richtextfield that we imported ..  blank / null requirement												  
# 	# body = models.TextField()                                                         # REMOVE the old body we created 
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')            
# 	likes = models.ManyToManyField(User, related_name='blog_posts')
# 	dislikes = models.ManyToManyField(User, related_name='dislike_blog_posts')  		


# 	def total_likes(self):                                                 
# 		return self.likes.count()                                           

# 	def total_dislikes(self):                                                
# 		return self.dislikes.count()        
																		    									
																		   
# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   
# 	name = models.CharField(max_length=255)                                     
# 	def __str__(self):                                                          
# 		return self.name                                                        

# 	def get_absolute_url(self):								                    
# 		return reverse('home')         




# since we made a change to our models file go to git bash terminal to push the changes  !!!!!!! 
# we also have to go to ablog/setting.py file to add the ckeditor !!!!!!!!!!!
# we also have to add code in our add_posts.html file to display the editor we want to add to our body 

























# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                          
# from ckeditor.fields import RichTextField                                               				


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)
# 	body = RichTextField(blank=True, null=True)    																						  
# 	# body = models.TextField()                                                         
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')    
# 	# snippet = models.CharField(max_length=255, default='Click above to see Blog Post...')         # ADDED .. CV snippet .. bound to the following code .. now we will add this varible to home.html
# 	snippet = models.CharField(max_length=255)                                                      # REMOVED the line above .. 
# 																								    # ADDED same line minus the default we dont want a default only needed the first time to push thru terminal                
# 	likes = models.ManyToManyField(User, related_name='blog_posts')
# 	dislikes = models.ManyToManyField(User, related_name='dislike_blog_posts')  		


# 	def total_likes(self):                                                 
# 		return self.likes.count()                                           

# 	def total_dislikes(self):                                                
# 		return self.dislikes.count()        
																		    									
																		   
# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   
# 	name = models.CharField(max_length=255)                                     
# 	def __str__(self):                                                          
# 		return self.name                                                        

# 	def get_absolute_url(self):								                    
# 		return reverse('home')        



# NOW we can add this snippet variable to our home.html file 































# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                          
# from ckeditor.fields import RichTextField                                               				


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	header_image = models.ImageField(null=True, blank=True, upload_to='images/')      # ADDED ... CV header image bound to the django models .. models using ImageField class ..
# 																					  # this class will assist with uploading images on a post ... 
# 																					  # null / blank are True because some posts may not want images !!
# 																					  # upload to the images directory (this will be automatically created ! ) 
																					   

# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)
# 	body = RichTextField(blank=True, null=True)    																						                                            
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')    
# 	snippet = models.CharField(max_length=255)                                                     																			     
# 	likes = models.ManyToManyField(User, related_name='blog_posts')
# 	dislikes = models.ManyToManyField(User, related_name='dislike_blog_posts')  		


# 	def total_likes(self):                                                 
# 		return self.likes.count()                                           

# 	def total_dislikes(self):                                                
# 		return self.dislikes.count()        
																		    									
																		   
# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   
# 	name = models.CharField(max_length=255)                                     
# 	def __str__(self):                                                          
# 		return self.name                                                        

# 	def get_absolute_url(self):								                    
# 		return reverse('home')        



# NOW go to git bash terminal and pip install Pillow .. Pillow is for image uploadings etc ...
# ALSO add another field for images in our form.py !!
# ALSO add html coding to add_post.html to display the image section 
# ALSO went to ablog/setting.py to create a variable called media_url 
























# from django.db import models
# from django.contrib.auth.models import User             
# from django.urls import reverse	
# from datetime import datetime                          
# from ckeditor.fields import RichTextField                                               				


# class Post(models.Model):
# 	title = models.CharField(max_length=255)
# 	header_image = models.ImageField(null=True, blank=True, upload_to='images/')      																				   
# 	title_tag = models.CharField(max_length=255)                     
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)
# 	body = RichTextField(blank=True, null=True)    																						                                            
# 	post_date = models.DateField(auto_now_add=True)                    
# 	category = models.CharField(max_length=255, default='coding')    
# 	snippet = models.CharField(max_length=255)                                                     																			     
# 	likes = models.ManyToManyField(User, related_name='blog_posts')
# 	dislikes = models.ManyToManyField(User, related_name='dislike_blog_posts')  		


# 	def total_likes(self):                                                 
# 		return self.likes.count()                                           

# 	def total_dislikes(self):                                                
# 		return self.dislikes.count()        
																		    									
																		   
# 	def __str__(self):
# 		return self.title + ' | ' + str(self.author)

# 	def get_absolute_url(self):								     
# 		return reverse('home')         


# class Category(models.Model):                                                   
# 	name = models.CharField(max_length=255)                                     
# 	def __str__(self):                                                          
# 		return self.name                                                        

# 	def get_absolute_url(self):								                    
# 		return reverse('home')  


# class Profile(models.Model):							                        # ADDED ... created new class Profile .. same parameters as previous classes in this file 
# 	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)      # variable user bound to our models class .. models class using onetoonefield .. this field is used for 1 to 1 relationships
# 																				# in this case the Profile will have a relationship with User .. 
# 																				# null is True because we already have exisitng users ... 
# 																				# on delete CASCADE which means when user delete profile all info gets deleted too 

# 	bio = models.TextField()                                                    # ADDED .. CV variable bio bound to models class .. models class using TextField .. we want our users bio to be  text field 
# 	profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')  # ADDED .. CV bound to the following code .. same concept as our header image ... 


# 																						# ADDED ... the 5 url variables ... 
# 	website_url = models.CharField(max_length=255, null=True, blank=True) 
# 	facebook_url = models.CharField(max_length=255, null=True, blank=True)          
# 	twitter_url = models.CharField(max_length=255, null=True, blank=True)          
# 	instagram_url = models.CharField(max_length=255, null=True, blank=True)          
# 	pinterest_url = models.CharField(max_length=255, null=True, blank=True)          



# 	def __str__(self):															# ADDED .. defining the str method ..
# 		return str(self.user)                                                   # we want to return the self.user 


# 	def get_absolute_url(self):	                                               # ADDED ... want to redirect to home page 							                    
# 		return reverse('home')  



# SOO the class Profile is the Users actual profile ... they will be able to fill out fields .. bio , profile pic , the 5 urls 
# FOR NOW we can go to localhost8000:/admin and fill out these fields 
# WE CAN ALSO add these fields to be displayed in our article detail.html file ... 
# NOW go to theblog/admin.py to add this new class !! 




































from django.db import models
from django.contrib.auth.models import User             
from django.urls import reverse	
from datetime import datetime                          
from ckeditor.fields import RichTextField                                               				


class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to='images/')      																				   
	title_tag = models.CharField(max_length=255)                     
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)    																						                                            
	post_date = models.DateField(auto_now_add=True)                    
	category = models.CharField(max_length=255, default='coding')    
	snippet = models.CharField(max_length=255)                                                     																			     
	likes = models.ManyToManyField(User, related_name='blog_posts')
	dislikes = models.ManyToManyField(User, related_name='dislike_blog_posts')  		


	def total_likes(self):                                                 
		return self.likes.count()                                           

	def total_dislikes(self):                                                
		return self.dislikes.count()        
																		    									
																		   
	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):								     
		return reverse('home')         


class Category(models.Model):                                                   
	name = models.CharField(max_length=255)                                     
	def __str__(self):                                                          
		return self.name                                                        

	def get_absolute_url(self):								                    
		return reverse('home')  


class Profile(models.Model):							                        
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)     
	bio = models.TextField()                                                    
	profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')  																					
	website_url = models.CharField(max_length=255, null=True, blank=True) 
	facebook_url = models.CharField(max_length=255, null=True, blank=True)          
	twitter_url = models.CharField(max_length=255, null=True, blank=True)          
	instagram_url = models.CharField(max_length=255, null=True, blank=True)          
	pinterest_url = models.CharField(max_length=255, null=True, blank=True)          

	def __str__(self):															
		return str(self.user)                                                   

	def get_absolute_url(self):	                                               			                    
		return reverse('home')  


class Comment(models.Model):												                   # ADDED ... class called Comment ... 
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)               # same concept as author variable from our Post class in this file 
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)                                           # this will display the title of the post being commented on along with the name of the user who posted a comment


# push these changes in git bash terminals 	
# add this class to theblog/admins 														 





