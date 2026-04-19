from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..utils.focus_utils import calculate_focus_score, generate_suggestions
from ..schemas import FocusScoreResponse
from ..database import get_db
from datetime import date, timedelta
from ..models import  ActivityLog, UserStreak
from collections import defaultdict

router = APIRouter(
    prefix = "/focus-score",tags=["focus-score"]
)

def update_streak(db: Session, user_id: str, today_score: float) -> int:
    streak =  db.query(UserStreak).filter(UserStreak.user_id == user_id).first()
    today_str= str(date.today())
    yesterday_str = str(date.today() - timedelta(days=1)) 

    if not streak:
        streak = UserStreak(user_id = user_id, streak_days = 0, last_focus_days= None) #last_focus_days is a comma separated string of dates when the user had a focus score above the threshold
        db.add(streak)
    
    # to set benchmark for the user, we want to give them a few days to build up their streak before we start counting it
    if today_score >= 70: # Assuming 70 is the threshold for a "good" focus score
        if streak.last_focus_date == today_str: # when the user has already had a good focus score today, we don't want to increment the streak again
            pass  # Already counted today
        elif streak.last_focus_date == yesterday_str: # when the user had a good focus score yesterday, we want to continue the streak
            streak.streak_days += 1 # Continue the streak
            streak.last_focus_date = today_str # Update the last focus date
        else: # when the user had a good focus score before yesterday, we want to reset the streak
            streak.streak_days = 1 # Reset the streak to 1 since they have a good focus score today
            streak.last_focus_date = today_str # Update the last focus date
    
    else: # when the user doesn't have a good focus score today, we want to reset the streak
        if streak.last_focus_date != today_str: # Only reset if they haven't already had a good focus score today
            pass  # Don't reset if they already had a good focus score today
        else:
            streak.streak_days = 0 # Reset the streak to 0 since they don't have a good focus score today
            streak.last_focus_date = today_str # Update the last focus date

#save the streak to the database
    db.commit()
    db.refresh(streak)
    return streak.streak_days

@router.get("/{user_id}", response_model=FocusScoreResponse) # to get the focus score for a user, we will calculate it based on the activity logs for the user for the current day
def get_focus_score(user_id: str, db: Session = Depends(get_db)): # we will calculate the focus score based on the activity logs for the user for the current day
    today = date.today()
    logs = (
        db.query(ActivityLog)       # get all activity logs for the user for the current day and calculate the focus score based on the duration of the activities and the category of the activities
        .filter(
            ActivityLog.user_id == user_id,
            func.date(ActivityLog.timestamp) == today
        ).all()
    )

    productive = sum(l.duration for l in logs if l.category == "productive")
    distracting = sum(l.duration for l in logs if l.category == "distracting")
    neutral = sum(l.duration for l in logs if l.category == "neutral")

    total = productive + distracting + neutral
    score = calculate_focus_score(productive, total)


    # for distractive sites: 
    distracting_sites = defaultdict(float)
    for log in logs:
        if log.category == "distracting":
            distracting_sites[log.domain] += log.duration
    
    top_distracting_sites = sorted(distracting_sites.keys(), key = lambda d: distracting_sites[d], reverse= True)  # sort the distracting sites based on the total duration spent on them, in descending order
                                                                                   # lambda function to sort the distracting sites based on the total duration spent on them, in descending order
    
    streak_days = update_streak(db, user_id, score) # update the user's streak based on their focus score for the day
    suggestions = generate_suggestions(score, distracting,top_distracting_sites, streak_days) 


    return FocusScoreResponse(
        focus_score = score,
        productive_time = productive,
        neutral_time= neutral,
        distracting_time = distracting,
        total_time= total,
        streak_days= streak_days,
        suggestions = suggestions
    )