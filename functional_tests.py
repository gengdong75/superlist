from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.assertIn('To-Do' , self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请他输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #她在文本框输入“buy peacock feathers”
        inputbox.send_keys('buy peacock feathers')

        #她按回车界面更新，待办事项表格中显示‘1:buy peacock feathers’
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1:buy peacock feathers' for row in rows),"new to-do item did not appear in table")

        #页面中又显示了文本框可以输入其他事项，她输入了‘use peacock feathers to make a fly’

        self.fail('finish the test!')

if __name__ == '__main__':
    unittest.main()

#应用邀请她输入一个待办事项
#她在一个文本框中输入“buy peacock feathers”
#她按回车后页面更新了，代办事项表格中显示了“1:buy peacock feathers”

