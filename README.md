# Notion Team Members Automation

## Overview

This project automates fetching and parsing team members from Notion using Playwright.
The extracted details include:

- **Name**
- **Email**
- **Role**
- **Created At**: (Joining Date) (⚠️ Not available via UI scraping)

## Initial Approach: API Tracking via Network Tab

Initially, the task was to extract team members details by identifying the API endpoint through the browser’s Developer Tools (Network tab and enable both XHR filter, preserve log). However, this approach failed due to:

### Challenges

1. No Exposed API Endpoint
2. Request Headers & Authentication: The API requests were internally authenticated, making it difficult to replicate them programmatically.
3. Multiple Attempts: Despite several tries, I was unable to track a stable API endpoint that provided the required details.

## Alternative Approach: UI Scraping

Since API tracking was not feasible, the alternative approach involved **scraping data directly from the UI**:

- The script navigates to the **Notion** -> **Settings** -> **People** page.
- It extracts data from the table
- It handles pagination by clicking "**Load More**" until all members are retrieved

### Challenges
Why "**Created At**" (Joining Date) Couldn't Be Extracted??

The Created At field is internal metadata and is not displayed anywhere in the UI.
Since scraping works by extracting visible elements from the DOM, this field remains inaccessible.

## Setup and Usage

### Clone the Repository
```bash
git clone https://github.com/VenkateshP23/Notion-Team-Members-Automation.git
```

### Install Dependencies
Ensure Python is installed, then install the required dependencies using:
```bash
pip install -r requirements.txt
```

### Save Notion Login Session
Run the following script to manually log in to Notion and save the session:
```bash
python save_session.py
```
Once logged in successfully, press Enter in the terminal.

### Run the Automation Script
To fetch the team members, execute:
```bash
python get_team_members.py
```
This will generate a JSON file containing the extracted data(**notion_team_members.json**).

### Error Handling & Edge Cases

- If Notion session expires, re-run login_session.py to save a new session.
- If "Load More" button doesn't appear, it means all members are already visible.
- If some fields are missing, they will be marked as "N/A" in the output.

## Conclusion

Although the API-based approach would have been more efficient, it was not feasible due to authentication restrictions. Instead, the UI scraping method successfully retrieves Name, Email, and Role for all members in a Notion workspace.