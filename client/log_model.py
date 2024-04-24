from pydantic import BaseModel


class Log(BaseModel):
    log_msg: str
