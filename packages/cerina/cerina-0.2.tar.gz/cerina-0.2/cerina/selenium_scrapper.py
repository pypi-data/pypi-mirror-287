from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumScraper:
    def __init__(self, name: str, base_url: str, class_id: str = None, headless: bool = True):
        self.name = name
        self.base_url = base_url
        self.class_id = class_id
        self.headless = headless
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def scrape(self, path: str) -> str:
        url = f"{self.base_url}{path}"
        self.driver.get(url)
        
        try:
            if self.class_id:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, self.class_id))
                )
                elements = self.driver.find_elements(By.CLASS_NAME, self.class_id)
                content = "\n".join([element.text for element in elements])
            else:
                content = self.driver.page_source
        except Exception as e:
            raise Exception(f"Failed to scrape {url}. Error: {str(e)}")
        finally:
            self.driver.quit()
        
        return content

    async def use_tool(self, query: str) -> str:
        # For simplicity, let's assume the query is directly the path to scrape
        return self.scrape(query)
