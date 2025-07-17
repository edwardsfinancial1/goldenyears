# GoldenYears IQ User Guide

## Introduction

Welcome to GoldenYears IQ, a premium retirement income planning software designed to help you visualize and plan your financial future with confidence. This guide will walk you through the features and functionality of the application.

## Getting Started

### Installation

1. **Prerequisites**:
   - Python 3.8 or higher
   - pip (Python package installer)

2. **Install the application**:
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/goldenyears-iq.git
   cd goldenyears-iq
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Launch the application**:
   ```bash
   cd app
   streamlit run app.py
   ```
   
   The application will open in your default web browser at `http://localhost:8501`.

### Deployment Options

GoldenYears IQ can be deployed in several ways:

1. **Streamlit Cloud** (Recommended for public access):
   - Create a GitHub repository with your app code
   - Sign up for Streamlit Cloud (free tier available)
   - Connect to your GitHub repo and deploy

2. **Self-hosting**:
   - Install Streamlit on your server
   - Run `streamlit run app.py` to start the application
   - Set up a reverse proxy (like Nginx) if needed

3. **Docker**:
   - Use the provided Dockerfile to build a container
   - Deploy the container to your preferred hosting service

## Using the Application

### Navigation

The application is organized into several sections, accessible from the sidebar:

- **Dashboard**: Overview of your retirement income plan
- **Client Information**: Enter personal details and retirement goals
- **Income Sources**: Input various income sources for retirement
- **Scenarios**: Create and analyze survivor scenarios
- **Reports**: Generate and download PDF reports

### Step-by-Step Guide

#### 1. Enter Client Information

1. Navigate to the "Client Information" section
2. Enter client names, ages, and retirement age
3. Specify income needs in retirement
4. Add any specific retirement goals or milestones
5. Click "Save Client Information"

#### 2. Add Income Sources

1. Navigate to the "Income Sources" section
2. Enter Social Security income for each spouse
3. Add pension income and survivor benefit percentage
4. Enter investment amount and withdrawal rate
5. Add Fixed Indexed Annuity (FIA) income if applicable
6. Specify inflation rate for adjusting future values
7. Click "Save Income Sources"

#### 3. View Dashboard

1. Navigate to the "Dashboard" section
2. Review the income projection chart showing all income sources
3. Analyze the income vs. needs comparison
4. Examine the surplus/deficit analysis
5. Read your personalized retirement story

#### 4. Create Survivor Scenarios

1. Navigate to the "Scenarios" section
2. Select which spouse is the survivor
3. Choose the year when the scenario begins
4. Specify the pension survivor benefit percentage
5. Click "Calculate Survivor Scenario"
6. Compare the base scenario with the survivor scenario

#### 5. Generate Reports

1. Navigate to the "Reports" section
2. Select which sections to include in the report
3. Click "Generate PDF Report"
4. Download the PDF report for sharing or printing

## Features

### Income Projection

The income projection feature calculates your expected income throughout retirement, including:

- Social Security benefits for both spouses
- Pension income
- Investment income based on your specified withdrawal rate
- Fixed Indexed Annuity (FIA) income
- Inflation adjustments to maintain purchasing power

### Survivor Scenario Analysis

The survivor scenario analysis helps you understand how your income would be affected if one spouse passes away:

- Adjusts Social Security benefits (typically only the higher benefit continues)
- Modifies pension income based on the survivor benefit percentage
- Reduces income needs to reflect a single-person household
- Shows the impact on surplus/deficit throughout retirement

### AI-Powered Retirement Story

The application uses advanced AI to transform your financial data into a personalized retirement story that:

- Provides an emotional narrative of your retirement journey
- Highlights financial milestones and achievements
- Addresses potential challenges in a compassionate way
- Includes a well-being score to gauge your financial security

### PDF Reports

Generate comprehensive PDF reports that include:

- Executive summary of your retirement plan
- Detailed income projections with charts and tables
- Needs comparison analysis
- Surplus/deficit analysis
- Survivor scenario comparison (if created)
- Your personalized retirement story
- Assumptions and methodology

## Troubleshooting

### Common Issues

1. **Application won't start**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check that you're using Python 3.8 or higher: `python --version`

2. **Charts not displaying**:
   - Make sure you have entered all required information in the Client Information and Income Sources sections
   - Try refreshing the page

3. **PDF generation fails**:
   - Ensure you have completed all required information
   - Check that you have sufficient disk space

4. **Retirement story not generating**:
   - The AI feature requires an internet connection
   - If the OpenAI service is unavailable, a basic summary will be provided instead

### Getting Help

If you encounter issues not covered in this guide, please:

1. Check the [GitHub repository](https://github.com/yourusername/goldenyears-iq) for known issues
2. Submit a new issue with detailed information about your problem
3. Contact support at support@goldenyearsiq.com

## Privacy and Security

GoldenYears IQ is designed with your privacy in mind:

- All calculations are performed locally in your browser
- No financial data is stored on external servers
- PDF reports are generated locally on your device
- The only external service used is the OpenAI API for generating retirement stories

## Conclusion

GoldenYears IQ is designed to help you plan for a secure and fulfilling retirement. By providing comprehensive income projections, survivor scenario analysis, and personalized insights, we aim to give you the confidence to make informed financial decisions for your golden years.

Thank you for choosing GoldenYears IQ for your retirement planning needs!

---

© 2025 GoldenYears IQ | Premium Retirement Income Planning Software

