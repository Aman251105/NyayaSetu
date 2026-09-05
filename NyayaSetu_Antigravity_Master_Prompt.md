# NyayaSetu – Antigravity Master Prompt

MASTER PROMPT FOR ANTIGRAVITY
Project: NyayaSetu – Digital Justice & Rehabilitation Platform for Undertrial Prisoners in India

ROLE
You are a senior full-stack engineer, UI/UX designer, database architect, security engineer, and product designer. Build a complete, functional, demo-ready web application named “NyayaSetu”.

IMPORTANT
Do not create only a UI mockup. Implement the frontend, backend/API layer, database/data models, authentication, role-based authorization, admin panel, demo/seed data, workflows, validations, notifications, dashboards, and all major interactions. The application must run locally and be easy to demonstrate.

PROJECT OBJECTIVE
NyayaSetu is a technology platform intended to improve access to legal aid, case information, bail-process assistance, rights awareness, and rehabilitation support for undertrial prisoners in India.

The system connects:
Undertrial Prisoner → Authorized Support Person → Lawyer/Legal Aid Provider → UTRC/Legal Aid Organization → Prison Authority → Authorized Administrators.

The application is a support and case-management platform. It must NOT make autonomous legal decisions, determine guilt/innocence, or replace lawyers/judges. Any legal eligibility or bail-related flag must be presented as a “requires professional review” alert.

CORE MODULES
1. Undertrial Case Management
2. Legal Aid & Lawyer Matching
3. Bail Assistance Tracking
4. Court Hearing & Case Timeline
5. Rights & Legal Awareness
6. Rehabilitation & Skill Development
7. Support-Person Portal
8. UTRC/Authority Dashboard
9. Notifications & Alerts
10. Analytics & Reports
11. Complete Super Admin Panel
12. Audit Logs & Security

RECOMMENDED TECH STACK
Use a production-structured stack:
Frontend:
- React
- TypeScript
- Tailwind CSS
- React Router
- Recharts or another suitable chart library
- Responsive design for desktop/tablet/mobile

Backend:
- Django
- Django REST Framework
- JWT/session authentication as appropriate
- PostgreSQL
- Django ORM

Use environment variables for secrets and configuration.
If the Antigravity environment requires a different equivalent stack, preserve the same architecture and functionality.

DESIGN DIRECTION
Create a professional, modern, trustworthy government/legal-tech style interface.

Visual language:
- Clean white/light backgrounds
- Deep blue/navy primary accents
- Subtle neutral gray surfaces
- Accessible contrast
- Rounded cards with restrained shadows
- Clear typography
- Professional icons
- Minimal animation
- Responsive layouts
- Avoid excessive gradients or flashy effects

Brand:
Name: NyayaSetu
Tagline: “Bridging the Gap Between Justice and Access”

Create a simple text/logo treatment for NyayaSetu with a justice/bridge-inspired visual identity.

GLOBAL UX REQUIREMENTS
- Responsive on desktop, tablet, and mobile
- Sidebar navigation on dashboards
- Top navigation with profile, notifications, and logout
- Breadcrumbs where useful
- Loading states
- Empty states
- Error states
- Success/error toast messages
- Confirmation dialogs for destructive actions
- Search, filters, sorting, and pagination on data-heavy pages
- Accessible forms with validation
- Keyboard-friendly controls
- Consistent status badges
- Never expose sensitive prisoner information publicly

USER ROLES
Implement strict Role-Based Access Control (RBAC).

1. SUPER ADMIN
Full rights across the platform.
Can:
- Create/read/update/delete users
- Manage every role
- Manage undertrials
- Manage cases
- Manage lawyers
- Manage legal-aid organizations
- Manage UTRCs
- Manage prisons
- Manage courts
- Manage hearings
- Manage bail records
- Manage documents
- Manage rehabilitation programs
- Manage rights-awareness content
- Manage notifications
- View analytics
- Export reports
- View audit logs
- Configure system settings
- Activate/deactivate accounts
- Reset user access
- Assign/reassign cases
- Override ordinary workflow restrictions when necessary, with an audit entry

2. UTRC / AUTHORITY
Can:
- View authorized cases
- Monitor case status
- View priority alerts
- Review bail-related workflow status
- Assign/coordinate legal aid
- Monitor hearings
- View authorized reports
- Track rehabilitation progress
- Generate reports

3. LAWYER / LEGAL AID PROVIDER
Can:
- View assigned cases
- View permitted prisoner/case details
- Update legal representation status
- Add hearing updates
- Update bail application workflow
- Upload permitted legal documents
- Add case notes
- View relevant legal resources
- Receive notifications

