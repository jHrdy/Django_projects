from django import forms

from . import models

class AuthorForm(forms.ModelForm):
    error_css_class = "error"

    class Meta:
        model = models.Author
        fields = ["first_name", "last_name", ]  # and other fields...

    def clean(self):
        # call the method from the parent class
        super().clean()

        # do some additional validation
        if " " in self.cleaned_data["first_name"]:
            raise forms.ValidationError("First name cannot contain spaces")

class NotesForm(forms.ModelForm):
    error_css_class = "error"

    class Meta:
        model = models.Notes
        fields = "__all__"
        widgets = {
            'about': forms.TextInput(attrs={'placeholder': 'Describe your notes'}),
        }
