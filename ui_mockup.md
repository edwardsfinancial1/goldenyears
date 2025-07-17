# Income Planner UI Mockup

## Overall Design Principles
- Premium, professional appearance similar to MoneyGuidePro, eMoney, or RightCapital
- Clean, modern interface with ample white space
- Rich, meaningful visualizations
- Intuitive navigation
- Emotional resonance through design and language

## Color Scheme
- Primary: Deep blue (#1E3A8A) - Conveys trust, stability, and professionalism
- Secondary: Gold/amber (#F59E0B) - Represents wealth, prosperity
- Accent: Teal (#0D9488) - Modern, fresh color for highlights
- Background: Light gray (#F9FAFB) with white content areas
- Text: Dark gray (#1F2937) for main text, lighter gray (#6B7280) for secondary text

## Typography
- Headings: Montserrat (sans-serif)
- Body: Inter (sans-serif)
- Monospace: Roboto Mono (for numerical data)

## Layout Structure

### 1. Navigation
- Sidebar navigation with the following sections:
  - Dashboard (Home)
  - Client Information
  - Income Sources
  - Scenarios
  - Reports
  - Settings

### 2. Dashboard (Home)
- Header with application name and logo
- Client name and basic info card
- Key metrics cards:
  - Total retirement income (first year)
  - Income vs. needs gap
  - Projected years with surplus
  - Retirement readiness score
- Main visualization: Income vs. Needs over time chart
- Secondary visualizations:
  - Income sources breakdown (pie chart)
  - Surplus/deficit by year (bar chart)
- Quick actions buttons:
  - Edit inputs
  - Run scenarios
  - Generate report

### 3. Client Information Section
- Form with the following fields:
  - Client name(s)
  - Client 1 age
  - Client 2 age (if applicable)
  - Retirement age/year
  - Annual income needs in retirement
  - Inflation rate assumption
  - Projection period (slider: 5-30 years)
- "Save Information" button
- Progress indicator showing completion of inputs

### 4. Income Sources Section
- Social Security subsection:
  - Client 1 Social Security amount
  - Client 2 Social Security amount
  - Social Security start age for each client
- Pension subsection:
  - Pension amount
  - Pension provider (optional)
  - Survivor benefit percentage
- Investments subsection:
  - Total investment amount
  - Withdrawal rate (default 4%, adjustable)
  - Expected return rate
- Fixed Indexed Annuity (FIA) subsection:
  - FIA income amount
  - FIA provider (optional)
- Other Income subsection:
  - Additional income sources (name, amount, duration)
- Visual summary of all income sources

### 5. Scenarios Section
- Base scenario (default)
- Spouse death scenario configuration:
  - Year of death
  - Which spouse
  - Adjustments to income sources
- Comparison view showing:
  - Side-by-side charts of base vs. scenario
  - Income difference table
  - Surplus/deficit comparison
- "Add Scenario" button for multiple scenarios
- Scenario selection dropdown

### 6. Reports Section
- Report configuration options:
  - Sections to include
  - Level of detail
  - Chart customization
- Report preview panel
- "Generate PDF" button
- Download history

### 7. Settings
- Application preferences
- Default values
- Units and currency format
- Theme selection

## Interactive Elements

### Charts and Visualizations
1. **Income Projection Chart**
   - Stacked area chart showing all income sources over time
   - Horizontal line showing needs
   - Interactive tooltips showing details for each year
   - Ability to toggle income sources on/off

2. **Income Breakdown Pie Chart**
   - Proportional representation of income sources
   - Interactive segments with hover details
   - Year selector to see breakdown for different years

3. **Surplus/Deficit Chart**
   - Bar chart showing surplus (positive) or deficit (negative) for each year
   - Color coding (green for surplus, red for deficit)
   - Threshold line at zero

4. **Scenario Comparison Chart**
   - Line chart comparing total income across scenarios
   - Shaded area showing the difference
   - Interactive legend

### Form Elements
- Text inputs with validation
- Sliders for numerical ranges
- Toggles for boolean options
- Dropdowns for selections
- Date pickers for year selection
- Number inputs with increment/decrement buttons
- Help tooltips for explanations

## Mobile Responsiveness
- Collapsible sidebar on small screens
- Stacked layout for forms
- Simplified charts optimized for mobile viewing
- Touch-friendly input controls

## AI Integration Elements
- "Insights" panel with AI-generated analysis of the financial plan
- Natural language explanations of complex concepts
- Personalized recommendations based on the financial situation
- Q&A section where users can ask questions about their plan
- AI-assisted form filling suggestions

## PDF Report Design
- Professional cover page with client name and date
- Table of contents
- Executive summary with key findings
- Detailed income projections
- Visualizations matching the application
- Scenario comparisons
- Personalized insights and recommendations
- Appendix with assumptions and methodology
- Footer with page numbers and date

## Loading and Transition States
- Elegant loading animations
- Progress indicators for calculations
- Smooth transitions between sections
- Success/error notifications for user actions

