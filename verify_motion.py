from playwright.sync_api import sync_playwright

def verify_motion(page):
    # Set viewport to mobile
    page.set_viewport_size({"width": 390, "height": 844})

    page.goto("http://localhost:8080")

    # Wait for the motion section
    page.wait_for_selector("#motion")

    # Scroll to the motion section
    motion_section = page.locator("#motion")
    motion_section.scroll_into_view_if_needed()

    page.wait_for_timeout(1000)

    # Find the carousel container.
    # We look for the overflow-x-auto container inside #motion
    carousel = page.locator("#motion .md\\:hidden .overflow-x-auto")

    if carousel.is_visible():
        print("Carousel found")
        # Scroll horizontally to reveal second item partially or fully
        # Item width is 70vw ~ 273px. Gap is 1rem ~ 16px.
        # Scroll by approx 290px to snap to next?
        carousel.evaluate("node => node.scrollBy(290, 0)")
        page.wait_for_timeout(1000)

    page.screenshot(path="verification_mobile_scrolled.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_motion(page)
        finally:
            browser.close()
