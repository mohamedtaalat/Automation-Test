import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            web_driver = item.funcargs["driver"]
            screenshot_path = f"screen shots/{item.name}.png"
            web_driver.save_screenshot(screenshot_path)
            if hasattr(rep, "extra"):
                pytest_html = item.config.pluginmanager.getplugin('html')
                rep.extra.append(pytest_html.extras.image(screenshot_path))