import logging
import numpy as np
from PIL import Image
import io
import azure.functions as func
import json

# Import helper script
from .predict import predict_image_from_url

def main(req: func.HttpRequest) -> func.HttpResponse:
    image_input = req.get_body()# this returns a binary file
    logging.info('Image received: ' + str(type(image_input)))

    
          
    results = predict_image_from_url(image_input)
    
    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    
    return func.HttpResponse(json.dumps(results), headers = headers)


