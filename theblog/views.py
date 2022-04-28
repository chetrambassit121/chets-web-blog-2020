# from django.shortcuts import render


# def home(request):                                           # basic home request 
# 	return render(request, 'home.html', {})















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView   # ADDED .. these are two different generic views that we will use 
# 														# ListView is A page representing a list of objects. 
# 														# While this view is executing, self. object_list will contain the list of objects 
# 														# (usually, but not necessarily a queryset) that the view is operating upon. 
# 														# DetailView is more specific ... used to present the detail of a single object ...

# from .models import Post								# ADDED .. importing our Post class




# # def home(request):                                           
# # 	return render(request, 'home.html', {})

# class HomeView(ListView):                              # ADDED .. creating a class called homeview .. type of generic view will be the ListView
# 														 # codemy uses classes to create views which return templates ... slighty different than using VSC with jose from udemy
# 	model = Post										 
# 	template_name = 'home.html'                          
# 														 # lines 34-36 return home.html just like 31-32 ... coded differently
















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView   									 
# from .models import Post								


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                     

# class ArticleDetailView(DetailView):                     # ADDED the following class 
# 	model = Post
# 	template_name = 'article_details.html'



# #  now go to urls to add the new view  
















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView     # ADDED CreateView .. we created the add_post.html file which will be a CreateView type   									 
# from .models import Post								


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                     

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										# ADDED the following class for our add_post.html 
# 	model = Post 
# 	template_name = 'add_post.html'
# 	fields = "__all__"												# created variable fields bound to the attribute all .. this will display all the Post input fields that user fills out
# 	# fields = ('title', 'body')                                    # variable feilds bound to the followings strings ... title and body are the variables from our Post class in models.py
# 																	# can use either one of the fields depends on what we want returned 
















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView     									 
# from .models import Post	
# from .forms import PostForm 											# ADDED the PostForm class 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                     

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            # ADDED form class variable bound to the PostForm class 
# 	template_name = 'add_post.html'
# 	# fields = "__all__"											 # REMOVED this line not needed anymore since we added the form class line 	














# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView          # ADDED .. the UpdateView ... this was added after we created the update_post.html file     									 
# from .models import Post	
# from .forms import PostForm 											 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                     

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					# ADDED the following class .. same concept as Addpostview                    
# 	model = Post
# 	form_class = PostForm 										# we are going to use the same PostForm from forms.py to style the updatepost.html file
# 															    # we WILL make another form more spefic for the update post page .. check out forms.py
# 	template_name = 'update_post.html'
	





















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView              									 
# from .models import Post	
# from .forms import PostForm, EditForm                 # ADDED the edit form ...
# from django.urls import reverse_lazy                  # ADDED for our deletepostview class   											 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                     
# 	# ordering = ['-id']                             # ADDED .. ordering bound to the - id .. which means our posts will de displayed from newest id to oldest id ..        
# 	ordering = ['-post_date']                        # ADDED ... will order from newest post date to oldest post date !! we will use this order post_date instead of the id 

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        # edited .. added our EditForm 
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              # this is needed for use to be able to delete a post ... w/o this line we will get an error 




















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                # ADDED ... the Category class from models.py	
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy                  										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                     
# 	# ordering = ['-id']                               
# 	ordering = ['-post_date']                        

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						# ADDED the following class .. addcategory has the same createview as addpost .. now we will create the template ! 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									# ADDED .. instead of a class Codemy wants to use a function .. both classes and functions can be used together ! 
# 																	# the purpose of this function is to return all posts under a single category 
# 																	# request required to return a html file .. cats is for our catergorys in urls.py  
# 	category_posts = Post.objects.filter(category=cats)             # CV bound to the Post.object (post is an object) from models.py .. using filter to get a specfic data .. 
# 																	# the data we want to filter will be a category  
# 	return render(request, 'categories.html',                       # return the category.html template with render ..
# 	{'cats': cats.title(), 'category_posts': category_posts})      	# {} is the contents of the dictionary which will be cats (categories) and the category posts  
# 																	# .title will turn the category into a title format  !     
# 																	# now we will create the category.html file in remplates 
















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy                  										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                     
# 	# ordering = ['-id']                               
# 	ordering = ['-post_date']                        

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))       # EDITED ... ADDED replace() .. this will replace blank spaces ' ' with a - on our link !             
# 	return render(request, 'categories.html',                       
# 	{'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   # EDITED .. ADDED .replace('-', ' ') to cats.title .. 
# 																				  # this will now remove the - from the white spaces in our <h2>{{ cats }}</h2> title from categories.html       	
# 																	
























# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy                  										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                                                  
# 	ordering = ['-post_date']   

# 	def get_context_data(self, *args, **kwargs):                               # ADDED .. the following function w/ the three arguemnts 
# 																			   # self is needed since the class Categorys in models.oy uses it too 
# 																			   # *args collects the positional arguments that are not explicitly defined and store them in a tuple. 
# 																			   # **kwargs does the same as *args but for keyword arguments.
# 																			   # these arguemnts needed to return the categories 
# 		cat_menu = Category.objects.all()                					   # CV bound to the Category class in models.py .. objects in the Category class .. 
# 																			   # access all() the objects in the category class 
# 																			   # so we want to access all the categories that we have  
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)	   # CV context bound to the following ... this line will basically use super to access Homeview, self ..
# 																			   # then acess our function get_context_data with the two arguements	
# 		context['cat_menu'] = cat_menu								           # now the context variable which contains a dictionary named cat_menu can be bound to the cat_menu variable
#         return context                                                       # now we will return the context variable which will contain all our categories !  
#       																	   # when we are on the home url .. and click on categories on the nav bar .. all existing categores will appear in list form
#       																	   # the categories button only available right now when we are on home url ....    
       																		    

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))                
# 	return render(request, 'categories.html',                       
# 	{'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   

















# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy                  										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                                                  
# 	ordering = ['-post_date']   

# 	def get_context_data(self, *args, **kwargs):                               
# 		cat_menu = Category.objects.all()                					   
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)	   
# 		context['cat_menu'] = cat_menu								           
# 		return context                                                         


# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))                
# 	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   

# def CategoryListView(request):                                 # ADDED .. a new view for categories .. this view is intended to contain all the different categories thats exist																							
# 	cat_menu_list = Category.objects.all()                     # CV cat_menu_list .. same concept as cat_menu variable .. return all the categories  
# 	return render(request, 'category_list.html',             # we want to return he following html file (which will display the categoires .. need to create this) 
# 	{'cat_menu_list': cat_menu_list})                         # the dictionary {} cat_menu_list is the key and also the value ..     

























# from django.shortcuts import render, get_object_or_404                                         # ADDED, get_object_or_404 .. this will get an object for us if it doesnt exsit 404 error will return 
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy, reverse                                           # ADDED .. reverse 
# from django.http import HttpResponseRedirect                                            # ADDED .. used for returning htmls ..                										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                                                  
# 	ordering = ['-post_date']   

# 	def get_context_data(self, *args, **kwargs):                               
# 		cat_menu = Category.objects.all()                					   
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)	   
# 		context['cat_menu'] = cat_menu	

# 		stuff = get_object_or_404(Post, id=self.kwargs['pk'])                         #
# 		total_likes = 
# 		context['total_likes'] = total_likes                                          # ADDED .. using context variable to find our 'total_likes' .. bound to the total_likes variable that we created  

# 		return context                                                         


# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))                
# 	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   

# def CategoryListView(request):                                																						
# 	cat_menu_list = Category.objects.all()                     
# 	return render(request, 'category_list.html',             
# 	{'cat_menu_list': cat_menu_list}) 

# def LikeView(request, pk):						                        	# ADDED .. defiing the LikeView with request and pk as arguments 
# 	post = get_object_or_404(Post, id=request.POST.get('post_id'))          # CV post .. bound to .. the follwoing django function .. this function being used on Post from models.py
# 																			# id bound to request.POST.get("") ... this will get the 'post_id' from the like button in article_detail.html 
# 	post.likes.add(request.user)											# this will allow our database to know the following user liked the following post !! 
# 	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))  # return the following .. the httpresponseredirt method .. using reverse .. on our article detial html page
# 																			# we want to find the primary key which that post belongs to .. so we will be returning that post that was liked basically
# 																			# OVERALL when a user likes a post we want to return that same page back to the user   	





















