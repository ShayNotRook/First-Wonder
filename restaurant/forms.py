from django import forms
from .models import UserComments, Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComments
        fields = ('comment', 'helpful')
        
        
class RatingForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    
    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rating', widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Rating
        fields = ['rating']