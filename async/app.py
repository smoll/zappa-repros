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


@app.route('/sns')
def spike_sns():
    """ Fire off an SNS notification """
    import boto3
    sns_client = boto3.client('sns')
    return sns_client.publish(TopicArn='arn:aws:sns:us-east-1:517753740273:spike-topic', Message='foo')


if __name__ == "__main__":
    app.run()
