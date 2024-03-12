# lc_questions/forms.py

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'constraints',
                  'sample_input_1', 'sample_output_1',
                  'sample_input_2', 'sample_output_2',
                  'hidden_input_1', 'hidden_output_1',
                  'hidden_input_2', 'hidden_output_2',
                  'hidden_input_3', 'hidden_output_3']
