from fastapi import APIRouter

from .endpoints import users
from .endpoints import data

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(data.router, prefix="/data", tags=["Data"])