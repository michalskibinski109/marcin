import logging
import os


def get_logger(path="./logs/", file_name="studies.log", save_to_file=False, lvl=10):
    log_format = "%(levelname)-7s: %(filename)-10s: %(message)s"
    if save_to_file:
        if not os.path.exists(path):
            os.makedirs(path)
        path_to_file = os.path.join(path, file_name)
        logging.basicConfig(filename=path_to_file, format=log_format)
    else:
        logging.basicConfig(format=log_format)
    logger = logging.getLogger("log")
    logger.setLevel(lvl)
    return logger
