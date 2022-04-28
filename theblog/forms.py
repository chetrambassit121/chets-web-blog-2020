# in order to style our add_post.html template we need to create a form !!

# from django import forms 						# form class used to buid forms . It describes a form and how it works and appears. I
# from .models import Post

# class PostForm(forms.ModelForm)					# creating class PostForm .. which will inheriet forms. then the ModelForm which is basically Model from models.py
# 	class Meta:								    # A metaclass in Python is a class of a class that defines how a class behaves. this is like a rquirement 
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'body')         # these are the four input fields in Post		

# 		widgets = {                                                   # now we are creating the variable widgets to be a dictionary .. remember dictionarys have keys:value
# 			'title': form.TextInput(attrs={'class': 'form-control'}), # the title field is the key bound to the form class using TextInput ..
# 																	  # title is a TextInput feild so we have use the TextInput class on title ...
# 																	  # attrs is attributes that we want to apply to our title field .. attrs bound to the following key:value .. 
# 																	  # we are accessing the 'class' key and the 'form-control' value .. 'form-control' is a type of CSS !!    
#																	  # 'form control'  
# 		}



# now go to addpost.html to add the div class="form control" to our html file












# from django import forms 						
# from .models import Post

# class PostForm(forms.ModelForm)					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'body')         

# 		widgets = {                                                   
# 			'title': form.TextInput(attrs={'class': 'form-control'}),
# 			'title_tag': form.TextInput(attrs={'class': 'form-control'}),  # ADDED .. title tag is also a TextInput box
# 			'author': form.Select(attrs={'class': 'form-control'}),        # ADDED .. author is a drop selector box therefore we use Select
# 			'body': form.Textarea(attrs={'class': 'form-control'})        # ADDED .. body is a text area box so we use Textarea
# 		}



# now go to views.py to add PostForm and make changes 















# from django import forms 						
# from .models import Post

# class PostForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'body')         

# 		widgets = {                                                   
# 			# 'title': forms.TextInput(attrs={'class': 'form-control'}),      											# we could use the placeholder in the line below 
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	    # ADDED .. 'placeholder' .. will display This is Title Placeholder 
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											# ADDED .. title tag is also a TextInput box
# 			'author': forms.Select(attrs={'class': 'form-control'}),        											# ADDED .. author is a drop selector box therefore we use Select
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											# ADDED .. body is a text area box so we use Textarea
# 		}

















# from django import forms 						
# from .models import Post

# class PostForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'body')         

# 		widgets = {                                                   
# 			# 'title': forms.TextInput(attrs={'class': 'form-control'}),      											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),        											
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}

# class EditForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'author', 'body')         

# 		widgets = {                                                   
# 			# 'title': forms.TextInput(attrs={'class': 'form-control'}),      											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	    
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),        											
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}

# created our own edit form which differs slightly from the post form ... there is no text input box for title tag anymore for the update page 
















# from django import forms 						
# from .models import Post


# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'),]           # ADDED .. CV choices bound to a list with tuples ..
# 																						# these tuples are our category and need to be listed twice for the categorys field to work !!

# class PostForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'category', 'body')             # ADDED category as a field    
# 		widgets = {                                                   
# 			# 'title': forms.TextInput(attrs={'class': 'form-control'}),      											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),
# 			'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),          # ADDED category to the wiggets dictionary, choices=choices to link back to our variable choices			        											
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}


# class EditForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'author', 'body')         
# 		widgets = {                                                   
# 			# 'title': forms.TextInput(attrs={'class': 'form-control'}),      											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	    
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),        											
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}

















# from django import forms 						
# from .models import Post, Category


# # choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'),]    # REMOVED
# choices = Category.objects.all().values_list('name', 'name')                                     # ADDED .. better way to code line above ..
# 																								 # we used 'name' b/c thats the variable from models.py Category Class      


# choice_list = []																				 # CV bound to empty list

