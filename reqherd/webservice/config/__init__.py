import os
import logging
from pathlib import Path
from subprocess import check_output

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

logger = logging.getLogger(__name__)


SOFTWARE_VERSION = "0.0.1"

REQHERD_API_V1_STR = "/reqherd/api/v1"

DEVELOPER_MODE = True


def reqherd_settings():
    """Get database connection info

    Get the information for connecting to the database. Change this so that
    it makes sense for your security model. I'm not an expert in cryptography
    or infosec, what little I know says that you need to define your threat
    model and minimize your attack surface. Just going to throw this out there,
    if your threat model involves trying to defend from nation state level
    attacks and espionage you probably shouldn't be using my software to
    track your project requirements if you want them to stay secure.

    The methodology implemented below is meant to convey clearly what is
    going on and not to actually provide any security for your database
    credentials.

    Returns
    -------
    dict
        Dictionary of database connection parameters.

    """

    def connection_params():
        # If you're going to use SQLite be more elegant than this.
        if DEVELOPER_MODE is True:

            def establish_database():
                database = "reqkit.db"
                reqherd_connection_url = f"sqlite:///reqherd/{database}"
                engine = create_engine(reqherd_connection_url)
                if not database_exists(engine.url):
                    create_database(engine.url)
                return reqherd_connection_url

            return establish_database()
        else:
            # Something like this
            connection_params_dict = {
                "rdbms": "postgres",
                "database_server": "localhost",
                "database_user": "root",
                "database_user_password": "root",
                "schema": "reqherd",
                "database_driver": "psycopg2",
            }
            return connection_params_dict

    if os.name == "posix":
        logger.info("Woo!")
        return connection_params()
    else:
        logger.info("WINDOZERRR!")
        return connection_params()
