from fastapi import APIRouter

router = APIRouter()


@router.get("/employee/salary")
def get_employee_salary(employee_id: int):
    # Logic to fetch employee's salary
    return {"employee_id": employee_id, "salary": 0}

