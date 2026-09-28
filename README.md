# Best Cars Dealership — Full-Stack Capstone Project

A full-stack web application for **Best Cars Dealership**, a national car retailer in the U.S., built as the IBM Full-Stack Developer Professional Certificate Capstone Project.

## Project Overview

This application allows users to:
- Browse national car dealership branches
- View dealer reviews with sentiment analysis
- Submit their own dealership reviews
- Manage their account (register, login, logout)

## Technology Stack

| Layer | Technology |
|---|---|
| **Frontend** | React.js, Bootstrap 5 |
| **Backend (Web)** | Django 4.x, Python 3.x |
| **Backend (Data)** | Node.js, Express.js, MongoDB |
| **Microservice** | Flask, NLTK (Sentiment Analysis) |
| **Database** | SQLite (Django), MongoDB (reviews/dealers) |
| **CI/CD** | GitHub Actions |
| **Deployment** | Docker, IBM Cloud Code Engine |

## Project Structure

```
├── server/
│   ├── djangoapp/           # Django application
│   │   ├── models.py        # CarMake, CarModel models
│   │   ├── views.py         # All API view functions
│   │   ├── restapis.py      # REST API helpers
│   │   ├── admin.py         # Admin panel configuration
│   │   ├── urls.py          # URL patterns
│   │   ├── populate.py      # Database seed data
│   │   └── microservices/   # Flask sentiment analyzer
│   │       └── app.py
│   ├── djangoproj/          # Django project settings
│   ├── frontend/            # React frontend
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── Dealers/     # Dealers list, detail, post review
│   │   │   │   ├── Login/       # Login page
│   │   │   │   ├── Register/    # Registration page
│   │   │   │   └── Header/      # Navigation header
│   │   └── static/          # Static HTML pages
│   │       ├── About.html
│   │       ├── Contact.html
│   │       └── Home.html
│   └── database/            # Node.js/MongoDB backend
│       ├── app.js           # Express API server
│       ├── dealership.js    # Mongoose Dealership model
│       ├── review.js        # Mongoose Review model
│       └── data/            # Seed JSON data
│           ├── dealerships.json
│           └── reviews.json
└── .github/
    └── workflows/
        └── linting.yml      # CI/CD GitHub Actions
```

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### 2. Django Backend

```bash
cd server
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3. Node.js / MongoDB Backend

```bash
cd server/database
npm install
# Start with Docker Compose (recommended):
docker-compose up -d
# Or run locally (requires MongoDB running on port 27017):
node app.js
```

### 4. Flask Sentiment Microservice

```bash
cd server/djangoapp/microservices
pip install -r requirements.txt
python -m nltk.downloader vader_lexicon
flask run --port=5050
```

### 5. React Frontend

```bash
cd server/frontend
npm install
npm run build
```

## API Endpoints

### Django (port 8000)
| Method | Endpoint | Description |
|---|---|---|
| POST | `/djangoapp/login` | User login |
| GET | `/djangoapp/logout` | User logout |
| POST | `/djangoapp/register` | User registration |
| GET | `/djangoapp/get_dealers` | Get all dealerships |
| GET | `/djangoapp/get_dealers/<state>` | Get dealers by state |
| GET | `/djangoapp/dealer/<id>` | Get dealer details |
| GET | `/djangoapp/reviews/dealer/<id>` | Get dealer reviews |
| POST | `/djangoapp/add_review` | Post a review |
| GET | `/djangoapp/get_cars` | Get all car makes/models |

### Node.js Backend (port 3030)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/fetchDealers` | Fetch all dealers |
| GET | `/fetchDealers/<state>` | Fetch dealers by state |
| GET | `/fetchDealer/<id>` | Fetch dealer by ID |
| GET | `/fetchReviews` | Fetch all reviews |
| GET | `/fetchReviews/dealer/<id>` | Fetch reviews by dealer |
| POST | `/insert_review` | Insert a new review |

### Flask Sentiment Service (port 5050)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/analyze/<text>` | Analyze sentiment of text |

## Features

- ✅ User Registration, Login, and Logout
- ✅ Dealers listing with state filtering
- ✅ Dealer detail pages with customer reviews
- ✅ Sentiment analysis (Positive / Neutral / Negative) on reviews
- ✅ Post reviews with car make, model, and year
- ✅ Django admin panel for car inventory management
- ✅ Responsive UI with Bootstrap 5
- ✅ GitHub Actions CI/CD pipeline

## License

This project is part of the IBM Full-Stack Developer Professional Certificate program on Coursera.