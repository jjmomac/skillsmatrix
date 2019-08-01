from django.db import models

# Create your models here.
class Management_Skill(models.Model):
	skill_id=models.AutoField(primary_key=True)
	skill=models.CharField(max_length=30)

	def __str__(self):
		return self.skill