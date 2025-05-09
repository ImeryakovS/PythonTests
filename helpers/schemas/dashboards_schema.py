from pydantic import BaseModel
from typing import List

class GetDashboardSchema(BaseModel):
    id: int
    refresh: str
    schemaVersion: int
    tags: List[str]
    timezone: str
    title: str = 'Dashboard for API'
    uid: str
    version: int

class GetDashboardsWithIncorrectCredentialsSchema(BaseModel):
    extra: None
    message: str = "Invalid username or password"
    messageId: str = "password-auth.failed"
    statusCode: int
    traceID: str