from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///app/reservation.html")

    # Check for the correct title
    if "Kas Logistics - Reservation" not in page.title():
        raise Exception(f"Expected 'Kas Logistics - Reservation' in title, but got '{page.title()}'")

    # Check for the correct navigation
    nav_links = page.locator('.nav li a')
    expected_links = ["Home", "About", "Services", "Reservation", "Contact"]
    for i, link in enumerate(expected_links):
        if nav_links.nth(i).inner_text() != link:
            raise Exception(f"Expected navigation link '{link}', but got '{nav_links.nth(i).inner_text()}'")

    # Check that the "Reservation" link is active
    if "active" not in nav_links.nth(3).get_attribute("class"):
        raise Exception("The 'Reservation' navigation link is not active")

    # Check for the correct page heading
    if page.locator('.second-page-heading h4').inner_text() != "Book Our Services Here":
        raise Exception(f"Expected page heading 'Book Our Services Here', but got '{page.locator('.second-page-heading h4').inner_text()}'")

    # Check for the presence of the reservation form
    if page.locator('.reservation-form').count() == 0:
        raise Exception("The reservation form is not present on the page")

    # Take a screenshot
    page.screenshot(path="verification/kas-logistics-reservation.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
