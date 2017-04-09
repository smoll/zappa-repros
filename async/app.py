import logging
import time
import uuid
from flask import Flask
from zappa.async import task

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@task
def make_pie():
    """ This takes a long time! """
    time.sleep(5)
    logger.info('pie %s has been baked!' % uuid.uuid4())


@app.route('/api/order/pie')
def order_pie():
    """ This returns immediately! """
    make_pie()
    return "Your pie is being made!"


if __name__ == "__main__":
    app.run()
