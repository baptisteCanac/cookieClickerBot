# www.github.com/baptisteCanac
from selenium import webdriver
import time

print("Enter \"random\" if you want a random name")
name = input("Enter your bakery's name:")

url = "https://orteil.dashnet.org/cookieclicker/"

driver = webdriver.Chrome(executable_path="driver/chromedriver_win32/chromedriver.exe")
driver.get(url)

i = 0 #compteur de clicks

bakeryName = driver.find_element_by_id("bakeryName")
bakeryName.click()

if name == "random":
	randomName = driver.find_element_by_id("promptOption1")
	randomName.click()

	confirmName = driver.find_element_by_id("promptOption0")
	confirmName.click()
else:
	bakeryNameInput = driver.find_element_by_id("bakeryNameInput")
	bakeryNameInput.send_keys(name)

	confirmName = driver.find_element_by_id("promptOption0")
	confirmName.click()


def mouse():
	mouseObject = driver.find_element_by_id("product0")
	mouseObject.click()

def grandma():
	grandmaObject = driver.find_element_by_id("product1")
	grandmaObject.click()

def farm():
	farmObject = driver.find_element_by_id("product2")
	farmObject.click()

def mine():
	mineObject = driver.find_element_by_id("product3")
	mineObject.click()

def factory():
	factoryObject = driver.find_element_by_id("product4")
	factoryObject.click()

def delay():
	time.sleep(5)
while True:
	i += 1
	cookie = driver.find_element_by_id("bigCookie")
	cookie.click()
	mouse()
	grandma()
	try:
		farm()
	except Exception as e:
		print("farm is locked")
	try:
		mine()
	except Exception as e:
		print("mine is locked")
	try:
		factory()
	except Exception as e:
		print("factory is locked")
