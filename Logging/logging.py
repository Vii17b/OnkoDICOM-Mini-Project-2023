import logging

class CustLogger:
    def __init__(self, log_level=logging.DEBUG, name=__name__):
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        
        file_holder = logging.FileHandler("src/log_file.log")
        
        formatter = logging.Formatter('%(asctime)s '
                                      '- %(levelname)s '
                                      '- %(name)s '
                                      '- : %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        
        file_holder.setFormatter(formatter)

        self.logger.addHandler(file_holder)