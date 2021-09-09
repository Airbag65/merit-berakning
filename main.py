from Kurs import Kurs
import berakna
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time


user_username = ""
user_password = ""


def user_info():
	global user_username, user_password
	user_username = input("Ange ditt användarnamn: ")
	user_password = getpass.getpass("Ange ditt lösenord: ")

def login():
	global user_username, user_password
	#soup = BeautifulSoup()
	driver = webdriver.Chrome()
	driver.get("https://barnomsorg.linkoping.se/Default.asp?page=auth/common/login")
	username_field = driver.find_element_by_name("username")
	password_field = driver.find_element_by_name("password")
	username_field.send_keys(user_username)
	password_field.send_keys(user_password)
	password_field.send_keys(Keys.ENTER)
	time.sleep(2)
	driver.get("https://barnomsorg.linkoping.se/Default.asp?page=gy/bas/studyplan")
	time.sleep(10)


def get_studyplan():
	pass


def main():
	user_info()
	login()
	get_studyplan()

if (__name__ == "__main__"):
	main()