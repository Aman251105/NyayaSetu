from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import RehabilitationProgram, RehabilitationEnrollment
from .serializers import RehabilitationProgramSerializer, RehabilitationEnrollmentSerializer
from users.models import Role


class RehabilitationProgramViewSet(viewsets.ModelViewSet):
    queryset = RehabilitationProgram.objects.all().order_by('name')
    serializer_class = RehabilitationProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in (Role.SUPER_ADMIN, Role.REHAB_STAFF):
            return RehabilitationProgram.objects.all().order_by('name')
        return RehabilitationProgram.objects.filter(is_active=True).order_by('name')

    def create(self, request, *args, **kwargs):
        if request.user.role not in (Role.SUPER_ADMIN, Role.REHAB_STAFF):
            return Response(
                {'detail': 'Only Super Admin and Rehabilitation Staff can create rehabilitation programs.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.role not in (Role.SUPER_ADMIN, Role.REHAB_STAFF):
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != Role.SUPER_ADMIN:
            return Response({'detail': 'Only Super Administrators can delete programs.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class RehabilitationEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = RehabilitationEnrollment.objects.all().order_by('-enrollment_date')
    serializer_class = RehabilitationEnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = user.role

        if role == Role.SUPER_ADMIN:
            return RehabilitationEnrollment.objects.all().order_by('-enrollment_date')

        if role == Role.REHAB_STAFF:
            # Rehab staff see enrollments they personally manage or all in system for staffing
            return RehabilitationEnrollment.objects.filter(
                managed_by=user
            ).order_by('-enrollment_date') | RehabilitationEnrollment.objects.filter(
                managed_by__isnull=True
            ).order_by('-enrollment_date')

        if role == Role.UNDERTRIAL:
            try:
                profile = user.undertrial_profile
                return RehabilitationEnrollment.objects.filter(
                    undertrial=profile
                ).order_by('-enrollment_date')
            except Exception:
                return RehabilitationEnrollment.objects.none()

        if role == Role.SUPPORT_PERSON:
            try:
                support = user.support_profile
                return RehabilitationEnrollment.objects.filter(
                    undertrial=support.undertrial
                ).order_by('-enrollment_date')
            except Exception:
                return RehabilitationEnrollment.objects.none()

        if role in (Role.PRISON_AUTHORITY, Role.UTRC_AUTHORITY, Role.LAWYER):
            # Read-only overview access
            return RehabilitationEnrollment.objects.all().order_by('-enrollment_date')

        return RehabilitationEnrollment.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role == Role.UNDERTRIAL:
            serializer.save(undertrial=user.undertrial_profile)
        elif user.role == Role.REHAB_STAFF and not serializer.validated_data.get('managed_by'):
            serializer.save(managed_by=user)
        else:
            serializer.save()

    def destroy(self, request, *args, **kwargs):
        if request.user.role != Role.SUPER_ADMIN:
            return Response({'detail': 'Permission denied: Only Super Admin can delete enrollments.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
