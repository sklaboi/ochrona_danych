from Crypto.PublicKey import RSA
import sys


def main():
    rsa_keys = RSA.generate(1024)
    pr_key = rsa_keys.exportKey('PEM')
    pub_key = rsa_keys.publickey()
    print 'rsa keys:'
    print rsa_keys
    print 'private key'
    print pr_key
    print 'public key'
    print pub_key
    print 'enter message:'
    mess = sys.stdin.readline()
    mess = pub_key.encrypt(mess, 'sialalala')
    print 'encrypted:'
    print mess
    mess = rsa_keys.decrypt(mess)
    print 'decrypted:'
    print mess

main()