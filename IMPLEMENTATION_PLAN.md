# NyayaSetu — Implementation Plan

Based on `NyayaSetu_Antigravity_Master_Prompt.md`

---

## 1. Project Architecture

| Layer | Implementation |
|-------|----------------|
| **Frontend** | React 19 + TypeScript + Vite + Tailwind CSS 4 + React Router 7 + Recharts + Axios |
| **Backend** | Django 6 + Django REST Framework + SimpleJWT |
| **Database** | SQLite (dev/demo); PostgreSQL via `DATABASE_URL` (production) |
| **API** | REST JSON under `/api/` with JWT Bearer auth |
| **Authentication** | JWT access/refresh tokens; email-based login |
| **Authorization** | Role-based access control (7 roles) enforced on backend + frontend route guards |
| **File Storage** | Local mock storage with metadata in `Document` model |
| **Deployment** | Django serves built React SPA from `frontend/dist`; optional split dev servers |

---

## 2. Technology Stack

- **Frontend:** React, TypeScript, Tailwind CSS, React Router, Recharts, Lucide icons, Axios
- **Backend:** Django, DRF, django-filter, django-cors-headers, SimpleJWT
- **Database:** SQLite (default dev), PostgreSQL (production via env)
- **Testing:** Django TestCase for backend RBAC/auth; frontend lint via oxlint

---

## 3. Complete Feature Breakdown

| Module | Implementation |
|--------|----------------|
| Case Management | `Case`, `Hearing`, `Document` models; CRUD API with RBAC filtering; timeline UI |
| Legal Aid Matching | `LawyerProfile`, `LegalAidOrganization`; filter by specialization/location/language |
| Bail Assistance | `BailApplication` workflow; status tracking; review alerts |
| Court Timeline | `CaseTimelineStepper` component; hearing history |
| Rights Awareness | `LegalResource` CRUD; categories; disclaimer |
| Rehabilitation | `RehabilitationProgram`, `RehabilitationEnrollment`; progress tracking |
| Support Person Portal | Scoped dashboard via `SupportPersonProfile` linkage |
| UTRC Dashboard | Analytics charts; case review panel; priority alerts |
| Notifications | In-app `Notification` model; read/archived states; triggers on updates |
| Analytics & Reports | `/api/analytics/` endpoints; CSV export on Reports page |
| Super Admin Panel | 18 admin modules with CRUD, search, filter, pagination |
| Audit Logs | Read-only API; auto-logging on admin actions |

---

## 4. User Roles & Permissions

| Role | Access |
|------|--------|
| **SUPER_ADMIN** | Full CRUD on all resources; analytics; audit logs; system settings |
| **UTRC_AUTHORITY** | View/manage cases in jurisdiction; assign legal aid; reports; UTRC dashboard |
| **LAWYER** | Assigned cases only; update hearings/bail; upload documents |
| **PRISON_AUTHORITY** | Undertrials in assigned prison; custody updates; rehab participation |
| **SUPPORT_PERSON** | Connected undertrial's case status, hearings, bail, approved docs only |
| **UNDERTRIAL** | Own case, hearings, bail, rights resources, rehab, notifications |
| **REHAB_STAFF** | Assigned enrollments; program management; attendance/progress |

---

## 5. Database Design

### Core Models (implemented)

- **User** — email (unique), role, phone, is_active, timestamps
- **Prison** — name, location, capacity
- **UTRC** — name, jurisdiction
- **UndertrialProfile** — user FK, prison FK, prisoner_number
- **SupportPersonProfile** — user FK, undertrial FK, relationship
- **Court** — name, location, court_type
- **LegalAidOrganization** — name, location, contact
- **LawyerProfile** — user FK, org FK, bar_license, specialization, languages, availability
- **Case** — fir_number, case_number, undertrial, court, status, priority, assigned_lawyer, utrc, dates
- **Hearing** — case FK, hearing_date, purpose, outcome, next_hearing_date
- **BailApplication** — case FK, status, lawyer, hearing_date, decision
- **Document** — case FK, title, document_type, file_url, uploaded_by
- **LegalResource** — title, category, explanations, language, is_published, last_reviewed_date
- **RehabilitationProgram** — name, program_type, provider, dates, is_active
- **RehabilitationEnrollment** — program FK, undertrial FK, status, attendance_rate
- **Notification** — user FK, title, message, is_read, is_archived
- **AuditLog** — user, action, module, record_id, details, ip_address, timestamp
- **SystemSetting** — key, value, description