# for item in choices:                                                                             # for each item (for each category) in the choices variable .. 																								 
# 	choice_list.append(item)                                									 # the choice_list variable will use append to add each item to its dictionary 
# 																								 # now we can add categorys from localhost:8000/admin/theblog/category and it will ... 
# 																								 # auto add on the website     
 

# class PostForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'category', 'body')                
# 		widgets = {                                                      											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),
# 			'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),          
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}


# class EditForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'author', 'body')         
# 		widgets = {                                                     											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	    
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),        											
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}
















# from django import forms 						
# from .models import Post, Category


# choices = Category.objects.all().values_list('name', 'name')                                    


# choice_list = []																				 

# for item in choices:                                                                             																								 
# 	choice_list.append(item)                                									 
 

# class PostForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'category', 'body')                
# 		widgets = {                                                      											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			# 'author': forms.Select(attrs={'class': 'form-control'}),                                               # REMOVED
# 			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author_field', 'type':'hidden'}),                        # ADDED ... now there will be no drop down menu for the author field
# 																												     # gave this line of coding a value of '' .. 
# 																												     # the value is an empty string which will be replaced by w.e data we want .. this will be determined in the html files  
# 																												     # gave this line of coding an id to help identify it for other pages, type:hidden will hide the field box .. 
# 																												     # now we will go to add_post.html to add some Javascript coding
# 																												     # PURPOSE of this is so the author can ONLY be what we assign it to be .. will determine this in the html files 
# 			'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),          
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}


# class EditForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'author', 'body')         
# 		widgets = {                                                     											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	    
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),        											
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),        											
# 		}
































# from django import forms 						
# from .models import Post, Category


# choices = Category.objects.all().values_list('name', 'name')                                    


# choice_list = []																				 

# for item in choices:                                                                             																								 
# 	choice_list.append(item)                                									 
 

# class PostForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet')                                              # ADDED .. another field called snippet                  
# 		widgets = {                                                      											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author_field', 'type':'hidden'}),                        																								    
# 			'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),          
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),
# 			'snippet': forms.Textarea(attrs={'class': 'form-control'}),      												  # ADDED ... the snippet field 		  											        											
# 		}


# class EditForm(forms.ModelForm):					
# 	class Meta:								    
# 		model = Post
# 		fields = ('title', 'author', 'body', 'snippet')         															  # ADDED ... snippet 
# 		widgets = {                                                     											
# 			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	    
# 			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
# 			'author': forms.Select(attrs={'class': 'form-control'}),        											
# 			'body': forms.Textarea(attrs={'class': 'form-control'}),   
# 			'snippet': forms.Textarea(attrs={'class': 'form-control'}),        											# ADDED ... snippet

# 		}






















from django import forms 						
from .models import Post,  Comment
# Category,

# choices = Category.objects.all().values_list('name', 'name')                                    


# choice_list = []																				 

# for item in choices:                                                                             																								 
	# choice_list.append(item)                                									 
 

class PostForm(forms.ModelForm):					
	class Meta:								    
		model = Post
		fields = ('title', 'title_tag', 'author',  'body', 'snippet', 'header_image')                                      # ADDED ... header image   
		                                                         # 'category',
		widgets = {                                                      											
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author_field', 'type':'hidden'}),                        																								    
			# 'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),          
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),      												  	  											        											
		}


class EditForm(forms.ModelForm):					
	class Meta:								    
		model = Post
		fields = ('title', 'author', 'body', 'snippet')         															 
		widgets = {                                                     											
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),	    
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  											
			'author': forms.Select(attrs={'class': 'form-control'}),        											
			'body': forms.Textarea(attrs={'class': 'form-control'}),   
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),        											

		}

class CommentForm(forms.ModelForm):					                                    # ADDED comment form ... 
	class Meta:								    
		model = Comment
		fields = ('name', 'body')         															 
		widgets = {                                                     																				
			'name': forms.TextInput(attrs={'class': 'form-control'}),        											
			'body': forms.Textarea(attrs={'class': 'form-control'}),      											
		}







