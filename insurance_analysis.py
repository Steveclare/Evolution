import pandas as pd
import logging
from datetime import datetime
import os

## SECTION: Logging Configuration
## Purpose: Set up logging to track analysis operations and potential issues
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('insurance_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

## SECTION: Constants
## Purpose: Define carrier names and other constants for easy maintenance
CARRIER_COLUMNS = [
    'AmTrust', 'Bristol West', 'Chubb', 'CNA', 'Employers', 'Guard',
    'Hanover', 'Hartford', 'Hourly', 'ICW', 'Kemper', 'Liberty Mutual',
    'Markel', 'Philadelphia', 'Preferred', 'Stillwater', 'Travelers', 'UFG'
]

class InsuranceAnalyzer:
    """
    ## CLASS: InsuranceAnalyzer
    ## Purpose: Main class for analyzing insurance submission data
    ## Usage: Primary tool for agents to analyze carrier quote patterns
    """
    
    def __init__(self, excel_path):
        """Initialize the analyzer with the path to the Excel file."""
        self.excel_path = excel_path
        self.df = None
        self.load_data()

    def load_data(self):
        """
        ## SECTION: Data Loading
        ## Purpose: Load and validate the Excel data
        ## Note: Empty carrier columns indicate no quote provided
        """
        try:
            logger.info(f"Loading data from {self.excel_path}")
            self.df = pd.read_excel(self.excel_path)
            logger.info(f"Successfully loaded {len(self.df)} records")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def analyze_carrier_response_patterns(self):
        """
        ## SECTION: Carrier Analysis
        ## Purpose: Analyze which carriers are quoting different types of business
        ## Returns: Dictionary with carrier quote statistics
        """
        results = {}
        
        # Count total quotes by carrier
        for carrier in CARRIER_COLUMNS:
            if carrier in self.df.columns:
                # Non-null values indicate quotes were provided
                quote_count = self.df[carrier].notna().sum()
                total_submissions = len(self.df)
                quote_percentage = (quote_count / total_submissions) * 100
                
                results[carrier] = {
                    'total_quotes': quote_count,
                    'quote_percentage': round(quote_percentage, 2),
                    'total_submissions': total_submissions
                }
        
        return results

    def analyze_by_lob(self):
        """
        ## SECTION: Line of Business Analysis
        ## Purpose: Analyze carrier preferences by line of business
        ## Returns: Dictionary with LOB statistics
        """
        results = {}
        
        for lob in self.df['LOB'].unique():
            lob_data = self.df[self.df['LOB'] == lob]
            carrier_responses = {}
            
            for carrier in CARRIER_COLUMNS:
                if carrier in self.df.columns:
                    quote_count = lob_data[carrier].notna().sum()
                    if quote_count > 0:
                        carrier_responses[carrier] = quote_count
            
            results[lob] = {
                'total_submissions': len(lob_data),
                'carrier_responses': carrier_responses
            }
        
        return results

    def generate_report(self):
        """
        ## SECTION: Reporting
        ## Purpose: Generate comprehensive analysis report
        ## Returns: Dictionary containing all analysis results
        """
        logger.info("Generating analysis report")
        
        report = {
            'carrier_patterns': self.analyze_carrier_response_patterns(),
            'lob_analysis': self.analyze_by_lob(),
            'analysis_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_records': len(self.df)
        }
        
        return report

def main():
    """
    ## SECTION: Main Execution
    ## Purpose: Entry point for running the analysis
    """
    try:
        analyzer = InsuranceAnalyzer('Evolution Master Submission Log.xlsx')
        report = analyzer.generate_report()
        
        # Print summary of findings
        print("\n=== Insurance Quote Analysis Report ===")
        print(f"\nAnalysis Date: {report['analysis_date']}")
        print(f"Total Records Analyzed: {report['total_records']}")
        
        print("\nCarrier Quote Patterns:")
        for carrier, stats in report['carrier_patterns'].items():
            print(f"\n{carrier}:")
            print(f"  Total Quotes: {stats['total_quotes']}")
            print(f"  Quote Rate: {stats['quote_percentage']}%")
        
        print("\nLine of Business Analysis:")
        for lob, data in report['lob_analysis'].items():
            print(f"\n{lob}:")
            print(f"  Total Submissions: {data['total_submissions']}")
            if data['carrier_responses']:
                print("  Carrier Responses:")
                for carrier, count in data['carrier_responses'].items():
                    print(f"    {carrier}: {count} quotes")
                    
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main() 