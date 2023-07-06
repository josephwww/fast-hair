from fastapi import APIRouter

router = APIRouter()


@router.get("/customer/booking")
def get_customer_booking(customer_id: int):
    # Logic to fetch customer's bookings
    return {"customer_id": customer_id, "bookings": []}


@router.post("/customer/booking")
def create_customer_booking(customer_id: int, date_time: str):
    # Logic to create a new booking for the customer
    return {"customer_id": customer_id, "date_time": date_time}