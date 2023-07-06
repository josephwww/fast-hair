from fastapi import FastAPI
from app.customer.booking import router as customer_booking_router
from app.customer.products import router as customer_products_router
from app.customer.membership import router as customer_membership_router
from app.employee.bookings import router as employee_bookings_router
from app.employee.salary import router as employee_salary_router
from app.manager.shop import router as manager_shop_router
from app.manager.staff import router as manager_staff_router

app = FastAPI()

# Mount the customer sub-app
app.include_router(customer_booking_router)
app.include_router(customer_products_router)
app.include_router(customer_membership_router)

# Mount the employee sub-app
app.include_router(employee_bookings_router)
app.include_router(employee_salary_router)

# Mount the manager sub-app
app.include_router(manager_shop_router)
app.include_router(manager_staff_router)
