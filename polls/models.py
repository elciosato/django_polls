from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(verbose_name="Question", max_length=200)
    pub_date = models.DateTimeField(
        verbose_name="Publish Date", auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(
        Question, related_name="choices_set", on_delete=models.CASCADE)

    choice_text = models.CharField(verbose_name="Choice", max_length=200)
    vote = models.IntegerField(verbose_name="Votes", default=0)

    def __str__(self):
        return self.choice_text
