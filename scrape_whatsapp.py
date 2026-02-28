import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    print("Setting up Chrome...")
    chrome_options = Options()
    # Remove headless so you can scan the QR code
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    print("Navigating to WhatsApp Web...")
    driver.get("https://web.whatsapp.com/")

    print("Please scan the QR code to log in.")
    print("Waiting 30 seconds for you to scan and the page to load...")
    time.sleep(60)

    print("Saving the page source to 'whatsapp_source.html'...")
    with open("whatsapp_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Page source saved successfully! You can now close the browser.")
    driver.quit()

if __name__ == "__main__":
    main()
