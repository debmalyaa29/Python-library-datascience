import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger("ArithmaticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Subtract {a}-{b}={result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiply {a} * {b} = {result}")
    return result

add(10,20)
subtract(20,12)
multiply(10,20)