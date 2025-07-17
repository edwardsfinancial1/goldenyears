# Income Planner Application Architecture

## Overview
The Income Planner will be built as a modern web application with a React frontend and a Python Flask backend. This architecture provides a responsive, interactive user interface while leveraging Python's powerful calculation capabilities.

## System Architecture

### Frontend (React)
- **User Interface Layer**: React components for forms, charts, and reports
- **State Management**: React Context API or Redux for managing application state
- **API Integration**: Axios for API calls to the backend
- **Visualization**: Chart.js or D3.js for interactive charts and graphs
- **PDF Generation**: Client-side PDF generation using jsPDF or integration with backend PDF service
- **Styling**: Styled-components or Tailwind CSS for premium styling

### Backend (Python Flask)
- **API Layer**: RESTful API endpoints for calculations and data processing
- **Calculation Engine**: Core financial calculation logic
- **PDF Generation Service**: Report generation using ReportLab or WeasyPrint
- **Data Persistence**: Optional storage of user scenarios (could use SQLite for simplicity)

## Component Breakdown

### Frontend Components
1. **Layout Components**
   - AppLayout: Main application layout with navigation
   - Dashboard: Overview of financial plan
   - Sidebar: Navigation and quick actions

2. **Input Components**
   - ClientInfoForm: Client personal information
   - IncomeSourcesForm: Social Security, pension, investments
   - CalculationParamsForm: Inflation, return rates, projection period
   - ScenarioForm: Spouse death scenario configuration

3. **Visualization Components**
   - IncomeChart: Stacked area chart showing income sources over time
   - NeedsComparisonChart: Line chart comparing income vs. needs
   - SurplusDeficitChart: Bar chart showing surplus/deficit by year
   - ScenarioComparisonChart: Comparing different scenarios

4. **Report Components**
   - ReportGenerator: Configures and generates PDF reports
   - ReportPreview: Displays a preview of the report
   - ExportOptions: Controls for customizing exports

### Backend Services
1. **Calculation Service**
   - IncomeCalculator: Core calculation logic for income projections
   - InflationAdjuster: Applies inflation adjustments to values
   - ScenarioSimulator: Simulates spouse death scenarios
   - InvestmentCalculator: Calculates investment returns and withdrawals

2. **PDF Service**
   - ReportGenerator: Creates PDF reports with charts and tables
   - TemplateManager: Manages report templates and styling

3. **Data Service** (Optional)
   - ScenarioManager: Saves and loads user scenarios
   - UserManager: Manages user accounts and data (if implementing multi-user support)

## Data Flow
1. User inputs client information and income sources
2. Frontend sends data to backend for calculation
3. Backend processes calculations and returns results
4. Frontend displays results in charts and tables
5. User can adjust inputs and see real-time updates
6. User can generate and download PDF reports

## Technology Stack
- **Frontend**:
  - React.js
  - Chart.js or D3.js for visualizations
  - Styled-components or Tailwind CSS for styling
  - jsPDF for client-side PDF generation (optional)

- **Backend**:
  - Python Flask for API endpoints
  - Pandas for data manipulation
  - NumPy for numerical calculations
  - ReportLab or WeasyPrint for PDF generation

- **Development Tools**:
  - Vite or Create React App for frontend scaffolding
  - Flask-CORS for handling cross-origin requests
  - ESLint and Prettier for code formatting
  - Jest for frontend testing
  - Pytest for backend testing

## Deployment Strategy
- Frontend and backend can be deployed separately or as a single application
- For simplicity, the backend can serve the frontend static files
- Deployment options:
  - Local deployment for desktop use
  - Web server deployment for multi-user access
  - Containerization with Docker for easy deployment

## Security Considerations
- Input validation on both frontend and backend
- CSRF protection for API endpoints
- Secure handling of financial data
- No persistent storage of sensitive information unless explicitly requested

## Future Extensibility
- Multi-user support with authentication
- Additional financial planning modules
- Integration with financial data providers
- Mobile application version

