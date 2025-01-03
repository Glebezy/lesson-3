import pytest
from selene import browser


@pytest.fixture()
def browser_setup():
    browser.config.window_width = 1024
    browser.config.window_height = 768
