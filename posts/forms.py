from django import forms
from .models import Post

#django form#
#class PostForm(forms.Form):
 #   title = forms.CharField()
  #  description =forms.CharField()
   # image = forms.ImageField()
    #slug = forms.CharField()


class PostModelForm(forms.ModelForm):
    class Meta:
        model= Post
        ##puedes usar fields o exclude
        fields = ['title','description', 'image','slug']