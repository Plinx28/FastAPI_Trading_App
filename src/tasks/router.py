from fastapi import APIRouter, BackgroundTasks, Depends

from src.tasks.tasks import send_email_report_dashboard
from src.auth.base_config import current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
    )


@router.get("/msgToEmail")
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    # The next comment is the second way to implement this feature:
    # background_tasks.add_task(send_email_report_dashboard, user.username)

    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": f"Mail was sent. Hello 1 2 3 ??...{current_user}",
        "details": None
    }