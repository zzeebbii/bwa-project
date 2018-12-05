from django import forms


class DiscussionForm(forms.Form):
    topic = forms.CharField(required=True, max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : 'form-control'}))