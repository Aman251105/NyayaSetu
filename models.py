from django.db import models
import uuid
from users.models import UndertrialProfile, User


class RehabProgramType(models.TextChoices):
    DIGITAL_LITERACY = 'DIGITAL_LITERACY', 'Digital Literacy'
    COMPUTER_BASICS = 'COMPUTER_BASICS', 'Computer Basics'
    COMMUNICATION_SKILLS = 'COMMUNICATION_SKILLS', 'Communication Skills'
    VOCATIONAL = 'VOCATIONAL', 'Vocational Training'
    ENTREPRENEURSHIP = 'ENTREPRENEURSHIP', 'Entrepreneurship'
    EDUCATION = 'EDUCATION', 'Education'
    LIFE_SKILLS = 'LIFE_SKILLS', 'Life Skills'
    COUNSELING = 'COUNSELING', 'Mental Health & Counseling'
    LEGAL_LITERACY = 'LEGAL_LITERACY', 'Legal Rights Education'


class RehabilitationProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    program_type = models.CharField(
        max_length=50, choices=RehabProgramType.choices)
    description = models.TextField(blank=True, null=True)
    provider_name = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class EnrollmentStatus(models.TextChoices):
    ENROLLED = 'ENROLLED', 'Enrolled'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    COMPLETED = 'COMPLETED', 'Completed'
    DROPPED = 'DROPPED', 'Dropped'


class RehabilitationEnrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(
        RehabilitationProgram,
        on_delete=models.CASCADE,
        related_name='enrollments')
    undertrial = models.ForeignKey(
        UndertrialProfile,
        on_delete=models.CASCADE,
        related_name='rehab_enrollments')
    status = models.CharField(
        max_length=50,
        choices=EnrollmentStatus.choices,
        default=EnrollmentStatus.ENROLLED)
    enrollment_date = models.DateField(auto_now_add=True)
    completion_date = models.DateField(blank=True, null=True)
    attendance_rate = models.FloatField(
        blank=True, null=True)  # Percentage 0-100
    notes = models.TextField(blank=True, null=True)
    managed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_enrollments')  # User with REHAB_STAFF role

    def __str__(self):
        return f"{self.undertrial} in {self.program.name}"
