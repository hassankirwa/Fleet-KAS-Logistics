
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///app/about.html")

    # Check the title
    assert page.title() == "Kas Logistics - About Us"

    # Check the navigation links
    nav_links = page.locator(".nav a").all_inner_texts()
    assert nav_links == ["Home", "About", "Services", "Contact"]

    # Check the main banner content
    assert page.locator(".about-main-content h4").inner_text() == "Your Trusted Logistics Partner"
    assert page.locator(".about-main-content h2").inner_text() == "Welcome To Kas Logistics"
    assert "leading provider of logistics" in page.locator(".about-main-content p").inner_text()

    # Check the footer
    assert "Kas Logistics" in page.locator("footer p").inner_text()

    page.screenshot(path="/home/jules/verification/kas-logistics-about.png")
    browser.close()

print("About page verification successful!")
