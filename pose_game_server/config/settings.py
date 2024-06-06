from config.env_util import Environment
from dotenv import load_dotenv
from logger import logger

""""load environment variables"""

# Load env variables from a file, if exists else default would be set
logger.info("SERVER_INIT::Setting environment variables from .env file")
load_dotenv(verbose=True)


class ENV:
    # db_url = Environment.get_string("MONGO_DB_URL")