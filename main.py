from selenium import webdriver
import boto3

val = True

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')


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


def func_exit():
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

# Process messages by printing out body
while (val):
    for message in queue.receive_messages():
        # Print out the body of the message
        msg = '{0}'.format(message.body)
        if msg == 'func_up_full':
            func_up_full()

        elif msg == 'func_down_full':
            func_down_full()

        elif msg == 'func_up_normal':
            func_up_normal()

        elif msg == 'func_down_normal':
            func_down_normal()

        elif msg == 'func_up_abit':
            func_up_abit()

        elif msg == 'func_down_abit':
            func_down_abit()

        elif msg == 'func_exit':
            func_exit()
            val = False

        elif msg == 'func_forward':
            func_forward()

        elif msg == 'func_back':
            func_back()

        # elif msg == 'func_find_link':

        print(msg)
        # Let the queue know that the message is processed
        message.delete()
