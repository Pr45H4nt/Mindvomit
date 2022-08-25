from django import forms

class addpost(forms.Form):
    Title = forms.CharField(widget = forms.Textarea(attrs={'rows':2,'cols':150}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':17,'cols':150}))

class Feedback(forms.Form):
    Name = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=15)
    Email = forms.EmailField(max_length = 200)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':60}))