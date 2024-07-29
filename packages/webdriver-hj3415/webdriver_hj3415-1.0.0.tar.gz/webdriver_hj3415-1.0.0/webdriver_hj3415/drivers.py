import sys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils_hj3415 import utils

import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


os_n_browser = {
    "Darwin": "safari",
    "Linux": "chrome",
    "Windows": "edge"
}


def get(browser_type: str = '') -> WebDriver:
    if browser_type == '':
        # 운영체제별로 적절한 드라이버를 받아온다.
        os_it = utils.get_pc_info()['os']
        browser_it = os_n_browser[os_it]
    else:
        assert browser_type in os_n_browser.values(), f"Browser type must be among {os_n_browser.values()}."
        browser_it = browser_type

    if browser_it == 'safari':
        driver = get_safari()
    elif browser_it == 'edge':
        driver = get_edge()
    elif browser_it == 'chrome':
        driver = get_chrome()
    return driver


def get_safari() -> WebDriver:
    try:
        driver = webdriver.Safari()
    except:
        raise Exception("Fail to get safari driver..(You should safari setting first, 설정/개발자/원격자동화허용 on)")
    else:
        print(f'Get safari driver successfully...')
        return driver


def get_edge() -> WebDriver:
    try:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    except:
        raise Exception("Fail to get edge driver..")
    else:
        print(f'Get edge driver successfully...')
        return driver


def get_chrome(temp_dir: str = '', headless=True, geolocation=False) -> WebDriver:
    """ 크롬 드라이버를 반환
    Args:
        temp_dir : 크롬에서 다운받은 파일을 저장하는 임시디렉토리 경로(주로 krx_hj3415에서 사용)
        headless : 크롬 옵션 headless 여부
        use_tor :  토르 프록시 사용 여부

    """
    # 크롬드라이버 옵션 세팅
    options = webdriver.ChromeOptions()
    # reference from https://gmyankee.tistory.com/240
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-extensions")
    options.add_argument('--window-size=1920,1080')
    if headless:
        # referred from https://www.selenium.dev/blog/2023/headless-is-going-away/
        options.add_argument('--headless=new')

    prefs = {}

    if geolocation:
        # https://copyprogramming.com/howto/how-to-enable-geo-location-by-default-using-selenium-duplicate

        prefs.update(
            {
                'profile.default_content_setting_values': {'notifications': 1, 'geolocation': 1},
                'profile.managed_default_content_settings': {'geolocation': 1},
            }
        )

    if temp_dir != '':
        logger.info(f'Set temp dir : {temp_dir}')
        # referred from https://stackoverflow.com/questions/71716460/how-to-change-download-directory-location-path-in-selenium-using-chrome
        prefs.update({'download.default_directory': temp_dir,
                      "download.prompt_for_download": False,
                      "download.directory_upgrade": True})

    options.add_experimental_option('prefs', prefs)

    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    capabilities = DesiredCapabilities().CHROME
    capabilities.update(options.to_capabilities())


    # 크롬드라이버 준비
    # https://pypi.org/project/webdriver-manager/
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    except:
        raise Exception("Fail to get chrome driver..")
    else:
        print(f'Get chrome driver successfully... headless : {headless}, geolocation : {geolocation}')
        return driver