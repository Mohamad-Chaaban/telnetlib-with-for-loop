import telnetlib

user = "cisco"
password = "cisco"

HOST = ['192.168.232.127', '10.10.10.2']

for div in HOST:
    print('\n #### Connecting to the device' + div.strip() + '####\n')
    tn = telnetlib.Telnet(div)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    tn.write(b"configure terminal\n")
    tn.write(b"int loopb 1\n")
    tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))