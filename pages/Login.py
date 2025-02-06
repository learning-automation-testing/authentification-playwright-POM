from playwright.sync_api import Page
from Data.login_data import standard_user, locked_out_user, problem_user, performance_glitch_user
class Login_form:

    def __init__(self, page:Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.locator("[data-test='password']")
        self.submit_button = page.locator('.btn_action')
        # print("tessst")

    def load(self, url):
        self.page.goto(url)

    def login(self, data):
        self.username.fill(list(data)[0])
        self.password.fill(list(data)[1])
        self.submit_button.click()

    def responsbile_credentials(self, method):
        match method:
            case 'standard':
                return standard_user
            case 'locked_out': 
                return locked_out_user
            case 'problem_user':
                return problem_user
            case 'performance_glitch':
                return performance_glitch_user
            case _:
                return 'pick an avialable method'