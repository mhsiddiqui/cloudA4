from flask import Flask, render_template, redirect
from forms import MyForm
from flask import request
import cmath
import socket
import sys
import socket
import fcntl
import struct

app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'


@app.route('/')
def index():
    form = MyForm()
    return render_template('index.html',
                           title='Home',
                           form=form)


@app.route('/get_equation_solution', methods=['POST', 'GET'])
def get_equation_solution():
    a = float(request.values.get('a'))
    b = float(request.values.get('b') if request.values.get('b') != '' else 0)
    c = float(request.values.get('c') if request.values.get('c') != '' else 0)
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return render_template('result.html',
                           a=a,
                           b=b,
                           c=c,
                           sol1=sol1,
                           sol2=sol2,
                           ip=get_ip_address())


def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        try:
            ip = get_ip_address_with_eth0_wlan('eth0')
        except Exception:
            ip = get_ip_address_with_eth0_wlan('wlan0')
    return ip


def get_ip_address_with_eth0_wlan(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


if __name__ == '__main__':
    arg = sys.argv
    app.run(host=arg[1], port=int(arg[2]))
