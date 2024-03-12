from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    constraints = models.TextField()
    sample_input_1 = models.TextField(default='')
    sample_output_1 = models.TextField(default='')
    sample_input_2 = models.TextField(default='')
    sample_output_2 = models.TextField(default='')
    hidden_input_1 = models.TextField(default='')
    hidden_output_1 = models.TextField(default='')
    hidden_input_2 = models.TextField(default='')
    hidden_output_2 = models.TextField(default='')
    hidden_input_3 = models.TextField(default='')
    hidden_output_3 = models.TextField(default='')

    def __str__(self):
        return self.title
