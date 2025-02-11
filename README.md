# Evolution Partners Insurance Analytics Dashboard

A comprehensive analytics dashboard built with Streamlit for analyzing insurance submission data and tracking carrier responses.

## Features

- 📊 Real-time analytics of insurance submissions
- 🔍 Advanced business type search functionality
- 📈 Trend analysis and visualization
- 🏢 Line of Business (LOB) analysis
- 👷 Workers Compensation specific analysis
- 🏛️ Carrier response tracking
- 📅 Flexible date range filtering
- 📑 Source sheet filtering
- 💼 Detailed submission data view

## Prerequisites

- Python 3.8+
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/evolution-insurance-dashboard.git
cd evolution-insurance-dashboard
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your Excel file named `Evolution Master Submission Log.xlsx` in the project directory.

2. Generate the combined CSV file:
```bash
python combine_excel_sheets.py
```

3. Run the Streamlit dashboard:
```bash
streamlit run insurance_dashboard.py
```

4. Open your web browser and navigate to `http://localhost:8502`

## Project Structure

```
evolution-insurance-dashboard/
├── README.md
├── requirements.txt
├── insurance_dashboard.py    # Main dashboard application
├── combine_excel_sheets.py   # Data preprocessing script
├── insurance_analysis.py     # Analysis utilities
└── logo.png                 # Evolution Partners logo
```

## Configuration

The dashboard automatically loads data from `combined_submission_log.csv`, which is generated from your Excel file. The Excel file should contain the following columns:

- Applicant
- LOB (Line of Business)
- RCVD (Received Date)
- Bound With
- Various carrier columns for quotes

## Features in Detail

### Business Search
- Search through submissions using keywords
- Supports wildcard searches (e.g., "plumb*" for plumbing)
- View detailed carrier response patterns for specific business types

### Date Range Analysis
- Quick selection of common date ranges
- Custom date range selection
- Trend analysis over time

### Carrier Analysis
- Quote frequency analysis
- Win rate tracking
- Detailed carrier response patterns

### Line of Business Analysis
- Distribution visualization
- Detailed breakdown by LOB
- Special Workers Compensation analysis

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact Evolution Partners or open an issue in the GitHub repository. 