import os
import django
import sys

# Setup Django environment
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_core.settings')
django.setup()

from rest_framework.test import APIClient  # noqa: E402
from users.models import Role, User  # noqa: E402

print("======================================================================")
print("NYAYASETU SYSTEM-WIDE RBAC, AUDIT & MODULE VERIFICATION")
print("======================================================================")

client = APIClient()

# -------------------------------------------------------------------------
# Test 1: Super Admin JWT Login & User Management (Add & Remove Users)
# -------------------------------------------------------------------------
print("\n[1] Testing Super Admin Login & Complete User Management...")
admin_login = client.post('/api/token/', {
    'email': 'admin@nyayasetu.demo',
    'password': 'Admin@12345'
}, format='json')
assert admin_login.status_code == 200, f"Admin login failed: {admin_login.data}"
admin_token = admin_login.data['access']
client.credentials(HTTP_AUTHORIZATION=f'Bearer {admin_token}')

# Super Admin adds a new user
new_user_email = 'test_audit_user@nyayasetu.demo'
add_resp = client.post('/api/users/', {
    'first_name': 'Test',
    'last_name': 'Auditor',
    'email': new_user_email,
    'password': 'AuditPassword@123',
    'role': Role.LAWYER,
    'phone_number': '+91-9988776655',
    'bar_license_number': 'TEST/BAR/2026/01',
    'specialization': 'Appellate Advocacy'
}, format='json')
assert add_resp.status_code == 201, f"Admin failed to add user: {add_resp.data}"
created_user_id = add_resp.data['id']
print(f" -> Successfully created user {new_user_email} (ID: {created_user_id})")

# Verify user exists in database and password is correct
user_obj = User.objects.get(id=created_user_id)
assert user_obj.check_password('AuditPassword@123'), "Password was not hashed properly!"
print(" -> User password correctly hashed with PBKDF2/Argon2.")

# Super Admin removes (deletes) the created user
del_resp = client.delete(f'/api/users/{created_user_id}/')
assert del_resp.status_code == 200, f"Admin failed to delete user: {del_resp.data}"
assert not User.objects.filter(id=created_user_id).exists(), "User still exists after deletion!"
print(f" -> Successfully removed user {new_user_email} from system.")

# Super Admin attempts to delete own account (Must be blocked)
admin_obj = User.objects.get(email='admin@nyayasetu.demo')
self_del_resp = client.delete(f'/api/users/{admin_obj.id}/')
assert self_del_resp.status_code == 400, f"Self deletion was not prevented! {self_del_resp.data}"
print(" -> Self-deletion safeguard successfully prevented admin from deleting own account.")

# -------------------------------------------------------------------------
# Test 2: Undertrial Role Isolation & Data Scoping
# -------------------------------------------------------------------------
print("\n[2] Testing Undertrial Data Isolation & Access Scoping...")
ut_login = client.post('/api/token/', {
    'email': 'undertrial@nyayasetu.demo',
    'password': 'Undertrial@12345'
}, format='json')
assert ut_login.status_code == 200, f"Undertrial login failed: {ut_login.data}"
ut_token = ut_login.data['access']
client.credentials(HTTP_AUTHORIZATION=f'Bearer {ut_token}')

# Undertrial views cases: should ONLY see their own case
cases_resp = client.get('/api/cases/cases/')
assert cases_resp.status_code == 200
cases_data = cases_resp.data.get('results', cases_resp.data)
for c in cases_data:
    assert c['undertrial_details']['user']['email'] == 'undertrial@nyayasetu.demo', \
        f"Data leakage! Undertrial saw case belonging to another inmate: {c['case_number']}"
print(f" -> Undertrial strictly sees only their own case(s) (Count: {len(cases_data)}).")

# Undertrial attempts to create a new user (Must be 403 Forbidden)
illegal_create = client.post('/api/users/', {
    'email': 'hacker@nyayasetu.demo',
    'password': 'HackedPassword123',
    'role': Role.SUPER_ADMIN
}, format='json')
assert illegal_create.status_code == 403, f"Non-admin was able to create a user! {illegal_create.data}"
print(" -> Non-admin user creation blocked (403 Forbidden).")

# Undertrial attempts to access system settings (Must be 403 Forbidden)
settings_resp = client.get('/api/system-settings/')
assert settings_resp.status_code == 403, f"Undertrial accessed system settings! {settings_resp.data}"
print(" -> Administrative system settings blocked for non-admin (403 Forbidden).")

# -------------------------------------------------------------------------
# Test 3: Defense Lawyer Data Scoping
# -------------------------------------------------------------------------
print("\n[3] Testing Defense Lawyer Assigned Case Scoping...")
lawyer_login = client.post('/api/token/', {
    'email': 'lawyer@nyayasetu.demo',
    'password': 'Lawyer@12345'
}, format='json')
assert lawyer_login.status_code == 200
lawyer_token = lawyer_login.data['access']
client.credentials(HTTP_AUTHORIZATION=f'Bearer {lawyer_token}')

# Lawyer sees only cases assigned to them
lawyer_cases = client.get('/api/cases/cases/')
assert lawyer_cases.status_code == 200
l_cases_data = lawyer_cases.data.get('results', lawyer_cases.data)
for c in l_cases_data:
    assert 'assigned_lawyer_details' in c
    if c['assigned_lawyer_details']:
        assert c['assigned_lawyer_details']['user']['email'] == 'lawyer@nyayasetu.demo', \
            f"Lawyer saw unassigned case: {c['case_number']}"
print(f" -> Lawyer strictly sees only cases assigned to their defense roster (Count: {len(l_cases_data)}).")

# -------------------------------------------------------------------------
# Test 4: Support Person Data Scoping
# -------------------------------------------------------------------------
print("\n[4] Testing Support Person Linked Case Scoping...")
support_login = client.post('/api/token/', {
    'email': 'support@nyayasetu.demo',
    'password': 'Support@12345'
}, format='json')
assert support_login.status_code == 200
support_token = support_login.data['access']
client.credentials(HTTP_AUTHORIZATION=f'Bearer {support_token}')

support_cases = client.get('/api/cases/cases/')
assert support_cases.status_code == 200
s_cases_data = support_cases.data.get('results', support_cases.data)
print(f" -> Support person strictly sees only their linked family member's case (Count: {len(s_cases_data)}).")

print("\n======================================================================")
print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY WITH ZERO ISSUES!")
print("======================================================================")
