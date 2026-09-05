from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from users.models import Role, Prison, UndertrialProfile
from rehab.models import RehabilitationProgram, RehabilitationEnrollment, RehabProgramType, EnrollmentStatus

User = get_user_model()


class RehabilitationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            email='admin@nyayasetu.demo',
            password='Admin@12345',
            role=Role.SUPER_ADMIN
        )
        self.prison = Prison.objects.create(
            name='Tihar Central', location='Delhi', capacity=1500)
        self.rehab_staff = User.objects.create_user(
            email='rehab@nyayasetu.demo',
            password='Rehab@12345',
            first_name='Ananya',
            last_name='Deshmukh',
            role=Role.REHAB_STAFF
        )
        self.undertrial_user1 = User.objects.create_user(
            email='undertrial1@nyayasetu.demo',
            password='Password@123',
            first_name='Vikram',
            last_name='Singh',
            role=Role.UNDERTRIAL
        )
        self.ut_profile1 = UndertrialProfile.objects.create(
            user=self.undertrial_user1,
            prison=self.prison,
            prisoner_number='UT-REHAB-01'
        )
        self.undertrial_user2 = User.objects.create_user(
            email='undertrial2@nyayasetu.demo',
            password='Password@123',
            first_name='Raju',
            last_name='Kumar',
            role=Role.UNDERTRIAL
        )
        self.ut_profile2 = UndertrialProfile.objects.create(
            user=self.undertrial_user2,
            prison=self.prison,
            prisoner_number='UT-REHAB-02'
        )

        self.program = RehabilitationProgram.objects.create(
            name='Digital Literacy & Computer Basics',
            program_type=RehabProgramType.DIGITAL_LITERACY,
            provider_name='National Skill Development Mission',
            is_active=True
        )

    def test_program_creation_permissions(self):
        # Rehab staff can create program
        self.client.force_authenticate(user=self.rehab_staff)
        resp = self.client.post('/api/rehab/programs/', {
            'name': 'Electrician Vocational Certification',
            'program_type': RehabProgramType.VOCATIONAL,
            'provider_name': 'Pratham NGO'
        }, format='json')
        self.assertEqual(resp.status_code, 201)

        # Undertrial cannot create program
        self.client.force_authenticate(user=self.undertrial_user1)
        resp2 = self.client.post('/api/rehab/programs/', {
            'name': 'Unauthorized Program',
            'program_type': RehabProgramType.VOCATIONAL,
            'provider_name': 'Self'
        }, format='json')
        self.assertEqual(resp2.status_code, 403)

    def test_enrollment_workflow_and_scoping(self):
        # Create enrollment for Undertrial 1
        enr1 = RehabilitationEnrollment.objects.create(
            program=self.program,
            undertrial=self.ut_profile1,
            managed_by=self.rehab_staff,
            status=EnrollmentStatus.ENROLLED,
            attendance_rate=88.5
        )
        # Create enrollment for Undertrial 2
        RehabilitationEnrollment.objects.create(
            program=self.program,
            undertrial=self.ut_profile2,
            status=EnrollmentStatus.IN_PROGRESS,
            attendance_rate=92.0
        )

        # Undertrial 1 only sees enr1
        self.client.force_authenticate(user=self.undertrial_user1)
        resp1 = self.client.get('/api/rehab/enrollments/')
        self.assertEqual(resp1.status_code, 200)
        results1 = resp1.data.get('results', resp1.data)
        self.assertEqual(len(results1), 1)
        self.assertEqual(results1[0]['id'], str(enr1.id))

        # Admin sees both
        self.client.force_authenticate(user=self.admin)
        resp_admin = self.client.get('/api/rehab/enrollments/')
        self.assertEqual(resp_admin.status_code, 200)
        results_admin = resp_admin.data.get('results', resp_admin.data)
        self.assertEqual(len(results_admin), 2)

    def test_non_admin_cannot_delete_enrollment(self):
        enr = RehabilitationEnrollment.objects.create(
            program=self.program,
            undertrial=self.ut_profile1,
            managed_by=self.rehab_staff
        )
        self.client.force_authenticate(user=self.rehab_staff)
        resp = self.client.delete(f'/api/rehab/enrollments/{enr.id}/')
        self.assertEqual(resp.status_code, 403)
        self.assertTrue(
            RehabilitationEnrollment.objects.filter(
                id=enr.id).exists())

    def test_admin_can_delete_enrollment(self):
        enr = RehabilitationEnrollment.objects.create(
            program=self.program,
            undertrial=self.ut_profile1,
            managed_by=self.rehab_staff
        )
        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f'/api/rehab/enrollments/{enr.id}/')
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(
            RehabilitationEnrollment.objects.filter(
                id=enr.id).exists())
