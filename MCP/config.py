import os
from dotenv import load_dotenv

def config_env_vars():
    load_dotenv()

    KORONA_BASE_URL = os.getenv("KORONA_BASE_URL")
    KORONA_ACCOUNT_ID = os.getenv("KORONA_ACCOUNT_ID")
    KORONA_API_USERNAME = os.getenv("KORONA_API_USERNAME")
    KORONA_API_PASSWORD = os.getenv("KORONA_API_PASSWORD")

    if(None in (KORONA_BASE_URL, KORONA_ACCOUNT_ID, KORONA_API_USERNAME, KORONA_API_PASSWORD)):
        raise Exception("Some values in .env file are not initialized")


    os.environ["KORONA_BASE_URL"] = KORONA_BASE_URL
    os.environ["KORONA_ACCOUNT_ID"] = KORONA_ACCOUNT_ID
    os.environ["KORONA_API_USERNAME"] = KORONA_API_USERNAME
    os.environ["KORONA_API_PASSWORD"] = KORONA_API_PASSWORD