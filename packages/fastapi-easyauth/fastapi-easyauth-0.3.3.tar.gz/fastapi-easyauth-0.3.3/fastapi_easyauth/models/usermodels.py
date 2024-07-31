from .base import UserBaseModel, BaseValidateConfig
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, JSON, func

from typing import Optional, Union

from datetime import datetime


class FullUserModel(UserBaseModel):
    first_name: Mapped[Optional[str]] = mapped_column(String(length = 20))
    last_name: Mapped[Optional[str]] = mapped_column(String(length = 20))
    date_of_created: Mapped[datetime] = mapped_column(default = func.now())
    date_of_update: Mapped[datetime] = mapped_column(default = func.now(), onupdate = func.now())
    refresh_token: Mapped[Optional[str]]
    role: Mapped[Optional[str]]
    
    
    def validate(
        self,
    ) -> tuple[bool, str]:
        
        result = super().validate()
        if result[0] == False:
            return result
        
        v = self.ValidateConfig
        
        if v.min_len_first_name > len(self.first_name) or len(self.first_name) > v.max_len_first_name:
            return (False, f'The length of the first name must be from {v.min_len_first_name} to {v.max_len_first_name}')
        
        if v.min_len_last_name > len(self.last_name) or len(self.last_name) > v.max_len_last_name:
            return (False, f'The length of the last name must be from {v.min_len_last_name} to {v.max_len_last_name}')
        
        return result
        
        
    
    class ValidateConfig(BaseValidateConfig):
        min_len_first_name = 3
        max_len_first_name = 15
        min_len_last_name = 3
        max_len_last_name = 15
        
        


class UserModelR(UserBaseModel):
    refresh_token: Mapped[Optional[str]]