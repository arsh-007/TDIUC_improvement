from django.db import models


class Feedback(models.Model):
    details = models.TextField()
    satisfaction = models.BooleanField()
    question_id = models.IntegerField(default=1)
    image_id = models.IntegerField(default=1)
    initial_answer = models.TextField(default='init')
    date = models.DateField(auto_now_add=True)
