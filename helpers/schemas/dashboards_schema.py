from pydantic import BaseModel
from typing import List

class GetDashboardSchema(BaseModel):
    id: int
    timezone: str
    title: str = 'Dashboard for API'
    uid: str

class GetDashboardsWithIncorrectCredentialsSchema(BaseModel):
    message: str = "Invalid username or password"
    messageId: str = "password-auth.failed"