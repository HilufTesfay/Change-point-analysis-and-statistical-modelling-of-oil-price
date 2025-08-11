import logging
import numpy as np
from src.data.cpa_analysis import bayesian_change_points
from src.data.analysis import load_data
from src.utils.helper import settingup_logger,get_root_folder

root_folder=get_root_folder()
data_path=root_folder/"data"/"processed"/"BrentOilPrices_cleaned.csv"
# Setting up the logger for the main script
settingup_logger("main")
logger=logging.getLogger(__name__)

def main():
    logger.info("Starting the main script.")
    cleaned_df=load_data(file=data_path)
    
    cleaned_df['log_price'] = np.log(cleaned_df['Price'])
    cleaned_df['log_return'] = cleaned_df['log_price'].diff()
    cleaned_df = cleaned_df.dropna(subset=['log_return'])
    y = cleaned_df['log_return'].dropna().values
    change_indices = bayesian_change_points(y, min_segment_length=50, max_cps=5)
    change_dates = cleaned_df['Date'].iloc[change_indices].values

    logger.info(f"change point dates : {change_dates}")
    logger.info("Main script finished successfully.")


if __name__ == "__main__":
    main()