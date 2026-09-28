from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str="postgresql+asyncpg://postgres:root@localhost:5432/postgres"
    
    
    class Config:
        env_file=".env"
        
        
        
setting=Settings()        


        