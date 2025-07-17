# Income Planner Application Requirements

## Overview
The Income Planner is a premium financial planning tool designed to help users plan their retirement income. It provides a sophisticated yet user-friendly interface for inputting various income sources, adjusting for inflation, and simulating scenarios such as the death of a spouse.

## Functional Requirements

### User Inputs
1. **Client Information**
   - Client name(s)
   - Client age(s)
   - Retirement age/year
   - Current year (default to system date)
   - Annual income needs in retirement

2. **Income Sources**
   - Social Security income for each spouse
   - Pension income
   - Pension survivor percentage
   - Investment amount (for 4% rule calculation)
   - Fixed Indexed Annuity (FIA) income

3. **Calculation Parameters**
   - Inflation rate
   - Investment return rate
   - Projection period (up to 20 years)

4. **Scenario Options**
   - Ability to simulate spouse death in any given year
   - Option to specify which spouse dies
   - Adjustments to income sources based on death scenario

### Calculations
1. **Base Income Projection**
   - Calculate total income from all sources for each year
   - Project income needs adjusted for inflation
   - Calculate surplus/deficit for each year

2. **Inflation Adjustment**
   - Apply inflation rate to income sources as appropriate
   - Adjust income needs for inflation over time

3. **Spouse Death Scenario**
   - Remove the deceased spouse's Social Security
   - Adjust pension based on survivor percentage
   - Recalculate total income and surplus/deficit

4. **Investment Income**
   - Calculate 4% of investment amount as annual income
   - Option to adjust the withdrawal percentage

### Output and Visualization
1. **Interactive Dashboard**
   - Summary of inputs and key metrics
   - Visual representation of income vs. needs over time
   - Comparison of different scenarios

2. **Detailed Reports**
   - Year-by-year breakdown of all income sources
   - Inflation-adjusted values
   - Surplus/deficit analysis

3. **PDF Export**
   - Professional-looking reports with client information
   - Charts and tables showing income projections
   - Scenario comparisons
   - Emotional insights about financial security

## Non-Functional Requirements

### User Experience
1. **Premium Design**
   - Professional, high-end visual design similar to MoneyGuidePro, eMoney, or RightCapital
   - Intuitive navigation and workflow
   - Responsive design for different screen sizes

2. **Emotional Resonance**
   - Visual cues that evoke security and confidence
   - Language that emphasizes peace of mind and future planning
   - Personalized insights based on the financial situation

### Performance
1. **Calculation Speed**
   - Real-time updates of calculations when inputs change
   - Smooth transitions and animations

2. **Reliability**
   - Accurate calculations matching the Excel model
   - Proper handling of edge cases

### Technical
1. **Modern Web Technologies**
   - React for frontend
   - Python for backend calculations
   - PDF generation capabilities

2. **Data Persistence**
   - Option to save and load client scenarios
   - Export functionality for reports and data

## Constraints
1. Must match or exceed the calculation methodology in the provided Excel file
2. Must have a premium, professional appearance
3. Must be user-friendly for financial advisors and their clients
4. Must provide PDF export functionality

