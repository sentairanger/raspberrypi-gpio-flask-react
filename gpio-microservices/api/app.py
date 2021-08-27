from flask import Flask, jsonify, make_response, redirect
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

from .services.ledstatus import get_ledstatus

factory = PiGPIOFactory(host='192.168.0.10')
led = LED(17, pin_factory=factory)

app = Flask(__name__)

# Mozilla provides good references for Access Control at:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

@app.route('/api/ledstatus', methods=['GET'])
def ledstatus():
    """Return a JSON response for all customers."""
    status = {
        "status": get_ledstatus()
    }
    # JSONify response
    response = make_response(jsonify(status))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response
    
@app.route('/api/ledon')
def ledon():
    led.on()
    return redirect('http://localhost:3000', code=302)

@app.route('/api/ledoff')
def ledoff():
    led.off()
    return redirect('http://localhost:3000', code=302)





