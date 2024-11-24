from selene import browser, be, have
from fixtures import browser_setup


def test_google_found(browser_setup):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    (browser.element('[id="rcnt"]').should(be.visible)
     .should(have.text('User-oriented Web UI browser tests in Python')))


def test_google_not_found():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('fsdnfusi23uniufgbirbuei').press_enter()
    browser.element('[id="rcnt"]').should(be.visible).should(have.text('did not match any documents'))
