from flask import Flask, jsonify
app = Flask(__name__)

import RPi.GPIO as GPIO
import time

print("__name__: ", __name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/tasks")
def list_tasks():
    tasks = [{"name": "task1"}, {"name": "task2"}]
    return jsonify(tasks)

@app.route("/blinkLed")
def blink_led():
    pin = 21         # The pin connected to the LED
    iterations = 10  # The number of times to blink
    interval = .25   # The length of time to blink on or off
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)

    # The parameters to "range" are inclusive and exclusive, respectively,
    #  so to go from 1 to 10 we have to use 1 and 11 (add 1 to the max)
    for x in range(1, iterations+1):
    
        print("Loop %d: LED on" % (x))
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(interval)
    
        print("Loop %d: LED off" % (x))
        GPIO.output(pin, GPIO.LOW)
        time.sleep(interval)
    return "done!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
