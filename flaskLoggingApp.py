
import logging
from google.cloud import logging 
from flask import Flask
app = Flask(__name__)


@app.route("/hello")
def getHello():
  
    client = logging.Client()

    logger = client.logger(logger_name)
    
    logger.log_struct(
        {
            "msg": "Hello Flipkart Health",
            "location":"Bangalore"
        }
    )

    client.setup_logging()

    text = "Hello GCP!"

    
    logging.warning(text)

    return "Hello Flipkart"
  


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8090")