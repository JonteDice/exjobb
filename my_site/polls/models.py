from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.TextField()
    answer_1 = models.CharField(max_length = 255)
    answer_2 = models.CharField(max_length = 255)
    answer_3 = models.CharField(max_length = 255)
    total_1 = models.IntegerField(default=0)
    total_2 = models.IntegerField(default=0)
    total_3 = models.IntegerField(default=0)

    def total(self):
        return self.total_1 + self.total_2 + self.total_3