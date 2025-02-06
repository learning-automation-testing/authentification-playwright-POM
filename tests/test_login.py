from pages.Login import Login_form
from playwright.sync_api import Page
import pytest
from pytest_bdd import scenarios , given


scenarios('../features/login.feature')
@given('the user is trying to login in to the website')
def test_login_standarduser(page:Page):
    loginpage= Login_form(page)
    loginpage.load('https://www.saucedemo.com/v1/')
    data = loginpage.responsbile_credentials('standard')
    loginpage.login(data)

def test_login_locked_out_user(page:Page):
    loginpage= Login_form(page)
    loginpage.load('https://www.saucedemo.com/v1/')
    data = loginpage.responsbile_credentials('locked_out')
    loginpage.login(data)

def test_login_problem_user(page:Page):
    loginpage= Login_form(page)
    loginpage.load('https://www.saucedemo.com/v1/')
    data = loginpage.responsbile_credentials('problem_user')
    loginpage.login(data) 

def test_login_performance_glitch(page:Page):
    loginpage= Login_form(page)
    loginpage.load('https://www.saucedemo.com/v1/')
    data = loginpage.responsbile_credentials('performance_glitch')
    loginpage.login(data)
    

