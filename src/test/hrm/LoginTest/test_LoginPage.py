from src.main.hrm.pages.LoginPage import LogInPage
import pytest

@pytest.mark.usefixtures("setup")
class Test_login:
    
    @pytest.mark.smoke
    def test_valid_login(self):
        
        LogInPage(self.driver).do_login("Admin", "admin123")
        print("This is valid login test")

    # def test_invalid_login(self):
    #     print("This is invalid login test")