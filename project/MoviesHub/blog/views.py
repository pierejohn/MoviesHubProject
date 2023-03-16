from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import post,Category,Comment
from .forms import postForm,updateForm,CommentForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model=post
    template_name="home.html"
    ordering=["-timeCreation"]
    # ordering=['-id']

class ArticlrDetailView(DetailView):
    model=post
    template_name="articleDetail.html"
   

    

class addPostView(CreateView):
    model=post
    form_class=postForm
    template_name="add_posts.html"
class updatePost(UpdateView):
    model=post
    template_name="updatepost.html"
    form_class=updateForm
    success_url =reverse_lazy("community")

    # fields=['title','title_tag','body']
class deletePost(DeleteView):
    model=post
    template_name="deletePost.html" 
    success_url =reverse_lazy("community")

def movies(request):
    return render(request,"movies.html",{})

class community(ListView):
    model=post
    template_name="community.html"
    ordering=["-timeCreation"]
    
    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(community,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

      
    # ordering=['-id']
def Categoryview(request,cat):
    Category_posts = post.objects.filter(category=cat.replace('-',' '))
    
    
    return render(request,'categores.html',{'cat':cat.replace('-',' '),'Category_posts':Category_posts})

class addCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name="add_Comment.html"
    
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url ="/article/{post_id}"
    # fields="__all__"

