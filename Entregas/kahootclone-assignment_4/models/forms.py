from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from models.models import Questionnaire
from models.models import Question
from models.models import Answer


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class CreateQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = Questionnaire
        fields = ['title']


class RemoveQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = Questionnaire
        fields = ['title']


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question', 'answerTime']


class RemoveQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question']


class CreateAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer', 'correct']


class RemoveAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer']