### Indexes
- Case: status, priority, undertrial_id, assigned_lawyer_id
- Hearing: hearing_date, case_id
- Notification: user_id, is_read

---

## 6. API Design

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Login (email + password) → JWT |
| POST | `/api/token/refresh/` | Refresh access token |
| POST | `/api/auth/password-reset/` | Demo password reset |
| POST | `/api/auth/change-password/` | Change password (authenticated) |

### Resources (ViewSets under `/api/`)
- users, prisons, utrcs, undertrials, support-persons, notifications, audit-logs, system-settings
- cases/cases, cases/hearings, cases/bail-applications, cases/documents, cases/courts
- legal-aid/lawyers, legal-aid/organizations, legal-aid/resources
- rehab/programs, rehab/enrollments

### Analytics
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/analytics/dashboard/` | Role-scoped dashboard stats |
| GET | `/api/analytics/cases-by-status/` | Chart data |
| GET | `/api/analytics/bail-stats/` | Bail workflow distribution |
| GET | `/api/analytics/reports/{type}/` | Exportable report data |

All endpoints require JWT except token obtain. Permissions enforced per role.

---

## 7. Frontend Pages

| Page | Route | Roles |
|------|-------|-------|
| Landing | `/home` | Public |
| Login | `/login` | Public |
| Forgot Password | `/forgot-password` | Public |
| Dashboard | `/dashboard` | All (role-specific content) |
| Cases | `/cases` | Authorized roles |
| Case Detail | `/cases/:id` | Authorized |
| Documents | `/documents` | Authorized |
| Bail Applications | `/bail` | Authorized |
| Legal Aid | `/legal-aid` | Authorized |
| Rehabilitation | `/rehab` | Authorized |
| UTRC Review | `/utrc` | UTRC, Admin |
| Rights Awareness | `/rights` | All authenticated |
| Reports | `/reports` | UTRC, Admin |
| Notifications | `/notifications` | All |
| Profile | `/profile` | All |
| Admin Users | `/admin/users` | Super Admin |
| Admin Prisons/Courts/UTRCs | `/admin/*` | Super Admin |
| Admin Settings | `/admin/settings` | Super Admin |
| Audit Logs | `/admin/audit-logs` | Super Admin |
| 403 / 404 | `/403`, `*` | Public |

---

## 8. Backend Modules

- `backend_core/` — settings, urls, wsgi
- `users/` — auth, RBAC, profiles, notifications, audit, settings
- `cases/` — cases, hearings, bail, documents, courts
- `legal_aid/` — lawyers, organizations, resources
- `rehab/` — programs, enrollments
- `analytics/` — dashboard stats and reports (new app or views module)

---

## 9. Admin Panel

Super Admin sidebar with: Dashboard, Users, Prisons, Courts, UTRCs, Audit Logs, System Settings + shared module pages for Cases, Bail, Legal Aid, Rehab, Rights, Documents, Reports.

Each table: search, filter, pagination, CRUD with confirmation dialogs and audit logging.

---

## 10. Implementation Phases

### Phase 1 — Foundation (Complete)
- Django project, models, migrations, basic CRUD APIs, React scaffold

### Phase 2 — Security & RBAC (Current)
- Permission classes on all viewsets
- Object-level queryset filtering
- Frontend role-based navigation
- Audit logging middleware

### Phase 3 — Data & Workflows
- Expanded seed_demo command
- Notification triggers
- Bail review alerts
- Password reset flow

### Phase 4 — Dashboards & Analytics
- Role-specific dashboards
- Recharts integration
- Reports API

### Phase 5 — Polish & Documentation
- Tests, README, .env.example, FINAL_AUDIT.md
- Build verification

---

## 11. Testing Strategy

- **Auth tests:** login, invalid credentials, token refresh
- **RBAC tests:** undertrial isolation, support person scope, lawyer assigned cases only
- **Workflow tests:** case creation, bail status update, hearing scheduling
- **Admin tests:** super admin full access, non-admin blocked from settings
- **Frontend:** lint pass, production build

---

## 12. Definition of Done

1. All 22 acceptance criteria from master prompt met
2. Demo accounts login successfully
3. Seed data meets minimum counts and 10 demo scenarios
4. RBAC enforced on backend and frontend
5. No fake/non-functional primary actions
6. README with setup, credentials, API overview
7. IMPLEMENTATION_PLAN.md and FINAL_AUDIT.md complete
8. Backend tests pass; frontend builds without errors
9. Application runs on single Django server at port 8000
