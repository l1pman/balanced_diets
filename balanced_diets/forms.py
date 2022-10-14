from django import forms
from .models import User

class KcalForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['gender','name','weight','height','age','activity','lactose','vegan','diabetes']
