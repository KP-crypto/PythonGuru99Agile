import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename="C:/Users/Acer/PycharmProjects/AgileDevelopment/Logs/automation.log",filemode='a',level=logging.INFO,format='%(asctime)s %(message)s')