4. PRISON AUTHORITY
Can:
- View authorized prisoner records
- Update permitted custody information
- View case/hearing status
- Record authorized rehabilitation participation
- Receive system alerts

5. SUPPORT PERSON
Can only view records explicitly authorized for them:
- Case status
- Next hearing
- Lawyer information
- Bail workflow status
- Approved documents/instructions
- Rights-awareness resources
- Notifications

6. UNDERTRIAL
Can access their own permitted information:
- Case status
- Hearing information
- Lawyer information
- Bail workflow information
- Legal rights resources
- Rehabilitation resources
- Notifications

7. REHABILITATION STAFF / NGO
Can:
- View assigned participants
- Manage education/vocational programs
- Record attendance/progress
- Upload permitted completion records
- Track rehabilitation outcomes

AUTHENTICATION
Create:
- Login
- Logout
- Password hashing
- Role-based route protection
- Session/token handling
- Unauthorized access page
- Account activation/deactivation
- Password reset flow suitable for demo
- Optional “remember me”
- Profile page

ADMIN PANEL
Create a dedicated, polished Super Admin dashboard, NOT just the default framework admin.

Admin dashboard cards:
- Total Users
- Total Undertrials
- Active Cases
- Cases Requiring Review
- Pending Bail Workflows
- Upcoming Hearings
- Unassigned Legal-Aid Cases
- Active Rehabilitation Programs

Admin pages:
1. Dashboard
2. Users
3. Undertrials
4. Cases
5. Lawyers
6. Legal Aid Organizations
7. UTRCs
8. Prisons
9. Courts
10. Hearings
11. Bail Applications
12. Documents
13. Rehabilitation Programs
14. Rights & Awareness Content
15. Notifications
16. Reports & Analytics
17. Audit Logs
18. System Settings

Every admin data table must support:
- Search
- Filter
- Sort
- Pagination
- View
- Edit
- Create where applicable
- Delete/archive where appropriate
- Activate/deactivate
- Export where appropriate

For sensitive/destructive actions:
- Require confirmation
- Record who performed the action
- Record timestamp
- Record the affected record
- Record before/after values when practical

CASE MANAGEMENT
Create a complete case profile.

Fields:
- Case ID
- FIR number
- Case number
- Undertrial
- Court
- Police station
- Applicable legal sections
- Case type
- Case status
- Date of arrest
- Date of admission/custody
- Assigned lawyer
- Legal aid organization
- UTRC
- Next hearing date
- Last hearing date
- Bail status
- Priority
- Notes
- Created date
- Updated date

Case statuses:
- Newly Registered
- Legal Aid Required
- Lawyer Assigned
- Bail Assistance
- Hearing Scheduled
- Under Proceedings
- Disposed
- Released
- Transferred
- Requires Review

Create a visual case timeline:
Arrest → Case Registration → Legal Aid → Lawyer Assignment → Bail Application → Hearings → Decision/Disposition → Rehabilitation → Reintegration

BAIL ASSISTANCE MODULE
Create a dedicated bail workflow.

Fields:
- Bail Application ID
- Case
- Application date
- Application type
- Current status
- Lawyer
- Next action
- Hearing date
- Decision
- Notes
- Documents
- Last updated

Statuses:
- Not Applied
- Preparation
- Filed
- Hearing Scheduled
- Pending Decision
- Granted
- Rejected
- Withdrawn
- Requires Review

Add a rules-based alert system that can flag cases for professional review based on configurable dates/statuses. Never present an automated flag as a legal conclusion.

LEGAL-AID MATCHING
Create a lawyer directory with:
- Name
- Bar/license identifier placeholder
- Specialization
- Location
- Organization
- Availability
- Languages
- Cases assigned
- Active/inactive status

Create matching/filtering by:
- Case type
- Location
- Specialization
- Language
- Availability

Display recommended matches with a clear disclaimer:
“Matching is administrative support only. Final assignment must be confirmed by an authorized legal-aid authority.”

RIGHTS AWARENESS
Create a multilingual-friendly rights-awareness module.

Categories:
- Legal Aid
- Bail Awareness
- Court Proceedings
- Undertrial Rights
- UTRC Assistance
- Prisoner Support
- Family/Support Person Guidance
- Legal Documentation

Each article should contain:
- Title
- Simple explanation
- Detailed explanation
- Who can help
- What to do next
- Required documents if applicable
- Last reviewed date
- Language
- Published/unpublished status

