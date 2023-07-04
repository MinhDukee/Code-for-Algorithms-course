import Config

# CONNECT TO INTERNET
def connect():
    if not sta.isconnected():
        print('connecting to network...')
        sta.active(True)
    sta.connect("Le Hong Lam", "19091972") #sta.connect('wifi ssid', 'wifi password')
    while not sta.isconnected():
        pass
    print('network config:', sta.ifconfig())

#LDR CLASS

class LDR:


    def __init__(self, pin, min_value=0, max_value=100):


        if min_value >= max_value:
            raise Exception('Min value is greater or equal to max value')


        self.adc = machine.ADC(machine.Pin(pin))

        self.adc.atten(machine.ADC.ATTN_11DB)

        self.min_value = min_value
        self.max_value = max_value

    def read(self):

        return self.adc.read()

    def value(self):

        return (self.max_value - self.min_value) * self.read() / 4095

# CALLBACK FUNCTION

def callback(req_id, method, params):
    print (f"RPC request received!\n'req_id': {req_id},\n 'method': {method},\n 'params': {params})")
    led.value(1)
    time.sleep(1)
    led.value(0)
    

    