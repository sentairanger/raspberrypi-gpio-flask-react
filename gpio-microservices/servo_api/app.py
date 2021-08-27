from flask import Flask, jsonify, make_response, redirect

from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from .services.servoposition import get_servoposition

factory = PiGPIOFactory(host='192.168.0.10')
servo = Servo(27, pin_factory=factory)

app = Flask(__name__)

# Mozilla provides good references for Access Control at:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

@app.route('/api/servoposition', methods=['GET'])
def servoposition():
    """Return a JSON response for all employees."""
    position = {
        "position": get_servoposition()
        
    }
    # JSONify response
    response = make_response(jsonify(position))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response

@app.route('/api/min')
def servomin():
    servo.min()
    return redirect('http://localhost:3000', code=302)

@app.route('/api/mid')
def servomid():
    servo.mid()
    return redirect('http://localhost:3000', code=302)

@app.route('/api/max')
def servomax():
    servo.max()
    return redirect('http://localhost:3000', code=302)
    



