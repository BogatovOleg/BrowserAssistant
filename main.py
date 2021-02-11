from selenium import webdriver
import chromedriver_binary
driverr = webdriver.Chrome()
driverr.maximize_window()
driverr.get('https://ru.wikipedia.org/wiki/Проверка_концепции')
output = open('output.txt', 'w', encoding='utf-8')
dict = {}
for i in driverr.find_elements_by_tag_name('a'):
    if i.get_attribute('title') != '':
        dict[str(i.get_attribute('title'))] = str(i.get_attribute('href'))
for i in dict: output.write(i + ' - ' + dict[i] + '\n')
driverr.get(dict['Машинное обучение'])
if driverr.current_url == dict['Машинное обучение']:
    print('true')
else:
    print('false')
driverr.quit()