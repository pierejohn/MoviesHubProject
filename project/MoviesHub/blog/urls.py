

from django.urls import path
from . import views
from .views import HomeView,ArticlrDetailView,addPostView,updatePost,deletePost,movies,community,Categoryview,addCommentView

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticlrDetailView.as_view(),name="articleDetail"),
    path('add_Post/',addPostView.as_view(),name="add_Post"),
    path('article/edit/<int:pk>',updatePost.as_view(),name="updatePost"),
    path('article/<int:pk>/delete',deletePost.as_view(),name="deletePost"),
    path('movies',views.movies,name="movies"),
    path('community/',community.as_view(),name="community"),
    path('category/<str:cat>',Categoryview,name="category"),
    path('article/<int:pk>/Comment',addCommentView.as_view(),name="Comment"),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
