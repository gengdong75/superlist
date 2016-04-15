from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def setDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪斯听说有一个在线待办事项应用
        #她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        #网页的标题和头部包含'to-do' 
        self.assertIn('to-do' , self.browser.title)
        self.fail('finish the test!')

if __name__ == '__main__':
    unittest.main()

#应用邀请她输入一个待办事项
#她在一个文本框中输入“buy peacock feathers”
#她按回车后页面更新了，代办事项表格中显示了“1:buy peacock feathers”

