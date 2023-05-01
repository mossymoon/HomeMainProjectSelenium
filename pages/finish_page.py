from base.base_page import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def finish(self):
        self.get_current_url()
        self.assert_url('https://domkniginn.ru/site/cart')
        self.get_screenshot()