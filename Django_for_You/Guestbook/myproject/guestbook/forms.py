#Forms are going to be somewhat similar to models
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}))
    #here is the difference between a form and a model
