
import logging as pythonlogging
from google.cloud import logging 
from flask import Flask
app = Flask(__name__)


@app.route("/")
def getHello():
  
    client = logging.Client()

    logger = client.logger("service_1")
    
    logger.log_struct(
        {
            "msg": "Hello Flipkart Health",
            "location":"Bangalore"
        }
    )

    client.setup_logging()

    text = "Hello GCP!"
    pythonlogger = pythonlogging.getLogger("service_1")
    
    pythonlogger.warning(text)

    return "Hello Flipkart"
  


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8090")