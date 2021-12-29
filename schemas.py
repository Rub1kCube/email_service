from pydantic import BaseModel, Field, validator, EmailStr
import re


class SupportClient(BaseModel):

    full_name: str
    company: str
    email_address: EmailStr
    number_phone: str
    description: str = Field(..., max_length=100)

    @validator('number_phone')
    def check_number_phone(cls, value):
        pattern = r'^(\+7|8)\d{10}$'

        if re.fullmatch(pattern, value):
            return value
        else:
            raise ValueError('Incorrectly written number phone')


