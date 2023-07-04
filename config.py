#MQTT Variables
My_Access_Token = 'oCMUGdNQecGtXwXjaykX'

credentials = {'user': 'Minh Duc Le Tran', 'password': '19091972'}

#MACHINES
i2 = machine.SoftI2C(scl=machine.Pin(27), sda=machine.Pin(25)) 
bmp = BMP180(i2)
UPDATE_TIME_INTERVAL = 5000 # in ms unit
last_update = time.ticks_ms()
led = machine.Pin(2, machine.Pin.OUT)

# HTTPS REQUEST FOR LOCATION
location_info = requests.get('http://ipinfo.io/json').json()
loc = location_info['loc'].split(",")
client.set_server_side_rpc_request_handler(callback)

