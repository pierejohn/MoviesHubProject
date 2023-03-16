from django import forms 
from .models import post,Category,Comment

choices=Category.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
    choices_list.append(item)


class postForm(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','auther','category','body','header_image')
        widgets={
            'title':forms.TextInput(attrs={"class":'form-control '}),
            # 'title_tag':forms.TextInput(attrs={"class":'form-control'}),
            'auther':forms.TextInput(attrs={"class":'form-control ','value':'','id':'userpost','type':'hidden'}),
            'category':forms.Select(choices=choices_list , attrs={"class":'form-select'}),
            # 'auther':forms.Select(attrs={"class":'form-control'}),
            'body':forms.Textarea(attrs={"class":'form-control '}),
            # 'title_tag':forms.TextInput(attrs={"class":'form-control'}),

        }
class updateForm(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','body','header_image')
        widgets={
            'title':forms.TextInput(attrs={"class":'form-control'}),
            # 'title_tag':forms.TextInput(attrs={"class":'form-control'}),
            'body':forms.Textarea(attrs={"class":'form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        widgets={
            'name':forms.TextInput(attrs={"class":'form-control ','value':'','id':'userpost',}),
            'body':forms.Textarea(attrs={"class":'form-control'}),

        }