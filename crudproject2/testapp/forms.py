from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    def clean_esal(self):
        inputmarks=self.cleaned_data['marks']
        if inputmarks>=35:
            raise forms.ValidationError('The minimum marks shlouls bee >=35')
        return inputmarks
    class Meta:
        model=Student
        fields='__all__'
    