Use simple, understandable language. Do not invent laws, rights, deadlines, or legal advice. Demo content must be clearly labeled as sample/demo content.

REHABILITATION MODULE
Create:
- Programs
- Participants
- Enrollment
- Attendance
- Progress
- Completion
- Certificates/records

Program types:
- Digital Literacy
- Computer Basics
- Communication Skills
- Vocational Training
- Entrepreneurship
- Education
- Life Skills

Dashboard metrics:
- Enrolled
- In Progress
- Completed
- Completion Rate

SUPPORT-PERSON PORTAL
Create an authorized support-person dashboard.

Show:
- Connected undertrial
- Case status
- Next hearing
- Lawyer details
- Bail workflow status
- Approved documents
- Notifications
- Rights-awareness resources

Never expose data beyond the support person's authorization.

NOTIFICATIONS
Implement an in-app notification system.

Examples:
- Upcoming hearing
- Lawyer assigned
- Case updated
- Bail status updated
- Document uploaded
- Legal-aid request received
- Rehabilitation program update
- Admin/system notification

Use notification states:
- Unread
- Read
- Archived

DASHBOARDS

UNDERTRIAL DASHBOARD
Cards:
- Current Case Status
- Next Hearing
- Lawyer
- Bail Status
- Rehabilitation Progress

Sections:
- Case Timeline
- Important Notifications
- Rights & Resources
- Rehabilitation

LAWYER DASHBOARD
Cards:
- Assigned Cases
- Hearings This Week
- Pending Bail Workflows
- Cases Requiring Update

Tables:
- Assigned Cases
- Upcoming Hearings
- Recent Notifications

UTRC/AUTHORITY DASHBOARD
Cards:
- Total Undertrials
- Active Cases
- Pending Bail Workflows
- Cases Requiring Review
- Unassigned Cases
- Upcoming Hearings

Charts:
- Cases by status
- Cases by priority
- Bail workflow distribution
- Monthly case activity
- Rehabilitation participation

PRISON AUTHORITY DASHBOARD
Show:
- Authorized undertrial count
- Upcoming hearings
- Case updates
- Rehabilitation participation
- Alerts requiring attention

ADMIN ANALYTICS
Include:
- Total cases
- Active/disposed cases
- Cases by status
- Cases by court
- Cases by location
- Bail workflow statistics
- Legal-aid assignment statistics
- Hearing trends
- Rehabilitation enrollment/completion
- User/role distribution

Allow date-range filtering.

REPORTS
Create downloadable/exportable reports for authorized users:
- Case status report
- Bail workflow report
- Hearing report
- Legal-aid assignment report
- Rehabilitation report
- User activity report

Do not include sensitive data in reports unless the requesting role is authorized.

AUDIT LOG
Every important administrative/security action should create an audit record:
- User
- Role
- Action
- Module
- Record ID
- Timestamp
- IP/device metadata if available and appropriate
- Before/after values where practical

Audit logs must be read-only for normal admins. Super Admin can manage retention/configuration but should not be able to silently erase individual audit records without an explicit audited action.

DATABASE MODELS
Implement normalized models for at least:
- User
- Role
- Undertrial
- SupportPerson
- Prison
- Court
- UTRC
- LegalAidOrganization
- LawyerProfile
- Case
- CaseAssignment
- Hearing
- BailApplication
- Document
- LegalResource
- RehabilitationProgram
- RehabilitationEnrollment
- Notification
- AuditLog
- SystemSetting

Add foreign keys, indexes, timestamps, unique constraints, and appropriate validation.

DEMO DATA
Seed the database with realistic but completely fictional data.

IMPORTANT:
Do not use real prisoners' names, real case numbers, real phone numbers, real addresses, or real personal information.

Create at least:
- 1 Super Admin
- 2 UTRC/Authority users
- 3 Lawyers
- 2 Prison Authority users
- 2 Rehabilitation/NGO users
- 5 Undertrial demo users
- 3 Support-person demo users
- 3 Legal-aid organizations
- 2 UTRCs
- 3 prisons
- 4 courts
- 10+ cases
- 15+ hearings
- 5+ bail applications
- 8+ rehabilitation programs/enrollments
- 15+ notifications
- 20+ audit-log entries
- 10+ rights-awareness resources

Use clearly fictional names such as:
- Aarav Mehta
- Rohan Shah
- Imran Khan
- Kavya Patel
- Neel Joshi
and similar fictional records.

Mark demo records internally as demo/sample where appropriate.

