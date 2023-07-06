from fastapi import APIRouter

router = APIRouter()


@router.get("/manager/staff")
def get_staff_info():
    # Logic to fetch staff information
    return {"staff": []}
