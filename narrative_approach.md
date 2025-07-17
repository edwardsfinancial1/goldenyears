# Retirement Storytelling Approach

## Overview
This document outlines the approach for transforming financial data into an emotional narrative that resonates with clients. The goal is to help users visualize their retirement future with warmth, hope, and realism, making the financial planning process more engaging and meaningful.

## Narrative Structure

### 1. Opening Hook
Start with a vivid, positive vision of retirement tailored to the couple's ages and plans. This creates immediate emotional engagement and helps clients visualize their future.

Example:
> "Imagine waking up at 65, hand in hand with [Partner Name], in your comfortable home, with the freedom to plan your day exactly as you wish. For the Johnsons, this vision becomes reality in 2030, with a financial foundation designed to support your dreams for decades to come."

### 2. Journey Through the Years
Weave financial projections into an emotional journey, highlighting:
- Secure periods as "chapters of freedom and joy"
- Shortfalls as "gentle reminders to nurture your nest egg"
- Inflation adjustments as "safeguards for lasting comfort"

Example:
> "Your first decade of retirement unfolds as a chapter of exploration and abundance. With $87,700 available annually (adjusted for inflation), you'll have approximately $7,300 monthly to enjoy life's pleasures—from regular dinners with friends to those European adventures you've been planning. As you move into your 70s, your income adjusts to keep pace with rising costs, ensuring your lifestyle remains comfortable even as prices change around you."

### 3. Emotional Anchors
Tie in user milestones or scenarios, especially addressing sensitive topics like survivor scenarios with compassion and practical reassurance.

Example:
> "Even in life's unexpected turns, your plan provides security. If [Partner Name] were to pass away in 2035, the surviving spouse would still maintain a comfortable $54,275 annual income—enough to cover essential needs, maintain your home, and continue meaningful traditions with family and friends."

### 4. Reflective Close
End with motivational insights, questions for reflection, and subtle calls to action.

Example:
> "How does this retirement story align with your vision? What dreams might you add to these secure chapters ahead? Consider how small adjustments today—perhaps increasing your investment contributions by just 2%—could add even more flexibility and joy to your future story."

### 5. Well-Being Score
Assign a 1-10 emotional security score based on the data, with a brief explanation.

Example:
> "Financial Well-Being Score: 8/10
> Your plan provides strong security throughout retirement, with income consistently meeting your needs. The small gap in later years presents an opportunity to further strengthen your legacy plans."

## Implementation Guidelines

### Tone and Language
- Use warm, reassuring language
- Avoid financial jargon; explain concepts in human terms
- Frame challenges as opportunities
- Be honest but optimistic
- Use the client's names throughout

### Personalization Elements
- Reference specific ages and years
- Incorporate known goals and dreams
- Adjust language based on client life stage
- Reference specific dollar amounts translated into lifestyle implications

### AI Integration
The narrative will be generated using the OpenAI API with:
- Client data from the income plan as context
- Custom prompting based on this narrative structure
- Appropriate temperature setting to ensure creativity while maintaining accuracy

## Example Prompt Template for AI

```
You are an empathetic retirement storyteller, helping users visualize their future with warmth, hope, and realism. Transform the following financial data into an emotional narrative that celebrates joys, addresses fears, and inspires action.

Client Information:
- Names: {client_names}
- Ages: {client_ages}
- Retirement Year: {retirement_year}
- Annual Income Needs: ${annual_needs}

Income Projection Summary:
{income_projection_summary}

Survivor Scenario (if applicable):
{survivor_scenario}

Known Goals/Milestones:
{client_goals}

Create a 300-500 word "Your Retirement Story" following this structure:
1. Opening Hook: A vivid, positive vision of retirement
2. Journey Through the Years: Financial projections as emotional chapters
3. Emotional Anchors: Address milestones and scenarios
4. Reflective Close: Motivational insights and questions
5. Well-Being Score: 1-10 score with brief explanation

Keep it uplifting yet honest, and personalized to the clients.
```

