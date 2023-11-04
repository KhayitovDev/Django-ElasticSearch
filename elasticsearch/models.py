from django.db import models

# Create your models here.

class Verb(models.Model):
    first_form=models.CharField(max_length=250)
    second_form=models.CharField(max_length=250)
    third_form=models.CharField(max_length=250)
    translation_to_uzbek=models.CharField(max_length=250, blank=True)
    example_first=models.TextField(blank=True)
    example_second=models.TextField(blank=True)
    example_third=models.TextField(blank=True)

    def __str__(self) -> str:
        return self.first_form
    

    class Meta:
        ordering=['-first_form']


