from fastapi import FastAPI # type: ignore
from app.services.sales_pipeline import generate_daily_sales_report

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Automated Data API Running"}

@app.get("/reports/daily-sales")
def daily_sales():

    df = generate_daily_sales_report()

    return df.to_dict(orient="records")

from fastapi.responses import FileResponse # type: ignore

@app.get("/reports/download")
def download_report():

    file_path = "reports/daily_sales.csv"

    return FileResponse(
        path=file_path,
        filename="daily_sales.csv",
        media_type="text/csv"
    )

from app.scheduler.jobs import scheduler

from fastapi.middleware.cors import CORSMiddleware # type: ignore

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)