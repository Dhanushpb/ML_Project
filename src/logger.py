import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filemode='w'
)

if __name__ == "__main__":
    logging.info("Logging setup complete.")
   
''' logging.info(f"Log file created at: {LOG_FILE_PATH}")
    logging.info("This is an info message for testing purposes.")
    logging.error("This is an error message for testing purposes.")
    logging.warning("This is a warning message for testing purposes.")
    logging.debug("This is a debug message for testing purposes.")'''