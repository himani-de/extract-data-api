import requests
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')


def get_api_response(endpoint):
    """
    get response from api
    """
    try:
        get_api_response = requests.get(endpoint)
        logger.info('Connected to todo api successfully')
    except Exception as e:
        logger.error('Error while connecting to api..exiting the program')
        sys.exit(2)
    finally:
        api_response = get_api_response.json()
        return api_response
