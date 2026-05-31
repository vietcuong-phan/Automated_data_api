# Automated Data API Platform

An end-to-end automated reporting platform built with Python, FastAPI, PostgreSQL, and React.  
The system automates daily SQL data processing pipelines and provides REST APIs for internal users to access and download reports without requiring manual support from the Data team.

---

# Project Overview

This project was developed to simulate a real-world internal data automation system used by operations and business teams.

The platform:

- Connects directly to a SQL database
- Automatically runs ETL pipelines
- Processes reporting data daily
- Exposes REST API endpoints
- Provides a React dashboard for internal users
- Supports CSV report downloads
- Uses Git/GitHub for version control

---

# System Architecture

```text
PostgreSQL Database
        ↓
Python ETL Pipeline
        ↓
FastAPI REST API
        ↓
React Frontend Dashboard
        ↓
Internal Users Download Reports
```

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pandas
- APScheduler

## Frontend

- React
- Axios

## Tools

- Git
- GitHub
- VS Code

---

# Features

## Data Automation

- Automated daily ETL pipeline
- SQL query execution
- Revenue calculations
- Aggregated reporting

## API System

- REST API endpoints
- Swagger API documentation
- CSV report download endpoint

## Frontend Dashboard

- React-based UI
- Report visualization
- Download CSV reports

## Scheduler

- Automated scheduled jobs using APScheduler

---

# Folder Structure

```text
automated-data-api/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   ├── scheduler/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── reports/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   └── public/
│
├── sql/
├── docs/
└── README.md
```

---

# Database Setup

## Create Database

```sql
CREATE DATABASE reporting_db;
```

---

## Create Sales Table

```sql
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    order_date DATE,
    product_name VARCHAR(255),
    category VARCHAR(100),
    quantity INT,
    price NUMERIC(10,2)
);
```

---

## Insert Sample Data

```sql
INSERT INTO sales (
    order_date,
    product_name,
    category,
    quantity,
    price
)
VALUES
('2026-05-01', 'Laptop', 'Electronics', 2, 1200),
('2026-05-01', 'Mouse', 'Accessories', 5, 25),
('2026-05-02', 'Keyboard', 'Accessories', 3, 80);
```

---

# Backend Setup

## Navigate to Backend

```bash
cd backend
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside `backend/`

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=reporting_db
DB_USER=postgres
DB_PASSWORD=yourpassword
```

---

# Run Backend Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

FastAPI automatically generates Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## Navigate to Frontend

```bash
cd frontend
```

---

## Install Dependencies

```bash
npm install
```

---

## Run React App

```bash
npm start
```

---

# Frontend URL

```text
http://localhost:3000
```

---

# API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Health check |
| `/reports/daily-sales` | GET | Get aggregated sales report |
| `/reports/download` | GET | Download CSV report |

---

# Sample API Response

```json
[
  {
    "category": "Accessories",
    "total_quantity": 8,
    "total_revenue": 365
  },
  {
    "category": "Electronics",
    "total_quantity": 2,
    "total_revenue": 2400
  }
]
```

---

# Scheduler Automation

The project uses APScheduler to automate ETL jobs.

Example:

```python
scheduler.add_job(
    generate_daily_sales_report,
    'cron',
    hour=7
)
```

---

# CSV Report Export

Generated reports are automatically stored in:

```text
backend/reports/
```

Example:

```text
daily_sales.csv
```

---

# Git Version Control

## Initialize Git

```bash
git init
```

---

## Commit Changes

```bash
git add .
git commit -m "Initial project setup"
```

---

## Push to GitHub

```bash
git push -u origin main
```

---

# Future Improvements

- JWT Authentication
- Docker Support
- CI/CD Pipeline
- Redis Cache
- Airflow Integration
- Power BI Integration
- Role-Based Access Control
- Cloud Deployment

---

# Screenshots

## FastAPI Swagger UI

_Add screenshot here_

---

## React Dashboard

_Add screenshot here_

---

# Business Value

This platform helps internal users:

- Access reports without contacting the Data team
- Download reports instantly
- Reduce manual reporting processes
- Improve reporting efficiency

---

# Skills Demonstrated

- Python Development
- FastAPI API Development
- SQL & PostgreSQL
- ETL/Data Pipeline Automation
- REST API Design
- React Frontend Development
- Scheduler Automation
- Git/GitHub Workflow

