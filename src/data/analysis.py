import pandas as pd 
import logging

logger=logging.getLogger(__name__)

def load_data(file:str) -> pd.DataFrame:
    """Loads data from a CSV file into a pandas DataFrame."""
    
    try:
        df = pd.read_csv(file)
        logger.info(f"Data loaded successfully from {file}")
        return df
    except Exception as e:
        logger.error(f"Error loading data from {file}: {e}")
        return None
    finally:
        logger.info(f"Finished loading data from {file}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the DataFrame by removing NaN values and duplicates."""
    
    if df is None:
        logger.warning("No data to clean.")
        return None
    
    logger.info("Starting data cleaning process.")
    logger.info(f"Initial data shape: {df.shape}")
    try:
        df_cleaned = df.dropna().drop_duplicates()
        final_shape = df_cleaned.shape
        df_cleaned["Date"]=pd.to_datetime(df['Date'], format='mixed')

        logger.info(f"Data cleaned: {df.shape} -> {final_shape}")
        return df_cleaned
    except Exception as e:
        logger.error(f"error cleaning data {e}")


def perform_initial_eda(df: pd.DataFrame) -> None:
    """Performs initial exploratory data analysis on the DataFrame."""
    
    if df is None or df.empty:
        logger.warning("No data available for EDA.")
        return
    
    logger.info("Performing initial EDA.")
    
    # Display basic information about the DataFrame
    logger.info(f"DataFrame shape: {df.shape}")
    logger.info(f"Columns: {df.columns.tolist()}")
    
    # Display summary statistics
    logger.info("Summary statistics:")
    logger.info(df.describe())
    
    # Display first few rows
    logger.info("First few rows of the DataFrame:")
    logger.info(df.head())
    
    logger.info("Initial EDA completed.")


