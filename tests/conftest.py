import pytest
from selenium import webdriver
import os
from pageobjects.Warranty import GetWarrantyPage

dirname = os.path.dirname(os.path.abspath(__file__))
_driver = None


@pytest.fixture(scope="package")
def driver():
    options = {
        "ignore_http_methods": [
            "HEAD",
            "OPTIONS"
        ]  # Ignore all HEAD and OPTIONS requests
    }

    option = webdriver.ChromeOptions()
    # 防止顯示無用的日志
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(options=option , executable_path=dirname + "\\drivers\\chromedriver.exe")
   
    
    driver.maximize_window()

    global _driver
    _driver = driver

    yield driver

    # driver.close()

@pytest.fixture(scope="class")
def frontend_url(variables, driver):
    url = variables.get("frontend", {})
    navigation  = url.get("navigation")
    

    driver.get(navigation)

    # Warranty_page = GetWarrantyPage(driver)

@pytest.fixture(scope="class")
def bitopro_url(variables, driver):
    url = variables.get("frontend_bitopro", {})
    navigation  = url.get("navigation")
    

    driver.get(navigation)   


from py._xmlgen import html


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = (
                    '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    # id = item.callspec.id
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


def _capture_screenshot():
    """截图保存为base64"""
    global _driver
    return _driver.get_screenshot_as_base64()