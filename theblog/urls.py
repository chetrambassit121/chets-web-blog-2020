# from django.urls import path                              # standard will always need for this url.py file
# from . import views                                       # this is how we import the views.py file ... standard way to import any file 

# urlpatterns = [
#    path('', views.home, name="home"),
# ]















# from django.urls import path
# from .views import HomeView                         # ADDED from views.py import the HomeView class  

# urlpatterns = [
#    path('', HomeView.as_view(), name="home"),       # EDITED ... HomeView using the as_view function .. as_view() requirement for requests / responses
                                                      # this path will be www.ablog.com/home  
# ]
















# from django.urls import path
# from .views import HomeView , ArticleDetailView                 # ADDED .. articledetialview                          

# urlpatterns = [
#    path('', HomeView.as_view(), name='home'),     
#    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),                     # ADDED ... this path will be www.ablog.com/article 
#                                                                                                      # each blog post will have its own unique id which is <int:pk> .. 
#                                                                                                      # int stands for integer .. pk stands for primary key  
#                                                                                                      # similar to uuid.uuid4().hex from VSC with Jose from udemy
#                                                                                                      # ArticleDetailView.as_view(), name='article-detail' same concept as the HomeView                 

# ]



# # now we will go to home page template to add the <a> anchor link 














# from django.urls import path
# from .views import HomeView, ArticleDetailView, AddPostView                                   # ADDED, the AddPostview class from views.py       

# urlpatterns = [
#    path('', HomeView.as_view(), name='home'),     
#    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),   
#    path('add_post/', AddPostView.as_view(), name='add_post'),                                                    # ADDED,  the path for AddPostView
#    ]
#    















# from django.urls import path
# from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView                     # ADDED the updatepostview class / deletepostview class from views                

# urlpatterns = [
#    path('', HomeView.as_view(), name='home'),     
#    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),   
#    path('add_post/', AddPostView.as_view(), name='add_post'),    
#    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),                   # ADDED the following path for our update post  
#    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),                   # ADDED the following path for our delete post                                                          
#    ]















# from django.urls import path
# from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView           #ADDED ... addcategoryview and categoryview                          
#                                                                                                                                      # two seperate paths !! 
# urlpatterns = [
#    path('', HomeView.as_view(), name='home'),     
#    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),   
#    path('add_post/', AddPostView.as_view(), name='add_post'),  
#    path('add_category/', AddCategoryView.as_view(), name='add_category'),                                                # ADDED .. this path will allow use to add a category
#    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),                    
#    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'), 
#    path('category/<str:cats>', CategoryView, name='category')                                                        # ADDED .. another path for category so users can view them 
#                                                                                                                      # str:cats stands for the string categorys !   
#                                                                                                                      # go to views to create the CategoryView                                                       
#    ]



# # now we will add the link on base.html for our add category path 















# from django.urls import path
# from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView   # ADDED .. CategoryListView           
# urlpatterns = [
#    path('', HomeView.as_view(), name='home'),     
#    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),   
#    path('add_post/', AddPostView.as_view(), name='add_post'),  
#    path('add_category/', AddCategoryView.as_view(), name='add_category'),                                                
#    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),                    
#    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'), 
#    path('category/<str:cats>', CategoryView, name='category'),    
#    path('category-list/', CategoryListView, name='category-list'),            # ADDED .. our path for the Category List View 
#    ]                                                  













# from django.urls import path
# from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView    # ADDED .. LikeView            
# urlpatterns = [
#    path('', HomeView.as_view(), name='home'),     
#    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),   
#    path('add_post/', AddPostView.as_view(), name='add_post'),  
#    path('add_category/', AddCategoryView.as_view(), name='add_category'),                                                
#    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),                    
#    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'), 
#    path('category/<str:cats>', CategoryView, name='category'),    
#    path('category-list/', CategoryListView, name='category-list'),            
#    path('like/<int:pk>', LikeView, name='like_post'),                                                                # ADDED .. path for like 
   
#    ]                                                  





















from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView,  LikeView, DislikeView, AddCommentView           # ADDED .. DislikeView , addcommentview    
# AddCategoryView, CategoryView, CategoryListView,
urlpatterns = [
   path('', HomeView.as_view(), name='home'),     
   path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),   
   path('add_post/', AddPostView.as_view(), name='add_post'),  
   # path('add_category/', AddCategoryView.as_view(), name='add_category'),                                                
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),                    
   path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'), 
   # path('category/<str:cats>', CategoryView, name='category'),    
   # path('category-list/', CategoryListView, name='category-list'),            
   path('like/<int:pk>', LikeView, name='like_post'),                                                                 
   path('dislike/<int:pk>', DislikeView, name='dislike_post'),                                                       # ADDED .. path for dislike 
   path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),                                     # ADDED .. path for comment .. 

   ]                                                  