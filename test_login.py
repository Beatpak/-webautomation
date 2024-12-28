import pytest
from playwright.sync_api import Page, expect

def test_naver_search(page: Page):
    # 네이버 메인 페이지로 이동
    page.goto("https://www.naver.com")
    
    # 페이지 타이틀 확인
    expect(page).to_have_title("NAVER")
    
    # 검색창 찾기
    search_input = page.get_by_role("textbox", name="검색어 입력")
    
    # 검색어 입력
    search_input.fill("playwright python")
    
    # 검색 버튼 클릭
    page.get_by_role("button", name="검색").click()
    
    # 검색 결과 페이지로 이동했는지 확인
    expect(page.get_by_role("main")).to_be_visible()
    
    # 스크린샷 저장
    page.screenshot(path="search_results.png")