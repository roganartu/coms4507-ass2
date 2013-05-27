from vstp_server import *
import struct

aes = AESEncryptionHandler(32)

keybase = "VSTPSERVER"
date = "20130221"
ip="172160"

plaintext = "exit"
msg = "9d513c622d0acf92986050f3bf0811b8ec4c78b1".decode("hex")

print "message len is " + str(len(msg)) + " bytes"

i = long(0)
rand = 10
lastOctet = 240

rand = 10
while rand <= 74:

	kb = keybase + date + ip + str(lastOctet) + str(rand);

	print "keybase: " + kb + " len " + str(len(kb))
	
	i = long(0)
	while i < (2**(8*(32-len(kb))) - 1):
		
		key = kb + struct.pack("L", i)[0:3]
		
		aes.sessionKey = key
		decoded = aes.AESDecryptString(msg)

		if decoded == plaintext:
			print "Possible Key Found!"
			print key.encode("hex")
		
			print "The message was '" + decoded + "'"
		i += 1
	rand += 1
