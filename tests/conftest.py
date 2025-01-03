# conftest.py
# import playwright
# import pytest
# from playwright.sync_api import Page, Playwright, expect

# @pytest.fixture
# def login_page(page: Page):
#     # 로그인 페이지로 이동
#     page.goto("https://dev-partners.qmarket.me/login")

# import pytest
# from playwright.sync_api import Page, expect

# def browser_type_launch_args(browser_type_launch_args):
#     """브라우저 시작 옵션을 설정하는 fixture"""
#     return {
#         **browser_type_launch_args,
#         "headless": False,  # headless 모드 비활성화
#         "slow_mo": 1000,    # 액션 간 1초 딜레이 (선택사항)
#     }

# @pytest.fixture
# def login_page(page: Page):
#     # 로그인 페이지로 이동
#     page.goto("https://dev-partners.qmarket.me/login")
    
#     # 로그인 수행
#     page.get_by_placeholder("아이디를 입력해주세요.").fill("qmarket")
#     page.get_by_placeholder("비밀번호를 입력해주세요.").fill("qmarket!@#")
#     page.get_by_role("button", name="로그인").click()
    
#     return page
    
#     # 로그인 수행
#     # browser = playwright.chromium.launch(headless=False)
#     # context = browser.new_context()
#     # page.get_by_placeholder("아이디를 입력해주세요.").click()
#     # page.get_by_placeholder("아이디를 입력해주세요.").fill("qmarket")
#     # page.get_by_placeholder("비밀번호를 입력해주세요.").click()
#     # page.get_by_placeholder("비밀번호를 입력해주세요.").fill("qmarket!@#")
#     # page.get_by_role("button", name="로그인").click()

    
#     # # 로그인 완료 후 페이지 객체 반환
#     # return page

# conftest.py
import pytest, time
from playwright.sync_api import Page, expect, Playwright

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    time.sleep(3)
    page.close()

@pytest.fixture
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)  # 직접 브라우저 설정
    yield browser
    time.sleep(3)
    browser.close()

@pytest.fixture
def login_page(page: Page):
    # 로그인 페이지로 이동
    page.goto("https://dev-partners.qmarket.me/login")
    
    # 로그인 수행
    page.get_by_placeholder("아이디를 입력해주세요.").fill("qmarket")
    page.get_by_placeholder("비밀번호를 입력해주세요.").fill("qmarket!@#")
    page.get_by_role("button", name="로그인").click()
    
    return page