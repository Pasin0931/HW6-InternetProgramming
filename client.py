import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Attempting connection...")
s.connect(('10.31.130.49', 104))
print("OK!")

print("Please specify the amount of money and currency")
amount = int(input("Amount of money: "))
curr = input("Type of currency: ").upper()
send_inf = f"{amount} {curr}"
s.send(send_inf.encode("utf-8"))

time.sleep(0.5)
msg=s.recv(1024)
print(msg.decode("utf-8"))
s.close()

# Client: Siraphob Phonphakdee 681054930