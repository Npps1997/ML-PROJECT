import sys
sys.path.append(r'G:\ML Project\src')

from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.component.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # data_ingstion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

