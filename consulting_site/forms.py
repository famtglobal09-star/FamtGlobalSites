from django import forms
from website.models import CallbackRequest

class CallbackForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['name', 'email', 'phone', 'service', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows':3, 'placeholder':'Tell us about your requirement'}),
            'name': forms.TextInput(attrs={'placeholder':'John Doe'}),
            'email': forms.EmailInput(attrs={'placeholder':'john@email.com'}),
            'phone': forms.TextInput(attrs={'placeholder':'+1 9876543210'}),
        }