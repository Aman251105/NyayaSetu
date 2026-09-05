from rest_framework import serializers
from .models import RehabilitationProgram, RehabilitationEnrollment
from users.serializers import UndertrialProfileSerializer, UserSerializer


class RehabilitationProgramSerializer(serializers.ModelSerializer):
    program_type_display = serializers.CharField(
        source='get_program_type_display', read_only=True)

    class Meta:
        model = RehabilitationProgram
        fields = '__all__'


class RehabilitationEnrollmentSerializer(serializers.ModelSerializer):
    program_details = RehabilitationProgramSerializer(
        source='program', read_only=True)
    undertrial_details = UndertrialProfileSerializer(
        source='undertrial', read_only=True)
    managed_by_details = UserSerializer(source='managed_by', read_only=True)
    status_display = serializers.CharField(
        source='get_status_display', read_only=True)

    class Meta:
        model = RehabilitationEnrollment
        fields = '__all__'
