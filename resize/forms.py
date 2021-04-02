
from django import forms
   
from .models import Upload
   

class UploadForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Upload
        fields = "__all__"