# from django.shortcuts import render, get_object_or_404                                         # ADDED, get_object_or_404 .. this will get an object for us if it doesnt exsit 404 error will return 
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy, reverse                                           # ADDED .. reverse 
# from django.http import HttpResponseRedirect                                            # ADDED .. used for returning htmls ..                										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                                                  
# 	ordering = ['-post_date']   

	


# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# 	def get_context_data(self, *args, **kwargs):                               
# 		cat_menu = Category.objects.all()                					   
# 		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)	 
# 		stuff = get_object_or_404(Post, id=self.kwargs['pk'])                         # ADDED .. CV stuff bound to the following method . method accessing Post class .. and the primary key of a specific post 
# 		total_likes = stuff.total_likes() 						                      # ADDED .. CV total_likes bound to the stuff variable .. stuff variable using total_likes method from the Post class  
# 		context['cat_menu'] = cat_menu												  # ADDED .. using context variable to find our 'cat_menu' .. bound to the cat_menu variable that we created
# 		context['total_likes'] = total_likes                                          # ADDED .. using context variable to find our 'total_likes' .. bound to the total_likes variable that we created  
# 		return context                                                         		  # return the variable context .. which will basically bring us back to the same page where the like button is 

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))                
# 	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   

# def CategoryListView(request):                                																						
# 	cat_menu_list = Category.objects.all()                     
# 	return render(request, 'category_list.html',             
# 	{'cat_menu_list': cat_menu_list}) 

# def LikeView(request, pk):						                        	
# 	post = get_object_or_404(Post, id=request.POST.get('post_id'))          
																			
# 	post.likes.add(request.user)											
# 	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))  
















# from django.shortcuts import render, get_object_or_404                                         
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy, reverse                                           
# from django.http import HttpResponseRedirect                                                         										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                                                  
# 	ordering = ['-post_date']   

	


# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# 	def get_context_data(self, *args, **kwargs):                               
# 		cat_menu = Category.objects.all()                					   
# 		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)	 

# 		stuff = get_object_or_404(Post, id=self.kwargs['pk'])                         
# 		total_likes = stuff.total_likes()
		

# 		liked = False                                                                      # ADDED ..CV liked bound to False .. we do this so the users like is False for now 
# 		if stuff.likes.filter(id=self.request.user.id).exists():		                   # ADDED .. same concept as our LikeView .. except using the variable stuff instead of post
# 			liked = True                                                                   # ADDED .. now the liked variable will be True 

# 		context['liked'] = liked                                                           # ADDED .. context finding the liked variable 
# 		context['cat_menu'] = cat_menu												 
# 		context['total_likes'] = total_likes  
		                                         
# 		return context                                                         		  

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))                
# 	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   

# def CategoryListView(request):                                																						
# 	cat_menu_list = Category.objects.all()                     
# 	return render(request, 'category_list.html',             
# 	{'cat_menu_list': cat_menu_list}) 

# def LikeView(request, pk):						                        	
# 	post = get_object_or_404(Post, id=request.POST.get('post_id'))          
# 	# liked = False																		# ADDED .. CV likes bound to False statement .. I HAD TO REMOVE this line of coding .. the like / unlike button wasnt switching
# 	if post.likes.filter(id=request.user.id).exists():	                                # ADDED .. the purpose of this line is to see if a logged in user has liked a post .. using exists() to see if this is True 	
# 		post.likes.remove(request.user)												    # ADDED .. so if the previous line does exists .. 
# 																						# which means the user has liked a post .. we will then remove() then like 
# 		liked = False                                                                   # ADDED .. so then liked will be false   
# 	else:                                                                               # ADDED ... else
# 		post.likes.add(request.user)											        # EDITED .. the user is liking a post .. 
# 																						# So we used an if / else statement to see if the user has already liked a post .. 
# 																						#  if they didnt like a post already that means they can only add() a like to that post 
# 		liked = True                                                                    # ADDED .. so then liked will be True in the else statement   
# 	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))  


































