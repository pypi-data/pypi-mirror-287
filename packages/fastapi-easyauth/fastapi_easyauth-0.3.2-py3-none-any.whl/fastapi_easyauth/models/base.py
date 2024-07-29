from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, JSON
from email_validator import validate_email, EmailSyntaxError, EmailNotValidError


class BaseValidateConfig:
    max_lenght_username = 50
    min_lenght_username = 3
    max_lenght_password = 50
    min_lenght_password = 5


class UserBaseModel:
    __tablename__ = 'User'
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(length = 50), unique = True)
    password: Mapped[str] = mapped_column(String(length = 50))
    email: Mapped[str] = mapped_column(nullable = True, unique = True)
    
    
    def validate(self) -> tuple[bool, str]: 
        if self.ValidateConfig.min_lenght_username > len(self.username) or len(self.username) > self.ValidateConfig.max_lenght_username:
            return (False, f'The user name must be between {self.ValidateConfig.min_lenght_username} and {self.ValidateConfig.max_lenght_username} characters long')
            
        if self.ValidateConfig.min_lenght_password > len(self.password) or len(self.password) > self.ValidateConfig.max_lenght_password:
            return (False, f'The password must be between {self.ValidateConfig.min_lenght_password} and {self.ValidateConfig.max_lenght_password} characters long')
            
        if self.email:      
            try:
                v = validate_email(self.email)
                email_normalized = v.normalized
                
            except EmailSyntaxError as e:
                return (False, f'The mail syntax is incorrect')
            
            except EmailNotValidError as e:
                return (False, f'This email is not valid')
        
        return (True, f'The data has been validated')
        
            
    
    
    class ValidateConfig(BaseValidateConfig):
        pass
    
    