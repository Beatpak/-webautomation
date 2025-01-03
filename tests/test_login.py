import pytest
from playwright.sync_api import Page, expect

# def test_login_page(page: Page):
#     # Inspector를 위한 일시 중지
#     page.pause()
    
#     # dev 파트너스 진입
#     page.goto("https://dev-partners.qmarket.me/login")

def test_login_page(login_page: Page):
    login_page.pause()