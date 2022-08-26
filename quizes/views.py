from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Answers, Questions
from results.models import Result
import math
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'
    
def quiz_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request,'quizes/quiz.html',{'obj':quiz})

def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for question in quiz.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)
        questions.append({str(question):answers})
        
    return JsonResponse({
        'data': questions,
        'time': quiz.time
    })

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    
def save_quiz_view(request,pk):
    if is_ajax(request=request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())#converts querydict to ordinary dict
        data_.pop('csrfmiddlewaretoken')#remove the token
        
        for k in data_.keys():
            question = Questions.objects.get(text=k)
            questions.append(question)
        
        
        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        
        score = 0
        multiplier = 100 / quiz.number_of_questions
        
        results = []
        correct_answer = None
        
        for q in questions:
            selected_answer = request.POST.get(q.text)
            if selected_answer != '':
                question_answers = Answers.objects.filter(question=q)
                for a in question_answers:
                    if selected_answer == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else: 
                        if a.correct:
                            correct_answer = a.text
                            
                results .append({str(q):{'correct_answer':correct_answer,'answered':selected_answer}})
                
            else:
                results.append({str(q):'not answered'})
                
        score_ = score * multiplier
        Result.objects.create(user=user,quiz=quiz,score=score_)
        
        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed':True,'score':score_,'results':results})
        else:
            return JsonResponse({"passed":False,'score':score_,'results':results})
                
    