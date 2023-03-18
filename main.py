from credit.logger import logging
from credit.exception import CreditException
import os
import sys
from credit.utils import get_collection_as_dataframe




def test_logger_and_exception():
    try:
        logging.info(f"Starting the test logger and exception")
        result = 3/10
        print(result)
        logging.info(f"Ending the test logger and exception")
    except Exception as e:
        logging.debug(str(e))
        raise CreditException(e, sys)



if __name__=="__main__":
    try:
        #test_logger_and_exception()
        get_collection_as_dataframe(database_name="CREDIT-CARD", collection_name="default-credit-card")
        
    except Exception as e:
        print(e)