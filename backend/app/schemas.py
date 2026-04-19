from pydantic import BaseModel
from typing import Optional 
from datetime import datetime


# Class - 1: 
class ActivityCreate(BaseModel):
    user_id: Optional[str]="default_user" 
    # By marking user_id as Optional[str], 
    # you are telling the program that a value for this field is not 
    # strictly required when a new object is created.
    url:str
    duration: float

  # ActivityCreate → “I receive clean JSON” → no config needed
  # ActivityResponse → “I receive messy objects” → config needed

class ActivtiyResponse(BaseModel):
    id:int
    user_id:str
    url:str
    domain:str
    duration: float
    category: str
    timestamp: datetime
         
    # Without Config → “I only understand JSON/dict”
    # With from_attributes=True → “I can also understand Python objects”
    class Config:
        form_attribute=True
    # Use Config (from_attributes) ONLY when working with ORM/database objects
    # Don’t use it for request models (unless special cases)    
  

class SiteCategoryCreate(BaseModel):
    domain: str
    category: str
# categorizes sites into neutral, productive, or distractive
    
class SiteCategoryResponse(BaseModel):
    id: int
    domain: str
    category: str
    is_custom: bool

    class Config:
        form_attribute=True


class FocusScoreResponse(BaseModel):
    focus_score: float
    productive_time: float
    distracting_time: float
    neutral_time: float
    total_time: float
    streak_days: int
    suggestions: str

def DomainStat(BaseModel):
    domain: str
    total_time: float
    category: str
    percentage: float

class DailyReportResponse(BaseModel):
    date: str
    total_time: float
    focus_score: float
    productive_time: float
    distracting_time: float
    neutral_time: float
    top_sites: list[DomainStat]
    hourly_activity: dict[int, float]  # hour (0-23) to total time spent in that hour

class WeeklyReportResponse(BaseModel):
    week_start: str
    week_end: str
    average_focus_score: float
    total_time: float
    daily_score: dict[str, float]  # date to focus score
    top_distracting_sites: list[DomainStat]
    