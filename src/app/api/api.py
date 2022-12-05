import zoneinfo
from datetime import datetime
from enum import Enum

from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse

router = APIRouter()


class Timezone(str, Enum):
    _ignore_ = "Timezone z"
    Timezone = vars()
    for z in zoneinfo.available_timezones():
        Timezone[z] = z


@router.get("/get_time")
def get_utc_time(zone: Timezone = Query(Timezone.UTC)):
    return {zone: datetime.now(tz=zoneinfo.ZoneInfo(zone))}


@router.get("/get_all_times")
def get_all_times():
    res = {}
    for zone in sorted(zoneinfo.available_timezones()):
        res[f"{zone}"] = f"{datetime.now(tz=zoneinfo.ZoneInfo(zone))}"

    return res
