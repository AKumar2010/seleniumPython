
from src.test.hrm.LoginTest.test_LoginPage import test_login

def execute_tests():
    test = test_login()
    test.test_valid_login()



if __name__ == "__main__":
    execute_tests()