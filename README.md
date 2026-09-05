# NyayaSetu (न्यायसेतु)

**Digital Justice & Undertrial Rehabilitation Platform**  
*Bridging the Gap Between Justice, Legal Aid, and Access for Undertrials in India.*

---

## One-Click Launch Options (Windows)

You can launch the platform instantly using any of the included batch scripts in the project root:

1. **`setup_and_run.bat`** (Interactive Launcher)
   - Automatically checks and sets up Python venv, installs dependencies, verifies Node.js, compiles the React build, runs database migrations, seeds rich demo accounts, and provides an interactive choice menu.
2. **`run_prod.bat`** (Unified Server Mode)
   - Launches single unified server where Django serves the React production build and REST APIs on [http://127.0.0.1:8000](http://127.0.0.1:8000).
3. **`run_dev.bat`** (Full Development Mode)
   - Launches Vite with live Hot Module Replacement (HMR) on [http://localhost:5173](http://localhost:5173) and Django REST API on [http://127.0.0.1:8000](http://127.0.0.1:8000) in separate console windows.

---

## Role-Based Demo Login Credentials

The database comes pre-seeded with specialized accounts and demo datasets for every persona:

| Role | Email | Password | Primary Functions & Modules |
| :--- | :--- | :--- | :--- |
| **Super Admin** | `admin@nyayasetu.demo` | `Admin@12345` | Platform configuration, User management, Prisons/Courts/UTRCs, Audit logs |
| **UTRC Authority** | `utrc@nyayasetu.demo` | `Utrc@12345` | UTRC quarterly review panel, Sec 436A CrPC / BNSS 479 over-detention release review |
| **Defense Lawyer** | `lawyer@nyayasetu.demo` | `Lawyer@12345` | Criminal defense, FIR tracking, Bail drafting & hearings, Client representation |
| **Human Rights Adv** | `lawyer2@nyayasetu.demo` | `Lawyer@12345` | Human rights defense, UTRC representation, Compromise drafting |
| **DLSA Panel Counsel**| `lawyer3@nyayasetu.demo` | `Lawyer@12345` | District Legal Services Authority defense counsel & interim bail petitions |
| **Prison Authority** | `prison@nyayasetu.demo` | `Prison@12345` | Facility custody records, Inmate admission dates, FIR copies & remand records |
| **Rehabilitation Staff**| `rehab@nyayasetu.demo` | `Rehab@12345` | Digital literacy, Vocational skill courses, Counseling programs, Attendance tracking |
| **Undertrial (Theft)** | `undertrial@nyayasetu.demo`| `Undertrial@12345` | Case FIR-2024-001, Assigned Adv. Aarav Mehta, Bail filing, Digital literacy course |
| **Undertrial (Assault)**| `undertrial2@nyayasetu.demo`| `Undertrial@12345`| Case FIR-2025-102, Assigned Adv. Sneha Reddy, Life skills counseling |
| **Support Person** | `support@nyayasetu.demo` | `Support@12345` | Family support view for brother Imran Khan |

---

## Key Modules & Features

1. **Interactive Dashboard**: Real-time metrics for active cases, pending bail applications, legal counsel rosters, and rehab initiatives.
2. **Case Directory & 9-Stage Visual Stepper**: End-to-end case tracking through Arrest, Registration, Legal Aid Request, Lawyer Assignment, Bail Application, Hearings, Judicial Decision, Rehabilitation, and Reintegration.
3. **Bail Application Tracker**: Filing and monitoring Regular, Interim, Anticipatory, and Section 436A statutory relief applications.
4. **UTRC Review Panel**: Automated custody duration monitoring with flags for undertrials eligible for personal bond release under Section 436A CrPC / Section 479 BNSS.
5. **Legal Aid & Advocates Directory**: Roster of certified pro bono and DLSA defense counsels with bar licenses, specializations, and availability status.
6. **Rehabilitation & Skill Initiatives**: Multi-track programs (Digital Literacy, Tailoring, Electrical Repair, Mental Health Counseling, Legal Rights) with student enrollment records and attendance tracking.
7. **Legal Document Vault**: Secure repository for FIRs, court orders, bail petitions, and custody certificates.
8. **Rights & Legal Awareness Hub**: Plain-language legal guides explaining Article 39A, D.K. Basu arrest safeguards, and bail rules.
9. **Reports & Analytics Export**: Exportable CSV reports for case summaries, bail workflows, legal aid rosters, and rehab enrollments.
10. **System Administration**: Full management of Users, Prisons, Courts, UTRC entities, Platform Settings, and Security Audit Trails.

---

## Technical Stack

- **Backend**: Python 3.10+, Django 6.x, Django REST Framework, SimpleJWT (Token Auth), SQLite (Zero-config).
- **Frontend**: React 18, TypeScript, Tailwind CSS, Lucide Icons, Vite.
- **Architecture**: Decoupled RESTful architecture with unified production serving capability.

---

## Legal & Ethical Disclaimer
*This platform provides administrative and informational workflow support and does not replace professional legal representation or official judicial decision-making. All sample data generated via `seed_demo` is fictional and used strictly for demonstration and testing purposes.*