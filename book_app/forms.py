from django.core import validators
from django import forms
from .models import Review


class UserReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'rating', 'review']
        widgets = {
            'reviewer': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'Please Rate This Book'}),
            # 'review': forms.TextInput()
        }