DEMO LOGIN ACCOUNTS
Create convenient demo accounts and display them in a development-only/demo login helper.

Example:
Super Admin:
admin@nyayasetu.demo
Password: Admin@12345

UTRC:
utrc@nyayasetu.demo
Password: Utrc@12345

Lawyer:
lawyer@nyayasetu.demo
Password: Lawyer@12345

Prison Authority:
prison@nyayasetu.demo
Password: Prison@12345

Support Person:
support@nyayasetu.demo
Password: Support@12345

Undertrial:
undertrial@nyayasetu.demo
Password: Undertrial@12345

Rehabilitation Staff:
rehab@nyayasetu.demo
Password: Rehab@12345

Clearly mark these credentials as DEMO ONLY and never use them in production.

DEMO SCENARIOS
Make sure the seeded data demonstrates:
1. A case with no lawyer assigned
2. A case with a lawyer assigned
3. A case with a pending bail workflow
4. A case with an upcoming hearing
5. A case requiring review
6. A released/closed case
7. A rehabilitation program in progress
8. A completed rehabilitation program
9. A support person connected to an undertrial
10. Notifications waiting to be read

The dashboard should look populated immediately after login.

DOCUMENT MANAGEMENT
Implement document upload metadata and secure access control.

Document types:
- FIR
- Bail Application
- Court Order
- Hearing Document
- Legal Aid Document
- Rehabilitation Document
- Other

Use file validation, size limits, access permissions, and safe filenames.

If actual file storage is unavailable in the demo environment, provide a functional mock/local storage implementation while preserving the same API structure.

SECURITY
Implement:
- Password hashing
- Authentication
- RBAC
- Protected routes
- API authorization
- Input validation
- CSRF protection where applicable
- Secure file handling
- SQL injection protection through ORM
- XSS-safe rendering
- Rate limiting where practical
- Audit logging
- No sensitive data in browser local storage unless absolutely necessary
- No sensitive information in URLs
- Environment variables for secrets

Never hard-code production secrets.

LEGAL/ETHICAL SAFETY
The platform must:
- Clearly label demo data
- Avoid making legal conclusions
- Avoid predicting court outcomes
- Avoid determining guilt/innocence
- Avoid automated legal advice
- Present bail/legal flags as “requires professional review”
- Restrict sensitive data according to user role
- Include a disclaimer in the legal resources section:
“This platform provides administrative and informational support and does not replace professional legal advice, judicial decision-making, or official legal processes.”

HOME/LANDING PAGE
Create an impressive landing page containing:
- NyayaSetu logo
- Tagline
- Problem statement
- How it works
- Key features
- Impact metrics using DEMO/SAMPLE labels
- User roles
- Legal awareness section preview
- Rehabilitation section preview
- Security/privacy section
- Login button
- Demo login button

Do not make fake claims such as “we have helped 10,000 prisoners” unless clearly labeled as fictional demo data.

MAIN NAVIGATION
Landing:
- Home
- About
- How It Works
- Legal Awareness
- Rehabilitation
- Login

Authenticated navigation should change according to role.

UI PAGES
Create all major pages instead of leaving placeholders:
- Login
- Forgot Password
- Dashboard
- Profile
- Notifications
- Case List
- Case Details
- Case Timeline
- Lawyer Directory
- Legal Aid Requests
- Bail Applications
- Hearings
- Legal Resources
- Rehabilitation Programs
- Support Person Dashboard
- Reports
- Admin Dashboard
- Admin Users
- Admin Cases
- Admin Lawyers
- Admin Organizations
- Admin UTRCs
- Admin Prisons
- Admin Courts
- Admin Hearings
- Admin Bail
- Admin Documents
- Admin Rehabilitation
- Admin Resources
- Admin Notifications
- Admin Audit Logs
- Admin Settings

API
Create clean REST APIs for:
- Authentication
- Users
- Undertrials
- Support persons
- Cases
- Case assignments
- Lawyers
- Legal-aid requests
- Hearings
- Bail applications
- Documents
- Legal resources
- Rehabilitation
- Notifications
- Analytics
- Reports
- Audit logs
- Admin operations

Use consistent API response structures and HTTP status codes.

SEARCH/FILTERING
Implement global or module-level search where useful.

Case filtering:
- Status
- Priority
- Court
- Lawyer
- UTRC
- Bail status
- Date range

Lawyer filtering:
- Specialization
- Location
- Language
- Availability

Rehabilitation filtering:
- Program
- Status
- Completion

