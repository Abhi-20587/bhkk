from django import forms
# 'last_name':forms.NumberInput(attrs={'class':'form-control'}),
from .models import Student
class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("first_name","last_name","instrument")
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'instrument':forms.TextInput(attrs={'class':'form-control'})
        }