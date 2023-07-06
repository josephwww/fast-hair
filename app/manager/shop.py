from fastapi import APIRouter

router = APIRouter()


# Manager Side
@router.get("/manager/shop")
def get_shop_info():
    # Logic to fetch shop information
    return {"shop": {}}
