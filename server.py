import socket
import time
import datetime

currency = {
    "THB": 32.5,
    "USD": 1.0,
    "EUR": 0.87,
    "JPY": 155.0
}

ERROR_WRONG_CURRENCY = 'Wrong currency !'

print("starting server. . .")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 104))
s.listen(1)

conn,info = s.accept()
msg=conn.recv(1024).decode('utf-8').strip()

this_ = msg.split(" ")
amount_money = float(this_[0])
this_currency = this_[1].upper()

print(f'\nreceived "{msg}" from client !')

if this_currency in currency.keys():
    for key, val in currency.items():
        if key != this_currency:

            converted_money = amount_money / currency[this_currency] * val

            print(f'Sending -> {amount_money} {this_currency} = {converted_money:.2f} {key}')

            conn.send(f'{amount_money} {this_currency} = {converted_money:.2f} {key}\r\n'.encode())

    today = datetime.datetime.now()
    conn.send(str(today).encode())

    print(f'Sending -> {str(today)}\n')

else:
    print(ERROR_WRONG_CURRENCY)
    conn.send(ERROR_WRONG_CURRENCY.encode())

time.sleep(0.3)
conn.close()
s.close()

# Server: Pasin Makcharoen 6810545794