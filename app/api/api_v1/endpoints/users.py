from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Get Users!"}

@router.get("/")
async def root():
    return {"message": "Test users"}