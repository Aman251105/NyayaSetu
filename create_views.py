
rehab_views = """from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import RehabilitationProgram, RehabilitationEnrollment
from .serializers import RehabilitationProgramSerializer, RehabilitationEnrollmentSerializer

class RehabilitationProgramViewSet(viewsets.ModelViewSet):
    queryset = RehabilitationProgram.objects.all()
    serializer_class = RehabilitationProgramSerializer
    permission_classes = [IsAuthenticated]

class RehabilitationEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = RehabilitationEnrollment.objects.all()
    serializer_class = RehabilitationEnrollmentSerializer
    permission_classes = [IsAuthenticated]
"""

rehab_urls = """from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RehabilitationProgramViewSet, RehabilitationEnrollmentViewSet

router = DefaultRouter()
router.register(r'programs', RehabilitationProgramViewSet)
router.register(r'enrollments', RehabilitationEnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
"""

cases_views = """from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Court, Case, Hearing, BailApplication, Document
from .serializers import CourtSerializer, CaseSerializer, HearingSerializer, BailApplicationSerializer, DocumentSerializer

class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all().order_by('name')
    serializer_class = CourtSerializer
    permission_classes = [IsAuthenticated]

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all().order_by('-created_at')
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not serializer.validated_data.get('undertrial'):
            from users.models import UndertrialProfile
            profile = UndertrialProfile.objects.first()
            if profile:
                serializer.save(undertrial=profile)
            else:
                serializer.save()
        else:
            serializer.save()

class HearingViewSet(viewsets.ModelViewSet):
    queryset = Hearing.objects.all().order_by('-hearing_date')
    serializer_class = HearingSerializer
    permission_classes = [IsAuthenticated]

class BailApplicationViewSet(viewsets.ModelViewSet):
    queryset = BailApplication.objects.all().order_by('-created_at')
    serializer_class = BailApplicationSerializer
    permission_classes = [IsAuthenticated]

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-uploaded_at')
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
"""

cases_urls = """from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, CaseViewSet, HearingViewSet, BailApplicationViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'cases', CaseViewSet)
router.register(r'hearings', HearingViewSet)
router.register(r'bail-applications', BailApplicationViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
"""

with open("rehab/views.py", "w") as f:
    f.write(rehab_views)
with open("rehab/urls.py", "w") as f:
    f.write(rehab_urls)
with open("cases/views.py", "w") as f:
    f.write(cases_views)
with open("cases/urls.py", "w") as f:
    f.write(cases_urls)
