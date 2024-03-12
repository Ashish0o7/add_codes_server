# lc_questions/views.py

from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import Question

from django.http import JsonResponse
from django.core import serializers
from .models import Question

def question_list(request):
    questions = Question.objects.all()
    # Serialize the queryset to JSON
    data = serializers.serialize('json', questions)
    return JsonResponse(data, safe=False)

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://code-editor-6rqa.onrender.com/')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})