# from django.shortcuts import render, get_object_or_404                                         
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
# from .models import Post, Category                
# from .forms import PostForm, EditForm                 
# from django.urls import reverse_lazy, reverse                                           
# from django.http import HttpResponseRedirect                                                         										 		


# class HomeView(ListView):                               
# 	model = Post										 
# 	template_name = 'home.html'                                                  
# 	ordering = ['-post_date']  

# 	def get_context_data(self, *args, **kwargs):                              
# 		cat_menu = Category.objects.all()                					  
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)	   
# 		context['cat_menu'] = cat_menu								          
# 		return context

	
# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# 	def get_context_data(self, *args, **kwargs):                               
# 		cat_menu = Category.objects.all()                					   
# 		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)	 

# 		stuff = get_object_or_404(Post, id=self.kwargs['pk'])                         
# 		total_likes = stuff.total_likes()
# 		total_dislikes = stuff.total_dislikes()                                            # ADDED ... DISLIKES !!!! 

# 		liked = False                                                                      
# 		if stuff.likes.filter(id=self.request.user.id).exists():		                   
# 			liked = True                                                                   

# 		disliked = False                                                                      # ADDED .. basically copying the same format as liked
# 		if stuff.dislikes.filter(id=self.request.user.id).exists():		                   
# 			disliked = True    

# 		context['liked'] = liked                                                           
# 		context['cat_menu'] = cat_menu												 
# 		context['total_likes'] = total_likes  
# 		context['total_dislikes'] = total_dislikes                                          # ADDED
# 		return context                                                         		  

# class AddPostView(CreateView):										
# 	model = Post 
# 	form_class = PostForm                                            
# 	template_name = 'add_post.html'

# class UpdatePostView(UpdateView):           					    
# 	model = Post
# 	form_class = EditForm 	                        
# 	template_name = 'update_post.html'

# class DeletePostView(DeleteView):
# 	model = Post
# 	template_name = 'delete_post.html'
# 	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))                
# 	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   

# def CategoryListView(request):                                																						
# 	cat_menu_list = Category.objects.all()                     
# 	return render(request, 'category_list.html',             
# 	{'cat_menu_list': cat_menu_list}) 

# def LikeView(request, pk):						                                       # EDITED ... created our own coding for a likes button .. 

# 	post = get_object_or_404(Post, id=request.POST.get('post_id'))          
# 	liked = False																		
# 	if post.likes.filter(id=request.user.id).exists():	                               # if the user clicks like button but a like already exists then pass ..
# 		pass
# 	elif post.dislikes.filter(id=request.user.id).exists(): 					       # if the user clicks the like button but a dislike already exist ..                             
# 		post.dislikes.remove(request.user)                                             # we remove that users dislike
# 		post.likes.add(request.user)                                                   # then add a like
# 		liked = True                                                                   # so like is a True statement
# 	else:                                                                              # else .. if user clicks like button while the user doesnt have a existing like or dislike
# 		post.likes.add(request.user)											       # then we will add a like to total likes
# 		liked = True                                                                   # therefore liked is True
# 	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))  

# def DislikeView(request, pk):						                        	      # same concept as our likeview for dislikes  
# 	post = get_object_or_404(Post, id=request.POST.get('post_id'))          
# 	disliked = False																		
# 	if post.dislikes.filter(id=request.user.id).exists():	
# 		pass
# 	elif post.likes.filter(id=request.user.id).exists():
# 		post.likes.remove(request.user)
# 		post.dislikes.add(request.user)
# 		disliked = True  
# 	else:                                									            
# 		post.dislikes.add(request.user)												    
# 		disliked = True                                                                
# 	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))  

























from django.shortcuts import render, get_object_or_404                                         
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView               									 
from .models import Post,  Comment                                                                      # ADDED comment ! Category,                
from .forms import PostForm, EditForm, CommentForm                                                               # ADDED comment form              
from django.urls import reverse_lazy, reverse                                           
from django.http import HttpResponseRedirect                                                         										 		


