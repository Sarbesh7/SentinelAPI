# 🛡️ SentinelAPI

> **Incident Reporting & Emergency Response Backend System**  
> A scalable REST API built with Django and Django REST Framework for reporting, managing, and responding to incidents with enterprise-grade role-based access control.

![Django](https://img.shields.io/badge/Django-6.0-darkgreen)
![DRF](https://img.shields.io/badge/DRF-3.14+-blue)
![JWT](https://img.shields.io/badge/JWT-Authentication-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Quick Navigation

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [User Roles](#-user-roles)
- [Installation](#-installation)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Authentication](#-authentication)
- [Usage Examples](#-usage-examples)

---

## 🚀 Features

### 🔐 Authentication & Security
- JWT Authentication with access & refresh tokens
- User registration with automatic profile creation
- Password hashing with Django's built-in validators
- Role-based access control (RBAC)
- Session management

### 👥 Role-Based System
- **Citizen** → Report incidents & track their status
- **Responder** → Investigate & update assigned incidents
- **Admin** → Full system control & user management

### 🚨 Incident Management
- Complete CRUD operations (Create, Read, Update, Delete)
- Incident categorization (Accident, Harassment, Fire, Cyber Abuse, Emergency, Other)
- Priority levels (Low, Medium, High)
- Status workflow (Pending → Investigating → Resolved/Rejected)
- Media attachments (images & videos)
- Location tracking
- Automatic reporter capture

### 📂 Media & File Management
- Image upload with validation
- Video/media upload support
- Organized storage in `incident_images/` and `incident_videos/`
- Automatic file organization

### 🔍 Advanced Filtering & Search
- Filter by status, category, and priority
- Full-text search by title and description
- Custom ordering options
- Pagination (5 items per page)
- Query parameter filtering

### 🔔 Notification System
- Auto-notifications on incident creation
- Mark notifications as read
- Notification deletion
- Chronological ordering
- User-specific notification queries

### 📊 Dashboard & Analytics
- **Citizen Dashboard** - Track own incidents with statistics
- **Responder Dashboard** - View assigned incidents and workload
- **Admin Dashboard** - Global incident overview with full control
- Real-time statistics (pending count, resolved count, total incidents)

### 👤 User Profile Management
- **Citizen Profile** - Address, emergency contact, date of birth
- **Responder Profile** - Department, badge number
- Auto-profile creation on user registration
- Profile cleanup on role changes

---

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Django** | Web Framework | 6.0 |
| **Django REST Framework** | API Toolkit | 3.14+ |
| **SimpleJWT** | JWT Authentication | Latest |
| **drf-spectacular** | API Documentation | Latest |
| **django-filter** | Advanced Filtering | Latest |
| **Pillow** | Image Processing | Latest |
| **SQLite** | Database (Development) | Built-in |
| **PostgreSQL** | Database (Production) | Optional |

---

## 👥 User Roles & Permissions

### 🟦 Citizen
- Report new incidents
- View only their own incidents
- Update/delete their own incidents
- Access citizen dashboard
- Receive status change notifications

### 🟩 Responder
- View all incidents
- Update assigned incidents
- Change incident status
- Access responder dashboard
- Track assigned workload

### 🟥 Admin
- Full access to all incidents
- Create/update/delete any incident
- Manage users and roles
- Access admin dashboard
- Global system control
- User role assignment

---

## 📡 Core API Endpoints

### Authentication
```
POST   /api/register/              → User registration
POST   /api/login/                 → User login
POST   /api/token/refresh/         → Refresh JWT token
GET    /api/profile/               → Get user profile
```

### Incidents
```
GET    /api/incident/              → List all incidents (with filters)
POST   /api/incident/              → Create new incident
GET    /api/incident/<id>/         → Get incident details
PUT    /api/incident/<id>/         → Update incident
DELETE /api/incident/<id>/         → Delete incident
```

### Notifications
```
GET    /api/notifications/         → Get user notifications
POST   /api/notifications/         → Create notification
PATCH  /api/notifications/<id>/    → Mark as read
DELETE /api/notifications/<id>/    → Delete notification
```

### Dashboards
```
GET    /api/citizen-dashboard/     → Citizen dashboard
GET    /api/responder-dashboard/   → Responder dashboard
GET    /api/admin-dashboard/       → Admin dashboard
```

### Admin Management
```
GET    /api/admin/users/           → List all users
GET    /api/admin/users/<id>/      → Get user details
PUT    /api/admin/users/<id>/      → Update user role
```

### API Documentation
```
GET    /api/docs/                  → Swagger UI
GET    /api/redoc/                 → ReDoc Documentation
GET    /api/schema/                → OpenAPI Schema
```

---

## 🔐 Authentication

### JWT Token Flow

SentinelAPI uses stateless JWT authentication for secure API access.

**1. Register**
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "role": "citizen"
  }'
```

**Response:**
```json
{
    "user": {"id": 1, "username": "johndoe", "email": "john@example.com", "role": "citizen"},
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**2. Login**
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "password": "securepassword123"}'
```

**3. Use Token**

Include the access token in every request:
```bash
Authorization: Bearer <access_token>
```

**4. Refresh Token**

When access token expires:
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "<refresh_token>"}'
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/Sarbesh7/SentinelAPI.git
cd SentinelAPI/sentinel_api
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Database
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

API available at: **http://localhost:8000**  
Swagger UI: **http://localhost:8000/api/docs/**

---

## 📁 Project Structure

```
SentinelAPI/
├── sentinel_api/                 # Django Project Root
│   ├── db.sqlite3               # Development Database
│   ├── manage.py                # Django Management
│   │
│   ├── sentinel_api/            # Project Settings
│   │   ├── settings.py          # Configuration
│   │   ├── urls.py              # URL Router
│   │   ├── asgi.py              # ASGI Config
│   │   └── wsgi.py              # WSGI Config
│   │
│   ├── accounts/                # Authentication & Profiles
│   │   ├── models.py            # User, CitizenProfile, ResponderProfile
│   │   ├── views.py             # Auth & Profile Views
│   │   ├── serializers.py       # Serializers
│   │   ├── signals.py           # Auto-Profile Creation
│   │   ├── urls.py              # Routes
│   │   └── migrations/
│   │
│   ├── incidents/               # Incident Management
│   │   ├── models.py            # Incident Model
│   │   ├── views.py             # CRUD Views
│   │   ├── serializers.py       # Serializers
│   │   ├── urls.py              # Routes
│   │   └── migrations/
│   │
│   ├── notifications/           # Notification System
│   │   ├── models.py            # Notification Model
│   │   ├── views.py             # Notification Views
│   │   ├── serializers.py       # Serializers
│   │   ├── signals.py           # Auto-Notifications
│   │   ├── urls.py              # Routes
│   │   └── migrations/
│   │
│   ├── core/                    # Dashboards & Admin
│   │   ├── views.py             # Dashboard Views
│   │   ├── urls.py              # Routes
│   │   └── migrations/
│   │
│   ├── responses/               # Response Management
│   │   └── models.py
│   │
│   └── media/                   # Uploaded Files
│       ├── incident_images/
│       └── incident_videos/
│
├── requirements.txt             # Dependencies
├── README.md                    # Documentation
└── CODE_REVIEW_ANALYSIS.md      # Code Review Report
```

---

## 💡 Usage Examples

### 1️⃣ Create an Incident
```bash
curl -X POST http://localhost:8000/api/incident/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Traffic Accident",
    "description": "Two vehicle collision",
    "location": "Main Street",
    "category": "accident",
    "priority": "high"
  }'
```

### 2️⃣ List Incidents with Filters
```bash
# Filter by category
curl -X GET 'http://localhost:8000/api/incident/?category=accident' \
  -H "Authorization: Bearer <token>"

# Search by title
curl -X GET 'http://localhost:8000/api/incident/?search=accident' \
  -H "Authorization: Bearer <token>"

# Pagination
curl -X GET 'http://localhost:8000/api/incident/?page=2' \
  -H "Authorization: Bearer <token>"
```

### 3️⃣ Upload Incident with Media
```bash
curl -X POST http://localhost:8000/api/incident/ \
  -H "Authorization: Bearer <token>" \
  -F "title=House Fire" \
  -F "description=Large residential fire" \
  -F "location=Oak Lane" \
  -F "category=fire" \
  -F "priority=high" \
  -F "images=@/path/to/image.jpg" \
  -F "videos=@/path/to/video.mp4"
```

### 4️⃣ Get Citizen Dashboard
```bash
curl -X GET http://localhost:8000/api/citizen-dashboard/ \
  -H "Authorization: Bearer <citizen_token>"
```

### 5️⃣ Update Incident (Responder)
```bash
curl -X PUT http://localhost:8000/api/incident/1/ \
  -H "Authorization: Bearer <responder_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "in_progress",
    "priority": "high"
  }'
```

### 6️⃣ Get Notifications
```bash
curl -X GET http://localhost:8000/api/notifications/ \
  -H "Authorization: Bearer <token>"
```

### 7️⃣ Mark Notification as Read
```bash
curl -X PATCH http://localhost:8000/api/notifications/1/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"is_read": true}'
```

---

## 🎨 Response Status Codes

| Code | Status | Meaning |
|------|--------|---------|
| 200 | OK | Successful request |
| 201 | Created | Resource created |
| 204 | No Content | Successful deletion |
| 400 | Bad Request | Invalid data |
| 401 | Unauthorized | Missing/invalid token |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 500 | Server Error | Internal error |

---

## 📊 Incident Categories

- 🚗 **Accident** - Traffic accidents, collisions
- 🤐 **Harassment** - Physical or verbal harassment
- 🔥 **Fire** - Fire emergencies
- 💻 **Cyber Abuse** - Online harassment, hacking
- ⚠️ **Emergency** - Medical, natural disaster
- ❓ **Other** - Miscellaneous incidents

---

## 🔄 Signal Hooks (Background Tasks)

### Auto-Profile Creation
When a user registers, Django signals automatically create:
- `CitizenProfile` for citizens
- `ResponderProfile` for responders
- Admin flag for admins

### Auto-Notifications
When an incident is created, a notification is automatically sent to the reporter.

---

## 🧪 Testing with Swagger UI

1. Go to: **http://localhost:8000/api/docs/**
2. Click **"Authorize"** button
3. Paste your JWT access token
4. Test endpoints directly from the UI

---

## 🚀 Production Deployment

### Deployment Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Use PostgreSQL instead of SQLite
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Setup HTTPS/SSL
- [ ] Configure S3 for media storage
- [ ] Setup environment variables
- [ ] Enable CSRF protection
- [ ] Configure email backend
- [ ] Setup logging & monitoring

### Environment Variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:pass@localhost:5432/sentinelapi
MEDIA_ROOT=/path/to/media
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)

---

## 👨‍💻 Author

**Sarbesh Adhikari**
- GitHub: [@Sarbesh7](https://github.com/Sarbesh7)
- Project: [SentinelAPI](https://github.com/Sarbesh7/SentinelAPI)

---

## 🎯 Project Goal

This project demonstrates backend engineering excellence, including:
- ✅ JWT authentication & security
- ✅ Role-based access control (RBAC)
- ✅ Clean API design with proper HTTP standards
- ✅ Database relationships & migrations
- ✅ Django signals for background tasks
- ✅ Scalable architecture
- ✅ Production-ready code

---

<div align="center">

**Made with ❤️ by Sarbesh Adhikari**

⭐ If this project helped you, please consider giving it a star!

[View on GitHub](https://github.com/Sarbesh7/SentinelAPI) • [Report Issue](https://github.com/Sarbesh7/SentinelAPI/issues) • 
</div>
