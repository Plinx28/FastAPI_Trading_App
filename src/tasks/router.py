from fastapi import APIRouter, BackgroundTasks, Depends

from src.tasks.tasks import send_email_report_dashboard
from src.auth.base_config import current_user

router = APIRouter(
    prefix="/message",
    tags=["Messages"]
    )


@router.get("/testMessage")
def get_dashboard_report(background_tasks : BackgroundTasks, user=Depends(current_user)):
    # background_tasks.add_task(send_email_report_dashboard, user.username)
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": f"Mail was sent. Hello 1 2 3 ??...{current_user}",
        "details": None
    }