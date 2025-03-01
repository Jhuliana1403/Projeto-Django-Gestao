from django import forms
from django.contrib.auth.models import User

class AdminCreationForm(forms.ModelForm):
    nome_completo = forms.CharField(max_length=150, required=True, label="Nome Completo")
    email = forms.EmailField(required=True, label="E-mail")
    senha = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")

    class Meta:
        model = User
        fields = ['nome_completo', 'email', 'senha']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Usa o e-mail como username
        user.set_password(self.cleaned_data['senha'])  # Criptografa a senha
        user.is_staff = True  # Define como administrador
        if commit:
            user.save()
        return user
