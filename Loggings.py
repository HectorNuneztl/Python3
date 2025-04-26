import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format = "%(asctime)s - %(levelname)s - %(message)s")

logging.debug("debug") # least important 
logging.info("info") # second least important 
logging.warning("warning") # third least important
logging.error("error") # fourth least important
logging.critical("critical") # more important

