from django import forms
from .models import New_kcal


class KcalForm(forms.ModelForm):
    class Meta:
        model = New_kcal
        fields = ['gender','name','weight','height','age','activity','lactose','vegan','diabetes']
