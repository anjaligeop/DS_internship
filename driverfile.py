def findElement(name):
    type=name.split(",")
    if type[1].upper()=="TEXT":
        return "driver.find_element_by_link_text('{}')".format(type[0])
    elif type[1].upper()=="ID":
        return "driver.find_element_by_id('{}')".format(type[0])
    elif type[1].upper()=="XPATH":
        return "driver.find_element_by_xpath(\"{}\")".format(type[0])
    elif type[1].upper()=="CSS":
        return "driver.find_element_by_css_selector(\"{}\")".format(type[0])
    elif type[1].upper()=="NAME":
        return "driver.find_element_by_name(\"{}\")".format(type[0])
