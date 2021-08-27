from flask import Flask, jsonify, make_response, redirect

from gpiozero import OutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from .services.motordirection import get_motordirection

factory2 = PiGPIOFactory(host='192.168.0.21')

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

app = Flask(__name__)

# Mozilla provides good references for Access Control at:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

@app.route('/api/motordirection', methods=['GET'])
def motordirection():
    """Return a JSON response for all employees."""
    direction = {
        "position": get_motordirection()
        
    }
    # JSONify response
    response = make_response(jsonify(direction))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response

@app.route('/api/up')
def north():
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()
    return redirect('http://localhost:3000', code=302)


# backwards
@app.route('/api/down')
def south():
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()
    return redirect('http://localhost:3000', code=302)

#right
@app.route('/api/right')
def east():
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()
    return redirect('http://localhost:3000', code=302)

#left
@app.route('/api/left')
def west():
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()
    return redirect('http://localhost:3000', code=302)

@app.route('/api/stop')
def stop_two():
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    return redirect('http://localhost:3000', code=302)




