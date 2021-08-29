from time import sleep
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from celery import Celery
from db_controller import *
from config import *

CELERY_BROKER_URL = 'redis://:' + REDIS_PASS + '@' + REDIS_HOST + ':' + str(REDIS_PORT) + '/0'
celery = Celery('tasks', broker=CELERY_BROKER_URL)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls get_path_token every 30 seconds
    sender.add_periodic_task(60, get_path_token.s(), expires=20)


@celery.task
def get_path_token():
    options = {
        # Address of the machine running Selenium Wire.
        'addr': 'celery_worker'
    }
    driver = webdriver.Remote(
        command_executor='http://shub:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True},
        seleniumwire_options=options
    )

    driver.get("https://explorer.roninchain.com/txs")
    sleep(5)
    # Access requests via the `requests` attribute

    path_token = None
    for request in driver.requests:
        if request.response:
            if "_next/data/" in request.url and \
                    "tx/" in request.url and \
                    request.response.headers['Content-Type'] == "application/json" and \
                    request.response.status_code == 200:
                path_token = \
                    request.url.replace("https://explorer.roninchain.com/_next/data/", "").split("/tx/")[0]
    # driver.close()
    driver.quit()
    if path_token:
        active_token = RoninUrlPathController.get_active_path_url_token()
        for token in active_token :
            if token == path_token:
                print("token " + path_token + " already up to date.")
            else:
                # insert new token
                print("new token has been inserted in database.")
                RoninUrlPathController.insert_path_url_token(path_token)
    else:
        print("Error, we cannot get path token.")

    return path_token
