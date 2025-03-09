import unittest
import time 
import sys
sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class testDeleteTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def test_delete_task(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/login.html")    

       

        # Đăng nhập vào hệ thống
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "emailSignin")))
        driver.find_element(By.ID, "emailSignin").send_keys("tanhaorn@gmail.com")  # Nhập email
        driver.find_element(By.ID, "passwordSignin").send_keys("123456ae")  # Nhập mật khẩu
        login_button = driver.find_element(By.ID, "btn_signin")
        driver.execute_script("arguments[0].click();", login_button)  # Click nút đăng nhập

         # Kiểm tra đăng nhập thành công bằng cách xác minh URL
        WebDriverWait(driver, 10).until(EC.url_contains("index.html"))
        
        # Kiểm tra có task nào tồn tại không
        tasks = driver.find_elements(By.CLASS_NAME, "task-item-trash")
        if not tasks:
            print(" Khong tim thay task nao de xoa !")
            self.fail("Khong co task nao de xoa")

        # Nhấn vào nút xóa của task đầu tiên
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "task-item-trash"))
        )

        # Tìm công việc cần xóa
        task_to_delete = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//p[text()='Học Selenium']/ancestor::div[contains(@class, 'task-item')]//i[contains(@class, 'task-item-trash')]"
            ))
        )

        driver.execute_script("arguments[0].click();", task_to_delete)  # Click nút xóa
        
        # Kiểm tra xem task đã bị xóa chưa
        time.sleep(2)  # Chờ DOM cập nhật
        remaining_tasks = driver.find_elements(By.CLASS_NAME, "task-item-trash")
        self.assertLess(len(remaining_tasks), len(tasks), "Công việc chưa bị xóa thành công")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)  # Chờ một chút trước khi đóng trình duyệt
        cls.driver.quit()  # Đóng trình duyệt

if __name__ == "__main__":
    unittest.main()    
