import inspect
import logging


def customer_logger():
    log_name = inspect.stack()[1][3]

    logger = logging.getLogger(log_name)

    logger.setLevel(logging.DEBUG)

    # filehandler=logging.FileHandler("{0}.log".format(logName), mode='a')
    # filehandler=logging.FileHandler("CodeLead.log".format(logName), mode='a')
    filehandler = logging.FileHandler("../reports/CodeLead.log".format(log_name), mode='a')

    filehandler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%y %I:%M:$S %p %A')

    filehandler.setLevel(logging.DEBUG)

    logger.addHandler(filehandler)

    return logger
