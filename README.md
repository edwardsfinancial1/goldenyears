# GoldenYears IQ

![GoldenYears IQ Logo](/app/static/images/logo.png)

A premium retirement income planning software that helps users visualize and plan their financial future with confidence.

## Features

- **Comprehensive Income Projection**: Calculate expected retirement income from multiple sources including Social Security, pensions, investments, and annuities
- **Inflation Adjustment**: Automatically adjust income and needs for inflation to maintain purchasing power
- **Survivor Scenario Analysis**: Model what happens when one spouse passes away, including Social Security adjustments and pension survivor benefits
- **AI-Powered Insights**: Generate personalized retirement stories that transform financial data into meaningful narratives
- **Premium Visualization**: View your retirement plan through elegant, interactive charts and graphs
- **Professional PDF Reports**: Generate comprehensive reports for sharing with family or financial advisors

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/goldenyears-iq.git
   cd goldenyears-iq
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   cd app
   streamlit run app.py
   ```

The application will open in your default web browser at `http://localhost:8501`.

## Deployment

### Streamlit Cloud (Recommended)

1. Create a GitHub repository with your app code
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect to your GitHub repo and deploy

### Self-hosting

1. Install Streamlit on your server
2. Run `streamlit run app.py` to start the application
3. Set up a reverse proxy (like Nginx) if needed

### Docker

1. Build the Docker image:
   ```bash
   docker build -t goldenyears-iq .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 goldenyears-iq
   ```

## Documentation

For detailed usage instructions, please refer to the [User Guide](/user_guide.md).

## Project Structure

```
goldenyears-iq/
├── app/                    # Main application directory
│   ├── app.py              # Main Streamlit application
│   ├── components/         # UI components
│   │   ├── sidebar.py      # Sidebar navigation
│   │   ├── client_info.py  # Client information form
│   │   ├── income_sources.py # Income sources form
│   │   ├── scenarios.py    # Survivor scenario analysis
│   │   └── charts.py       # Data visualization components
│   ├── utils/              # Utility modules
│   │   ├── calculations.py # Core calculation engine
│   │   ├── pdf_generator.py # PDF report generation
│   │   └── ai_insights.py  # AI-powered retirement stories
│   ├── static/             # Static assets
│   │   ├── style.css       # Custom CSS styles
│   │   └── images/         # Images and icons
│   ├── data/               # Data storage
│   └── tests/              # Test scripts
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── user_guide.md           # User documentation
```

## Development

### Running Tests

```bash
cd app/tests
python test_app.py
```

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for the amazing framework
- OpenAI for the AI-powered insights
- All contributors and users of GoldenYears IQ

---

© 2025 GoldenYears IQ | Premium Retirement Income Planning Software

