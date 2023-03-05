from pydantic import BaseSettings

class Settings(BaseSettings):                 #setting environment variables
  database_hostname:str
  database_port:str
  database_pw:str
  database_name:str
  database_username:str
  secret_key:str
  algorithm:str
  access_token_exp_min:int
  
  class Config:
      env_file=".env"                   #importing env variable values from .env file
      
    
settings=Settings()             #storing all env variables in an instance of Settings class   