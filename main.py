from selenium import webdriver
from flask import Flask, request
import time
import logging
import json
'''
'''
application = Flask(__name__)
@application.route('/')
def hello_world():
    return 'Sup. Subscribe'

application.run()

'''
def func_up_full():
    my_driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
    return 0


def func_up_normal():
    my_driver.execute_script("window.scrollBy(0, -250);")
    return 0


def func_up_abit():
    my_driver.execute_script("window.scrollBy(0, -50);")
    return 0


def func_down_full():
    my_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return 0


def func_down_normal():
    my_driver.execute_script("window.scrollBy(0, 250);")
    return 0


def func_down_abit():
    my_driver.execute_script("window.scrollBy(0, 50);")
    return 0


def func_exit_browser():
    my_driver.quit()
    return 0


def func_forward():
    my_driver.forward()
    return 0


def func_back():
    my_driver.back()
    return 0


def func_get_a_link(value):
    my_driver.get(value)
    return 0


def func_find_link(value):
    output = open('output.txt', 'w', encoding='utf-8')
    dict = {}
    for i in my_driver.find_elements_by_tag_name('a'):
        if i.get_attribute('title') != '':
            dict[str(i.get_attribute('title'))] = str(i.get_attribute('href'))
    for i in dict:
        output.write(i + ' - ' + dict[i] + '\n')
    return dict[str(value)]


# тут нужно ввести ссылку на драйвер на вашем компьютере, если не настроен PATH
my_driver = webdriver.Edge("C:/Users/bogat/Downloads/edgedriver_win64/msedgedriver.exe")
my_driver.maximize_window()
my_driver.get('https://ru.wikipedia.org/wiki/Проверка_концепции')

func_get_a_link(func_find_link('Машинное обучение'))
time.sleep(2)
func_get_a_link('https://ru.wikipedia.org')
func_back()
time.sleep(2)
func_forward()

it = 0
while it != 10:
    time.sleep(2)
    func_down_abit()
    time.sleep(2)
    func_up_abit()
    time.sleep(2)
    func_down_full()
    time.sleep(2)
    func_up_full()
    time.sleep(2)
    func_down_normal()
    time.sleep(2)
    func_up_normal()
    it += 1
    print(it)
func_exit_browser()
'''
