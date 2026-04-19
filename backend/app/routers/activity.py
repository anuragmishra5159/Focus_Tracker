from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..utils import extract_domain, classify_domain
from ..models import Activity, SiteCategory, ActivityLog
from app import crud, schemas
from ..database import get_db
from ..schemas import ActivityCreate, ActivtiyResponse, SiteCategoryCreate, SiteCategoryResponse, FocusScoreResponse, DailyReportResponse


router = APIRouter(
    prefix = "/activity",
    tags=["activity"]
)


#to send the data to the database and log the activity
@router.post("/", response_model=ActivtiyResponse)
def log_activity(activity: ActivityCreate, db: Session = Depends(get_db)):    
    domain = extract_domain(activity.url)
    custom_cats = {cat.domain: cat.category for cat in db.query(crud.SiteCategory).all()}
    category = classify_domain(domain, custom_cats)
    db_activity = ActivityLog(
        user_id = activity.user_id,
        url = activity.url,
        domain = domain,
        duration = activity.duration,
        category = category
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


# to get the activity logs for a user, with an optional limit on the number of logs returned
@router.get("/", response_model=[ActivtiyResponse])
def get_activity_logs(user_id : str = "default_user", limit: int = 50, db : Session = Depends (get_db)):
    logs = (
        db.query(ActivityLog).filter(ActivityLog.user_id==user_id).order_by(ActivityLog.timestamp.desc()).limit(limit).all()
    )
    return logs

#categories sites
@router.get("/sites", response_model = list[SiteCategory])
def get_site_categories(db: Session = Depends(get_db)):
    return db.query(SiteCategory).all()





@router.post("/sites", response_model=SiteCategoryResponse)
def set_site_category(site: SiteCategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(SiteCategory).filter(SiteCategory.domain == site.domain).first()
    if existing:
        existing.category = site.category
        db.commit()
        db.refresh(existing)
        return existing
    
    new_site = SiteCategory(domain=site.domain, category=site.category, is_custom=True)
    db.add(new_site)
    db.commit()
    db.refresh(new_site)
    return new_site


@router.delete("/sites/{domain}")
def delete_site_category(domain: str, db: Session = Depends(get_db)):
    site = db.query(SiteCategory).filter(SiteCategory.domain == domain).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site category not found")
    db.delete(site)
    db.commit()
    return {"detail": "Site category deleted"}