ADMIN SYSTEM SETTINGS
Create configurable settings for:
- Case statuses
- Priority levels
- Notification rules
- Rehabilitation categories
- Legal-resource categories
- Document types
- Organization settings

Do not allow ordinary users to modify system settings.

TESTING
Create:
- Backend unit tests for critical models/API permissions
- Authentication tests
- RBAC tests
- Case workflow tests
- Bail workflow tests
- Admin authorization tests
- Basic frontend/component tests where practical

Verify that:
- Undertrial A cannot access Undertrial B's private data
- Support person only sees authorized data
- Lawyer only sees assigned/authorized cases
- UTRC sees only authorized jurisdiction/data
- Super Admin can access all administrative modules

SEEDING
Create a repeatable seed command/script, for example:
python manage.py seed_demo

It must safely create/update demo records without creating uncontrolled duplicates.

README
Create a comprehensive README containing:
- Project overview
- Features
- Architecture
- Tech stack
- Folder structure
- Setup instructions
- Environment variables
- Database setup
- Migration commands
- Seed demo command
- Demo credentials
- API overview
- User roles
- Security notes
- Testing instructions
- Deployment instructions
- Known limitations
- Legal/ethical disclaimer

ENVIRONMENT
Create a .env.example with variables such as:
DATABASE_URL
SECRET_KEY
DEBUG
ALLOWED_HOSTS
CORS_ALLOWED_ORIGINS
JWT_SECRET or equivalent
FILE_STORAGE configuration

Never commit real secrets.

ERROR HANDLING
Create useful:
- 404 page
- 403 unauthorized page
- 500 error page
- API error handling
- Form validation messages
- Network failure states

PERFORMANCE
- Paginate large tables
- Avoid unnecessary API requests
- Lazy-load heavy pages where appropriate
- Add database indexes to frequently filtered fields
- Keep dashboards responsive

DEMO PRESENTATION MODE
Create a “Demo Mode” or demo-friendly experience so the entire project can be shown in 5–10 minutes.

Suggested demo:
1. Login as Super Admin
2. Show dashboard
3. Open an undertrial case
4. Show case timeline
5. Show pending bail workflow
6. Show lawyer assignment
7. Show UTRC alert
8. Login as lawyer
9. Update hearing/bail status
10. Login as support person
11. Show authorized information
12. Show rehabilitation progress
13. Return to Super Admin
14. Show audit log

ADMIN FULL-RIGHTS DEMO
When logged in as Super Admin, ensure every administrative module is reachable from the sidebar and every CRUD workflow works.

Do NOT merely create buttons that do nothing. Every visible action should either work or show a meaningful implemented state.

FINAL ACCEPTANCE CRITERIA
The project is complete only when:
1. Frontend runs successfully.
2. Backend/API runs successfully.
3. Database migrations work.
4. Demo seed data loads successfully.
5. Demo accounts can log in.
6. Role-based access works.
7. Super Admin has full administrative rights.
8. Case management works.
9. Lawyer assignment works.
10. Bail workflow works.
11. Hearing tracking works.
12. Notifications work.
13. Rights-awareness module works.
14. Rehabilitation module works.
15. Support-person access works.
16. Dashboards display real seeded data.
17. Admin CRUD operations work.
18. Audit logs record important actions.
19. Responsive design works.
20. No major page contains fake non-functional controls.
21. README contains complete setup instructions.
22. The application is polished enough for a hackathon/project demonstration.

DEVELOPMENT APPROACH
Work systematically:
1. Inspect the environment.
2. Create project structure.
3. Implement backend models and authentication.
4. Implement migrations.
5. Implement APIs and permissions.
6. Implement seed/demo data.
7. Implement frontend layout and routing.
8. Implement role-specific dashboards.
9. Implement admin panel.
10. Connect frontend to APIs.
11. Add validation/error handling.
12. Add testing.
13. Run the application.
14. Fix build/runtime/API/database errors.
15. Verify every demo account and major workflow.
16. Finish with a clean README.

Do not stop after generating files. Actually run/build/test the application and fix errors.

FINAL OUTPUT FROM YOU
At the end, provide:
- Project folder structure
- Setup commands
- Run commands
- Demo login credentials
- Main implemented features
- API summary
- Database summary
- Testing summary
- Any limitations
- A short 5–10 minute demo script

MOST IMPORTANT:
Build a REAL, FUNCTIONAL, DEMO-READY application, not a static prototype.
Prioritize correctness, security, role-based access, case/bail tracking, legal-aid coordination, UTRC monitoring, rehabilitation, and the Super Admin panel.
