from pyexpat import model
from django.db import models
from quizes.models import Quiz

# Create your models here.

class Questions(models.Model):
    text = models.CharField(max_length=300)
    quiz_one = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answers_set.all()
    
class Answers(models.Model):
    text = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
    