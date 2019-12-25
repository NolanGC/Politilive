from django.db import models

# Create your models here.


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    choices = ['Strongly Agree', 'Agree',
               'Neutral', 'Disagree', 'Strongly Disagree']

    strong_agree_xchange = models.IntegerField(default=0)
    agree_xchange = models.IntegerField(default=0)
    neutral_xchange = models.IntegerField(default=0)
    disagree_xchange = models.IntegerField(default=0)
    strong_disagree_xchange = models.IntegerField(default=0)

    strong_agree_ychange = models.IntegerField(default=0)
    agree_ychange = models.IntegerField(default=0)
    neutral_ychange = models.IntegerField(default=0)
    disagree_ychange = models.IntegerField(default=0)
    strong_disagree_ychange = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

    def get_change(self, choice):
        if(choice == 'Strongly Agree'):
            return [self.strong_agree_xchange, self.strong_agree_ychange]
        elif(choice == 'Agree'):
            return [self.agree_xchange, self.agree_ychange]
        elif(choice == 'Neutral'):
            return [self.neutral_xchange, self.neutral_ychange]
        elif(choice == 'Disagree'):
            return [self.disagree_xchange, self.disagree_ychange]
        elif(choice == 'Strongly Disagree'):
            return [self.strong_disagree_xchange, self.strong_disagree_ychange]
