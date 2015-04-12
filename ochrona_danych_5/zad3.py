from Crypto.PublicKey import RSA
import sys

def generate():
	print 'filenames for: private key, public key:'
	fpriv, fpub = sys.stdin.readline()[: -1], sys.stdin.readline()[: -1]
	rsa_keys = RSA.generate(1024)
	pr_key = rsa_keys.exportKey('PEM')
	pub_key = rsa_keys.publickey().exportKey('PEM')
	print pr_key
	# pub_key = str(pub_key)
	print pub_key
	fpriv = open(fpriv, 'w')
	fpriv.write(pr_key)
	fpriv.close()
	fpub = open(fpub, 'w')
	fpub.write(pub_key)
	fpub.close()

def decrypt():
	print 'file with your private key:'
	f = sys.stdin.readline()[: -1]
	f = open(f, 'r')
	key = RSA.importKey(f.read())
	f.close()
	print 'file with cipher:'
	f = sys.stdin.readline()[: -1]
	f = open(f, 'r')
	f = key.decrypt(f.read())
	print f

def encrypt():
	print 'file with someones public key:'
	f = sys.stdin.readline()[: -1]
	f = open(f, 'r')
	key = RSA.importKey(f.read())
	f.close()
	print 'file with plain text:'
	f = sys.stdin.readline()[: -1]
	f = open(f, 'r')
	f = key.encrypt(f.read(), 'rand')[0]
	print f
	print 'file to write:'
	w = open(sys.stdin.readline()[: -1], 'w')
	w.write(f)
	print f
