from django.db.models.fields import DateField, DateTimeField
from django.forms import widgets, ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from django.utils.regex_helper import Choice
from django.contrib.admin import widgets
import datetime
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

