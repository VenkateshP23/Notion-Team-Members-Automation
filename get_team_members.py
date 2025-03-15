from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
import time

def scrape_notion_team_members():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context(storage_state="notion_session.json")
            page = context.new_page()

            # Navigate to Notion Settings -> People
            page.goto("https://www.notion.so/1b5b6e60ad12800e921ac07a23ae37ab")
            
            #Ensure page loads and session is valid
            page.wait_for_selector('text="Settings"').click()
            
            #click on "Settings" and the "People"
            page.wait_for_selector('text="People"').click()

            # Ensure member table loads 
            page.wait_for_selector("tr")

            # Handle pagination with 'Load More' button
            while True:
                load_more_button = page.locator("div:text('Load more')")
                if load_more_button.count() > 0 and load_more_button.is_visible():
                    print("Clicking 'Load More'...")
                    load_more_button.click()
                    time.sleep(2)
                else:
                    break  

            # Extract member details from the table
            rows = page.locator("tr").all()
            members = []
        
            for row in rows:
                columns = row.locator("td").all()
            
                if len(columns) >= 3: 
                    # Extracting Name, Email, Role (Created_at not available in UI) 
                    email_element = columns[0].locator("div[title]").first  
                    email = email_element.text_content().strip() if email_element else "N/A"
                    role = columns[3].text_content().strip()
                
                    # Extract Name from Email
                    name = email.split("@")[0] if email != "N/A" else "Unknown"


                    members.append({
                        "Name": name,
                        "Email": email,
                        "Role": role,
                    })

            # Save extracted data as JSON
            with open("notion_team_members.json", "w") as f:
                json.dump(members, f, indent=4)

            print("Scraping complete! Data saved to notion_team_members.json")
        
        except Exception as e:
            print(f"Unexpected Error: {e}")
        
        finally:
            browser.close()
            
if __name__ == "__main__":
    scrape_notion_team_members()
