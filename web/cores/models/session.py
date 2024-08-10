from pydantic import BaseModel

class GetSession(BaseModel):
    _session: str
    user_id: int
    login: str
    password: str
    is_admin: int
    cookie_create_time: int # UNIX Time
    ip: str # TODO: нужно совместить с ipv6, но пока что лень
    token: str


class PayloadSession(BaseModel):
    user_id: int
    login: str
    password: str
    is_admin: int
    cookie_create_time: int # UNIX Time
    ip: str # TODO: нужно совместить с ipv6, но пока что лень
    token: str
    