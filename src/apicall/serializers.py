from rest_framework import serializers
from . models import Management_Skill

class Management_SkillSerializer(serializers.ModelSerializer):

	class Meta:
		model=Management_Skill
		#fields=('skill','skill_id')
		fields='__all__'