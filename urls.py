from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RehabilitationProgramViewSet, RehabilitationEnrollmentViewSet

router = DefaultRouter()
router.register(r'programs', RehabilitationProgramViewSet, basename='rehabilitation-program')
router.register(r'enrollments', RehabilitationEnrollmentViewSet, basename='rehabilitation-enrollment')

urlpatterns = [
    path('', include(router.urls)),
]
