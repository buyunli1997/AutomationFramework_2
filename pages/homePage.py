class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.profile_link_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/ul[1]/li[1]"
        self.logout_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/ul[1]/li[1]/ul[1]/li[4]/a[1]"

    def click_profile(self):
        self.driver.find_element_by_xpath(self.profile_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()
