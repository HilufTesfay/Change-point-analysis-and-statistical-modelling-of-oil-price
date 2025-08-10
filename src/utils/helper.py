import pathlib
import logging

def get_root_folder() -> pathlib.Path:
    """Returns the root folder of the project."""
    return pathlib.Path(__file__).resolve().parent.parent.parent


def settingup_logger(log_file:str) -> None:
    """ Sets up the logger for the application. """
    log_file = get_root_folder() / 'logs' / log_file 
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(f"{log_file}.log", mode='a', encoding='utf-8'),
        ]
    )


