import time


class StaticRisk:
    """判断选择食品类型，并点击"""
    def __init__(self, driver, tick):
        self.driver = driver
        self.tick = tick

    def run(self, food_type):
        driver.find_element_by_xpath('//*[@id="onclickbutton"]').click()
        time.sleep(tick)

        check_type_idx = -1
        for curr_type_idx in range(2, 9):  # 序号是[2,...,8]
            curr_text = self.driver.find_element_by_xpath(
                '/html/body/div[15]/div[2]/div[1]/table/tbody/tr[{}]/td[2]'.format(curr_type_idx)).text
            if curr_text == food_type:
                check_type_idx = curr_type_idx
                print("已经选择了序号: ", check_type_idx)
                break

        self.driver.find_element_by_xpath(
            '/html/body/div[15]/div[2]/div[1]/table/tbody/tr[{}]/td[1]/input'.format(check_type_idx)).click()
        time.sleep(tick)
        # 保存静态风险
        self.driver.find_element_by_xpath('/html/body/div[14]/div[2]/div[3]/ul/li[1]/div/div/button').click()
        time.sleep(loading)

        # 保存静态风险
        # driver.find_element_by_xpath('/html/body/div[14]/div[2]/div[3]/ul/li[1]/div/div/button').click()
        # time.sleep(loading)