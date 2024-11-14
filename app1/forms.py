from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['name', 'email', 'rating', 'experience']
        widgets = {
            'experience': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'rating': forms.RadioSelect(attrs={'class': 'rating'})  
        }
