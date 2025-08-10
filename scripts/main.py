import logging
from src.utils.helper import settingup_logger

# Setting up the logger for the main script
settingup_logger("main")
logger=logging.getLogger(__name__)

def main():
    logger.info("Starting the main script.")
    # Your main script logic goes here
    logger.info("Main script finished successfully.")


if __name__ == "__main__":
    main()