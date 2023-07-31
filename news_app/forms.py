from django import forms
from news_app.models import Contact

class ContactForm(forms.ModelForm):
     class Meta:
          model = Contact
          fields= "__all__"