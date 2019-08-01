from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Management_Skill
from . serializers import Management_SkillSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions


@permission_classes((permissions.AllowAny,))

class SkillList(APIView):

	def get(self, request):
		skill1=Management_Skill.objects.all()
		serializer=Management_SkillSerializer(skill1, many=True)
		return Response(serializer.data)

	def post(self):
		pass
