dump_file = open("/home/anjaligeorgep/Desktop/sample.txt", "r")
# store the contents of katalon dump in the form of 3 lists for iteration of each line
command = []
target = []
val = []
iter1 = dump_file.readlines()

for z in iter1:
    values = (z.split(" | "))  # delimiter
    if values[0] != "\n":
        command.append(values[0])
        target.append(values[1])
        if values[0] == "type" or values[0] == "select":
            val.append(values[2])
        else:
            val.append("0")

temp = open("/home/anjaligeorgep/Desktop/NAVIGATION.py", "w")  # open file to write selenium code

temp.write("from selenium import webdriver\n")
temp.write("from bs4 import BeautifulSoup\n")
temp.write("import os\n")
temp.write("import time\n")
temp.write("from selenium.webdriver.chrome.options import Options\n")
temp.write("from selenium.webdriver.support.ui import Select\n")
temp.write("options = Options()\n")
temp.write("options.add_argument(\"--headless\")\n")
temp.write('driver = webdriver.Chrome(executable_path="/home/anjaligeorgep/Desktop/perfios/chromedriver")\n')
# For headless mode: driver = webdriver.Chrome(chrome_options=options, executable_path="/home/anjaligeorgep/Desktop/perfios/chromedriver")
temp.write("driver.implicitly_wait(20)\n")

x=0 # index for html file name
def save_html(x):
    temp.write("a=driver.page_source\n")
    temp.write("file_nm=open('/home/anjaligeorgep/Desktop/perfios/html_files/file{}.html', 'w')\n".format(x))
    temp.write("file_nm.write(a)\n")

for a, b, c in zip(command, target, val):
    if a == "open":
        temp.write("driver.get('{}')\n".format(b))
        temp.write("parent = driver.current_window_handle\n")

    if a == "click" and b.startswith("//"):
        temp.write("driver.find_element_by_xpath(\"{}\").click()\n".format(b))

    if a == "click" and b.startswith("link"):
        temp.write("driver.find_element_by_link_text(\"{}\").click()\n".format(b[5:]))

    if a == "click" and b.startswith("id"):
        temp.write("driver.find_element_by_id(\"{}\").click()\n".format(b[3:]))

    if a == "click" and b.startswith("name"):
        temp.write("driver.find_element_by_name(\"{}\").click()\n".format(b[5:]))

    if a == "type" and b.startswith("id"):
        temp.write("driver.find_element_by_id('%s').send_keys('%s')\n" % (b[3:], c[:-1]))

    if a == "type" and b.startswith("//"):
        temp.write("driver.find_element_by_xpath('%s').send_keys('%s')\n" % (b,c[:-1]))
    if a == "select" and b.startswith("id") and c.startswith("label"):
        temp.write("Select(driver.find_element_by_id(\"{}\")).select_by_visible_text(\"{}\")\n".format(b[3:], c[6:-1]))



    if a == "selectWindow" and b.startswith("win_ser_1"):
        temp.write("child=driver.window_handles[1]\n")
        temp.write("driver.switch_to.window(child)\n")

    if a == "selectWindow" and b.startswith("win_ser_local"):
        temp.write("driver.switch_to.window(parent)\n")

    if a == "selectFrame" and b.startswith("index"):
        index=b[-1:]
        temp.write("index={}\n".format(b[-1:]))
        temp.write("time.sleep(5)\n")
        temp.write("driver.switch_to.frame({})\n".format(index))

    if a == "selectFrame" and b.startswith("relative=parent"):
        temp.write("driver.switch_to.default_content()\n")

    if a == "close" and b.startswith("win_ser_1"):
        temp.write("driver.close()\n")




