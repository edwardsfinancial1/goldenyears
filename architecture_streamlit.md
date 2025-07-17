# Income Planner Application Architecture (Streamlit)

## Overview
The Income Planner will be built as a Streamlit web application. This architecture provides a responsive, interactive user interface while leveraging Python's powerful calculation capabilities, all within a single technology stack.

## System Architecture

### Streamlit Application
- **User Interface Layer**: Streamlit components for forms, charts, and reports
- **State Management**: Streamlit session state for managing application state
- **Calculation Engine**: Direct integration with Python calculation modules
- **Visualization**: Plotly, Altair, or Matplotlib for interactive charts and graphs
- **PDF Generation**: ReportLab or WeasyPrint for PDF report generation
- **Styling**: Custom CSS and Streamlit theming for premium styling

## Component Breakdown

### Streamlit Pages/Sections
1. **Main Dashboard**
   - Overview of financial plan
   - Summary metrics and key insights
   - Navigation to other sections

2. **Input Sections**
   - Client Information: Personal details, ages, retirement year
   - Income Sources: Social Security, pension, investments, FIA
   - Calculation Parameters: Inflation, return rates, projection period
   - Scenario Configuration: Spouse death scenario settings

3. **Visualization Sections**
   - Income Projection: Stacked area chart showing income sources over time
   - Needs Comparison: Line chart comparing income vs. needs
   - Surplus/Deficit Analysis: Bar chart showing surplus/deficit by year
   - Scenario Comparison: Comparing different scenarios

4. **Report Section**
   - Report configuration options
   - Report preview
   - PDF download functionality

### Python Modules
1. **Calculation Module**
   - `income_calculator.py`: Core calculation logic for income projections
   - `inflation_adjuster.py`: Applies inflation adjustments to values
   - `scenario_simulator.py`: Simulates spouse death scenarios
   - `investment_calculator.py`: Calculates investment returns and withdrawals

2. **PDF Generation Module**
   - `report_generator.py`: Creates PDF reports with charts and tables
   - `report_templates.py`: Manages report templates and styling

3. **Data Persistence Module** (Optional)
   - `data_manager.py`: Handles saving and loading scenarios
   - `file_operations.py`: Manages file I/O operations

## Data Flow
1. User inputs client information and income sources via Streamlit forms
2. Streamlit passes data directly to Python calculation modules
3. Calculation results are stored in Streamlit session state
4. Streamlit renders visualizations and tables based on calculation results
5. User can adjust inputs and see real-time updates
6. User can generate and download PDF reports

## Technology Stack
- **Application Framework**:
  - Streamlit for the entire application
  
- **Data Processing and Calculations**:
  - Pandas for data manipulation
  - NumPy for numerical calculations
  
- **Visualization**:
  - Plotly for interactive charts
  - Altair for declarative visualizations
  - Matplotlib/Seaborn for static charts
  
- **PDF Generation**:
  - ReportLab or WeasyPrint for PDF generation
  
- **Styling**:
  - Custom CSS for premium styling
  - Streamlit theming capabilities

## Deployment Strategy
- Streamlit Cloud for easy deployment and sharing
- Docker container for local or custom server deployment
- GitHub integration for version control and continuous deployment

## Security Considerations
- Input validation within Streamlit forms
- No persistent storage of sensitive information unless explicitly requested
- Secure handling of financial data

## Advantages of Streamlit for this Application
1. **Rapid Development**: Streamlit allows for faster development with less code
2. **Python-Centric**: Entire application in Python, simplifying the tech stack
3. **Built-in Interactivity**: Native support for interactive elements
4. **Easy Deployment**: Simple deployment options
5. **Data Science Focus**: Excellent integration with data visualization libraries
6. **Responsive Design**: Automatic mobile-friendly layouts

## Future Extensibility
- Additional financial planning modules
- Integration with financial data providers
- Enhanced visualization capabilities
- Export to additional formats

