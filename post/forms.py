from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

        #custom errors
    def clean_title(self):

        title = self.cleaned_data['title']

        if len(title) < 10:
            raise forms.ValidationError("Title must not less than 10 characters")


        return title
    
    def clean_content(self):
        content = self.cleaned_data['content']

        if len(content) < 10:
            raise forms.ValidationError("content must not less than 10 characters")

        return content
        
