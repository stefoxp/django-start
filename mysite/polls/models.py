from django.db import models

# Create your models here.
'''
each model (= class) has a number of class variables,
each of which represents a database field in the model
Each field is represented by an instance of a Field class
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
