# main/forms.py

from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Project, Offer, Review, Comment, Message
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

ROLE_CHOICES = [
    ("freelancer", "Фрилансер"),
    ("client", "Заказчик"),
]

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect, label='Выберите роль')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        user.is_freelancer = role == 'freelancer'
        user.is_client = role == 'client'
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProjectForm(forms.ModelForm):
    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline < timezone.now().date():
            raise forms.ValidationError("Дедлайн не может быть в прошлом.")
        return deadline

    class Meta:
        model = Project
        fields = ['title', 'description', 'budget', 'deadline']


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['proposal_text', 'proposed_price']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'bio']