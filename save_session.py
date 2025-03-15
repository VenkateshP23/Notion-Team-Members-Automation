from playwright.sync_api import sync_playwright

def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to Notion login page
        page.goto("https://www.notion.so/login")
        print("Log in manually and then press Enter here...")
        input("Press Enter after successful login: ")

        # Save session for future use
        context.storage_state(path="notion_session.json")
        print("Session saved successfully!")
        
        browser.close()

if __name__ == "__main__":
    save_session()