class HomeView(ListView):                               
	model = Post										 
	template_name = 'home.html'                                                  
	ordering = ['-post_date']  

	def get_context_data(self, *args, **kwargs):                              
		# cat_menu = Category.objects.all()                					  
		context = super(HomeView, self).get_context_data(*args, **kwargs)	   
		# context['cat_menu'] = cat_menu								          
		return context

	
class ArticleDetailView(DetailView):   
	model = Post                 
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):                               
		# cat_menu = Category.objects.all()                					   
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)	 

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])                         
		total_likes = stuff.total_likes()
		total_dislikes = stuff.total_dislikes()                                            # ADDED ... DISLIKES !!!! 

		liked = False                                                                      
		if stuff.likes.filter(id=self.request.user.id).exists():		                   
			liked = True                                                                   

		disliked = False                                                                      # ADDED .. basically copying the same format as liked
		if stuff.dislikes.filter(id=self.request.user.id).exists():		                   
			disliked = True    

		context['liked'] = liked       

		# context['cat_menu'] = cat_menu												 
		context['total_likes'] = total_likes  
		context['total_dislikes'] = total_dislikes                                          # ADDED
		return context               

# class ArticleDetailView(DetailView):                     
# 	model = Post
# 	template_name = 'article_details.html'

# 	def get_context_data(self, *args, **kwargs):                               
# 		cat_menu = Category.objects.all()                					   
# 		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)	 

# 		stuff = get_object_or_404(Post, id=self.kwargs['pk'])                         
# 		total_likes = stuff.total_likes()
		

# 		liked = False                                                                      # ADDED ..CV liked bound to False .. we do this so the users like is False for now 
# 		if stuff.likes.filter(id=self.request.user.id).exists():		                   # ADDED .. same concept as our LikeView .. except using the variable stuff instead of post
# 			liked = True                                                                   # ADDED .. now the liked variable will be True 

# 		context['liked'] = liked                                                           # ADDED .. context finding the liked variable 
# 		context['cat_menu'] = cat_menu												 
# 		context['total_likes'] = total_likes  
		                                         
# 		return context                                                         		                                            		  

class AddPostView(CreateView):										
	model = Post 
	form_class = PostForm                                            
	template_name = 'add_post.html'

class UpdatePostView(UpdateView):           					    
	model = Post
	form_class = EditForm 	                        
	template_name = 'update_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')              

# class AddCategoryView(CreateView):						 				
# 	model = Category 
# 	fields = '__all__'                                           
# 	template_name = 'add_category.html'

# def CategoryView(request, cats):									
# 	category_posts = Post.objects.filter(category=cats.replace('-', ' '))                
# 	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})   

# def CategoryListView(request):                                																						
# 	cat_menu_list = Category.objects.all()                     
# 	return render(request, 'category_list.html',             
# 	{'cat_menu_list': cat_menu_list}) 

def LikeView(request, pk):						                                      
	post = get_object_or_404(Post, id=request.POST.get('post_id'))          
	liked = False																		
	if post.likes.filter(id=request.user.id).exists():	                               
		pass
	elif post.dislikes.filter(id=request.user.id).exists(): 					                                 
		post.dislikes.remove(request.user)                                             
		post.likes.add(request.user)                                                   
		liked = True                                                                   
	else:                                                                             
		post.likes.add(request.user)											       
		liked = True                                                                   
	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))  

def DislikeView(request, pk):						                        	      
	post = get_object_or_404(Post, id=request.POST.get('post_id'))          
	disliked = False																		
	if post.dislikes.filter(id=request.user.id).exists():	
		pass
	elif post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		post.dislikes.add(request.user)
		disliked = True  
	else:                                									            
		post.dislikes.add(request.user)												    
		disliked = True                                                                
	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))  

class AddCommentView(CreateView):                    # ADDED ... comment class !!!										
	model = Comment  
	form_class = CommentForm                                            
	template_name = 'add_comment.html'
	success_url = reverse_lazy('home')
	# fields = '__all__'

	def form_valid(self, form):                         # same concept as the members/views.py createprofilepageview class ... we want to link the post with the users comment 
		form.instance.post_id = self.kwargs['pk'] 
		return super().form_valid(form)


# will import this to urls.py !! 




