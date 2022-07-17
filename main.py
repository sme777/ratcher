from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
class Artist:

	def __init__(self, name, home_page):
		self.name = name
		self.home_page = home_page
		self.scrapper = self.init_scrapper()
		self.tour_page = self.find_tour_site()
		
	def find_tour_site(self):
		return

	def find_tour_dates_cities(self):
		print(self.home_page)
		self.driver.get(self.home_page)

	def init_scrapper(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference('browser.download.manager.showWhenStarting', False)
		profile.set_preference("browser.helperApps.alwaysAsk.force", False)  
		driver = webdriver.Firefox(profile)
		return driver

class City:

	def __init__(self, name, state):
		self.name = name
		self.state = state


def read_artists():
	with open('artists.csv') as file:
		csv_reader = csv.reader(file, delimiter=',')
		next(csv_reader)
		for name, site in csv_reader:
			print(name, site)
			artist = Artist(name, site)

read_artists()