import datetime

from django.db import models
from django.utils import timezone

#Dans notre application de sondage, nous allons créer deux modèles :
# Question et Choice (choix). Une Question possède une question et une date de mise en ligne.
# Un choix a deux champs : le texte représentant le choix et le décompte des votes. Chaque choix est associé à une Question.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


