import logging
import os
class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir)+ "..\\logs\\automation.log"
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(leveltime)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %P')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
