"""
World Bank Data Collector
Fetches economic indicators from World Bank API
"""

import wbdata
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WorldBankDataCollector:
    """Collects economic data from World Bank"""
    
    # Common economic indicators
    INDICATORS = {
        'NY.GDP.MKTP.CD': 'GDP (current US$)',
        'NY.GDP.MKTP.KD.ZG': 'GDP growth (annual %)',
        'FP.CPI.TOTL.ZG': 'Inflation (annual %)',
        'SL.UEM.TOTL.ZS': 'Unemployment rate (%)'
    }
    
    def get_country_data(self, countries, start_year=2000, end_year=2023):
        """Get economic data for specific countries"""
        try:
            data = wbdata.get_dataframe(
                indicators=self.INDICATORS,
                country=countries,
                convert_date=True
            )
            
            # Process the data
            data = data.reset_index()
            data['year'] = data['date'].dt.year
            data = data.drop('date', axis=1)
            
            logger.info(f"Retrieved data for {len(data)} country-year pairs")
            return data
            
        except Exception as e:
            logger.error(f"Error fetching data: {e}")
            return pd.DataFrame()

def main():
    """Example usage"""
    collector = WorldBankDataCollector()
    
    # Get data for major economies
    countries = ['USA', 'CHN', 'IND', 'BRA', 'DEU']  # US, China, India, Brazil, Germany
    data = collector.get_country_data(countries, 2020, 2022)
    
    if not data.empty:
        print("Sample data:")
        print(data.head())
    else:
        print("No data retrieved")

if __name__ == "__main__":
    main()
