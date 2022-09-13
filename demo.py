from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion

import sys

def main():
    try:
        # pipeline = Pipeline(config=Configuartion(current_time_stamp=get_current_time_stamp()))
        # pipeline.run_pipeline()
        
        datavalidationconfig = Configuartion().get_data_validation_config()
        print(datavalidationconfig)


    except Exception as e:
        logging.error(str(e))
        raise HousingException(e, sys) from e


if __name__=="__main__":
    main()
    