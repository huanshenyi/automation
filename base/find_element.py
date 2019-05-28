from util.read_ini import ReadIni
import os

class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split('>')[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
            elif by == "className":
                return self.driver.find_element_by_class_name(value)
        except:
            # file_path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\img\%s.png" % value
            # self.driver.save_screenshot(file_path)
            return None

if __name__ == '__main__':
    test = FindElement()
    test.get_element("register_button")

