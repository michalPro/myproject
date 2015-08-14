from django import forms
from django.forms.extras.widgets import SelectDateWidget


classes = (
    ('Warrior', 'Warrior'),
    ('Thief', 'Thief'),
    ('Tankozord', 'Tankozord'),
)


class CreateForm(forms.Form):
    name = forms.CharField(max_length=20)
    classname = forms.MultipleChoiceField(required=True,
        widget=forms.CheckboxSelectMultiple, choices=classes)