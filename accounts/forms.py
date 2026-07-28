from django import forms
from django.contrib.auth.models import User

style_class="p-2 rounded-xl border border-gray-200 w-full outline-0 mb-3 bg-white"
class UserForm(forms.ModelForm):
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

        

        widgets = {
            'first_name':forms.TextInput(attrs={
                'placeholder':'first name',
                'class':style_class,
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'last name',
                'class':style_class,
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'email',
                'class':style_class,
            }),
            'username':forms.TextInput(attrs={
                'placeholder':'username',
                'class':style_class,
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder':'password',
                'class':style_class,
            })

        }

        
    
    def save(self,commit=True):
        user = User.objects.create_user(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password'],
        )
        return user