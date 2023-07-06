from fastapi import APIRouter

router = APIRouter()


@router.get("/employee/bookings")
def get_employee_bookings(employee_id: int):
    # Logic to fetch employee's bookings
    return {"employee_id": employee_id, "bookings": []}
