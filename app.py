import sys
sys.path.append(r'G:\ML Project\src')

from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.component.data_ingestion import DataIngestion
from mlproject.component.data_transformation import DataTransformation

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # data_ingstion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path,test_data_path)

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

