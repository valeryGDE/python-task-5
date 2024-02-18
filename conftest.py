import pytest
from selene import browser, by, be


@pytest.fixture()
def precondition():
    browser.open('https://demoqa.com/automation-practice-form')
    if browser.element(by.text('Consent')).matching(be.visible):
        browser.element(by.text('Consent')).click()
    yield
    browser.driver.quit()