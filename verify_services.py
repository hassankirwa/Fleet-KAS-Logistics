from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///app/services.html")

    # Check for the correct title
    if "Kas Logistics - Services" not in page.title():
        raise Exception(f"Expected 'Kas Logistics - Services' in title, but got '{page.title()}'")

    # Check for the correct navigation
    nav_links = page.locator('.nav li a')
    expected_links = ["Home", "About", "Services", "Contact"]
    for i, link in enumerate(expected_links):
        if nav_links.nth(i).inner_text() != link:
            raise Exception(f"Expected navigation link '{link}', but got '{nav_links.nth(i).inner_text()}'")

    # Check that the "Services" link is active
    if "active" not in nav_links.nth(2).get_attribute("class"):
        raise Exception("The 'Services' navigation link is not active")

    # Check for the correct page heading
    if page.locator('.page-heading h4').inner_text() != "Our Services":
        raise Exception(f"Expected page heading 'Our Services', but got '{page.locator('.page-heading h4').inner_text()}'")

    # Check for the presence of the services section
    if page.locator('.amazing-deals').count() == 0:
        raise Exception("The services section is not present on the page")

    # Take a screenshot
    page.screenshot(path="verification/kas-logistics-services.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
