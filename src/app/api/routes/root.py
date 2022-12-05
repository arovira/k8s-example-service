import zoneinfo
from datetime import datetime
from enum import Enum

from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse

router = APIRouter()

success_status_code = 200


@router.get("/health", status_code=success_status_code)
def health():
    return {"status_code": f"{success_status_code}"}


@router.get("/", response_class=HTMLResponse)
def get_times_html():
    zones = ["America/New_York", "Europe/Berlin", "Asia/Tokyo"]
    res = ""
    for zone in zones:
        res += f"<h1>{zone}: {datetime.now(tz=zoneinfo.ZoneInfo(zone))}</h1>"

    return f"""
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
    <html>
        <head>
            <title>Times on the world</title>
        </head>
        <body>
            {res}
        </body>
    </html>
    """
