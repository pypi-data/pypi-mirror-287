from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class MyConfig(BaseSettings):
    anthropic_api_key: str = Field(env="ANTHROPIC_API_KEY")
    # datastore_dir_path: str = Field(env="DATASTORE_DIR_PATH")
    db_url: str = Field(env="DB_URL")
    cohere_api_key: str = Field(env="COHERE_API_KEY")
    openai_api_key: str = Field(env="OPENAI_API_KEY")
    qdrant_api_key: str = Field(env="QDRANT_API_KEY")
    qdrant_url: str = Field(env="QDRANT_URL")

    class Config:
        env_file = ".env"
        extra = "allow"


config = MyConfig()
