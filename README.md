# SkyDash ✈️

A full-stack aviation data explorer dashboard built with FastAPI, Vue 3, and PostgreSQL. SkyDash fetches live global flight data from the AviationStack API, persists it to a cloud database, and displays it through an interactive dashboard with real-time search, data visualization, and an interactive map.

---

## Live Demo
- **Frontend:** https://d3r43tijueh8sn.cloudfront.net
- **API:** http://skydash-backend-env.eba-zxgivwnm.us-east-1.elasticbeanstalk.com
- **API Docs:** http://skydash-backend-env.eba-zxgivwnm.us-east-1.elasticbeanstalk.com/docs

---

## Tech Stack

### Backend
- **Python 3.13** — core language
- **FastAPI** — REST API framework with automatic Swagger documentation
- **SQLAlchemy** — ORM for database interaction
- **Alembic** — database migration management
- **PostgreSQL** — relational database
- **httpx** — async HTTP client for AviationStack API integration
- **AviationStack API** — real-time flight data source

### Frontend
- **Vue 3** — progressive JavaScript framework
- **Pinia** — state management
- **Vue Router** — client-side routing
- **PrimeVue** — UI component library
- **Chart.js / vue-chartjs** — data visualization
- **Leaflet** — interactive mapping

### Cloud & DevOps
- **AWS RDS** — managed PostgreSQL hosting (db.t3.micro, free tier)
- **AWS Elastic Beanstalk** — backend API deployment with auto-scaling
- **AWS S3** — frontend static file hosting
- **AWS CloudFront** — global CDN with HTTPS for frontend delivery
- **GitHub Actions** — CI/CD pipeline

---

## Features

- 🌍 **Live Flight Data** — fetches real-time global aircraft data from AviationStack API
- 💾 **Data Persistence** — saves flight snapshots to PostgreSQL with timestamps
- 📊 **Country Chart** — bar chart showing top 10 airlines by active flight count
- 🗺️ **Interactive Map** — Leaflet map with clickable aircraft markers and flight details
- 🔍 **Real-time Search** — filter flights by callsign, ICAO24, or airline instantly
- 📋 **Flight History** — browse historically recorded flights from the database
- 🌙 **Dark Mode** — persistent dark/light theme toggle

---

## Architecture
```
AviationStack API
        │
        ▼
   FastAPI Backend  ──────────────────►  PostgreSQL (AWS RDS)
   (AWS Elastic Beanstalk)
        │
        ▼
   Vue 3 Frontend
   (AWS S3 + CloudFront)
        │
        ├── Live Dashboard (chart + map + table)
        └── History Page (database query)
```

---

## Getting Started

### Prerequisites
- Python 3.13+
- Node.js 18+
- PostgreSQL 17+
- Git

### Environment Variables

**Backend** — set these in your environment or AWS Elastic Beanstalk:
```
DATABASE_URL=postgresql://user:password@host:port/dbname
AVIATIONSTACK_KEY=your_aviationstack_api_key
```

**Frontend** — create a `.env.local` file in the `frontend` folder:
```
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/your-username/skydash.git
cd skydash/backend

# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start the development server
uvicorn main:app --reload
```

API available at `http://127.0.0.1:8000`
Swagger docs at `http://127.0.0.1:8000/docs`

### Frontend Setup
```bash
cd skydash/frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

Frontend available at `http://localhost:5173`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/flights/` | Fetch live flights from AviationStack and save to DB |
| GET | `/flights/history` | Query 100 most recent saved flights |

---

## Project Structure
```
skydash/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── database.py          # Database connection and session management
│   ├── requirements.txt     # Python dependencies
│   ├── Procfile             # Elastic Beanstalk startup command
│   ├── .ebextensions/       # Elastic Beanstalk configuration
│   ├── routers/
│   │   └── flights.py       # Flight API routes
│   ├── models/
│   │   ├── flight.py        # Pydantic model (API schema)
│   │   └── flight_model.py  # SQLAlchemy model (database schema)
│   ├── services/
│   │   └── opensky.py       # AviationStack API integration
│   └── migrations/          # Alembic database migrations
└── frontend/
    ├── src/
    │   ├── App.vue           # Root component
    │   ├── main.js           # App entry point
    │   ├── components/
    │   │   ├── NavBar.vue        # Navigation bar with dark mode toggle
    │   │   ├── CountryChart.vue  # Bar chart component
    │   │   └── FlightMap.vue     # Leaflet map component
    │   ├── views/
    │   │   ├── HomeView.vue      # Live dashboard page
    │   │   └── HistoryView.vue   # Flight history page
    │   ├── stores/
    │   │   ├── flights.js        # Pinia flight data store
    │   │   └── theme.js          # Pinia theme store
    │   └── router/
    │       └── index.js          # Vue Router configuration
    └── package.json
```

---

## Deployment

### Backend (AWS Elastic Beanstalk)
```bash
cd backend
eb deploy
```

### Frontend (AWS S3)
```bash
cd frontend
npm run build
aws s3 sync dist s3://skydash-frontend-daniel --delete
```

---

## Author

**Daniel Fijalka**
Junior Software Developer | MS Computer Science Student
Oklahoma Christian University

[GitHub](https://github.com/aklajifd) · [LinkedIn](https://www.linkedin.com/in/daniel-fijalka-989a6421b/)

---

## License

MIT License — feel free to use this project as a reference or starting point.