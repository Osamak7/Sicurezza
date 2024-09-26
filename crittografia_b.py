# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAylN7vEix6t3w/zHnODL71AkYb3eZ32nRBOMzQLR7fagYh/sD\nBkOPS5wlcADL8TWMRyMu1CmcHD3vl9wA58pq/ZEFiDGb2npEpAdYoe9hpkVFs3zG\nWDIZrIg1S/mQqlXUmHTr1XCiVYWmOIFgoWTpJRVTgWXrbgc74bn13mNJf8OnjyO6\nzc+I0LRqlYWagc+NVXAHQ1hxzVn7jgJA0n+5ecpzZBGLE+Py7+JPQbjXZmB2u0eH\nYgrKCX0/k+TBvRSV8xWJTm7/kZDWuQa7jtaZL7T4MoFi0eb1hb5jzD39zeehF+xi\n04LwdFus9mKTFcgDDYN+TmuGcp3VX5KW8TPIOQIDAQABAoIBAC291wUXyEWJnMEN\nJrGhcSacUc5tkzebxDofJYi05RBhDv67JJFnd7+H0zzxqSnkycyRazZjG9yUshS6\nk+fTbwHZpg8G7C3mI5uT35lotcJx+dKc3Hi3Bu/nMWl2SBsCYZiAIos0NjcwioZO\n1apXVpBgNGtWP/Y1o3eiY7A98TF1gtcjua61fvTIQ7KXtl+W6PGYZS99iqNwn3FE\nqaENdo+uZQsvhZx2JvbwC2O4eunY5Jm+gDRYDGJy4oPWGOucuUyRRV2LOXslY4eg\nOtmMuhmwEaVdqM8DMWPgsN4TTgKc83fkfoGoz74cjltbuLUV6a6DOsRWYK4eCOoC\nQAsddbsCgYEA1m/KCEsJZzFnoqDWdXAr98DI6hDXPczi8StNjQ3rLLMUHb+QLlJV\nNG1Qr33sgQfJgKUS/i83t+vUgMrJ+QDjzIRSTk4mDyoa482QD8LqjVBOiMYaBfAG\nlaf5yehe85nadr2bzWpx4NYZEKVaKIx0Id7ypIDiUVodNGeaShOfmv8CgYEA8YrG\ngkEhsYR/dTjvF2WSH9BBkygJ9xajCFBoF9sXipaKtlZ1lQxXTNy5uILTjqoQQQTq\nsvrAvlN5v+eiCnCa9j8x6itFZ8EgmdwiKiVgtH/FnTqIuUPXx8Q6yYwG2NL5t7UE\nN2pOH477M3dc4yhg5xMy7mN0eTSwF0vnXevZtMcCgYAv9tNG5ZnV1iwrKTSvEgcT\npLCMAnZSoXiFnzz6dwmKdwfh245hfhMG5gitKEp1VguRVdsYtfENl5dxs2pX4wYR\nIevTDhHfRHi9SaaWj++s6jCW0VDS0Sx33xm1Ot+6N0ixVJn76XpNYzY6DfJLrZbw\nWJEHkLiOn8x2g1H0jc0eewKBgAD6B611J/a4y28k6MqWbY3VYL6AlfG61LPu50zZ\nZPH5g9wS42zT3PKBnfqiBMr54xDwPSa2HttmKQLeo+gY5neCb+g7fo9Z15Dns/ep\nqQdx0NG+79iX7qJvJ7Gy8EAmMj5M7BRxSJmWEWv22phMjH/Csx0Fp+3piaC+fNQD\nZSD3AoGAPH0OW6VP5Gmob4RDInLkjCtuwXqucEzWkXeb5KXaAiIWuR27+oNCskwR\nca3XLsU0eCdGjdZ9qVIQKruN6QmuGLYcX7Bhjrv6i5RyOGH1GdyNNwmX7DTP67Vz\nWfiEUiUEPc0tOCpdyOjMtg6oTK7xgcLTTt97chj8oad1CkjCQKA=\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAylN7vEix6t3w/zHnODL7\n1AkYb3eZ32nRBOMzQLR7fagYh/sDBkOPS5wlcADL8TWMRyMu1CmcHD3vl9wA58pq\n/ZEFiDGb2npEpAdYoe9hpkVFs3zGWDIZrIg1S/mQqlXUmHTr1XCiVYWmOIFgoWTp\nJRVTgWXrbgc74bn13mNJf8OnjyO6zc+I0LRqlYWagc+NVXAHQ1hxzVn7jgJA0n+5\necpzZBGLE+Py7+JPQbjXZmB2u0eHYgrKCX0/k+TBvRSV8xWJTm7/kZDWuQa7jtaZ\nL7T4MoFi0eb1hb5jzD39zeehF+xi04LwdFus9mKTFcgDDYN+TmuGcp3VX5KW8TPI\nOQIDAQAB\n-----END PUBLIC KEY-----"

sPub_a="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmcATnIt4I1IzjkPp350h\nct/+civ4B8rLPWg+rSpbnFnTJS0pmBJrN6C01tedThDCN+Jg2B9nROOalnz7JsN7\n3yk1SHw+Z60LKS1Uuy4wU3IVMkiNBwgfkznHPjWDYrXwGj2cdmzHBvCKxYxQD1mM\ntHuuG+L91kQa3x1hq5723WCV7KyXX7hZ0laVQwo4gP2lD5RQitNojAI11HjkqISa\nFr74pz+yLnlImToCbWdG3EG1pz0adRmtQIDaIcwP6TFrgn40ztMliMedldfG8gwM\nbcZwROOmt8AryGFfG4eee5JOYNqzbHok6iLFKwWR5EHKHjdtFn6lw37JPvQ+eOMj\n2QIDAQAB\n-----END PUBLIC KEY-----"
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
PK_a = RSA.import_key(sPub_a)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "ciao come va"
encrypted_message = encrypt_message(message, PK_a)
#decrypted_message = decrypt_message(encrypted_message, key_pair)
print(f"Encrypted Message: {encrypted_message} \n")

message_cryptated="lOX0zV32vqX+Y0dRqEkwyi/eK3hWgVZJ1o/wESb8gTn7QDFCM3sSHbsdAuDRfJ48EckeRN5ko3G/5KT5J8HFlpnj/8mvjs/3M0mTcw/5nuPEtFYAcfbYFXyOb0iv4m4/Oc4JYgzYNeKcOflLaZuCiIKYZ3Zt20NhEemrPzH9YmsduMEypBrGFLbmz9y1sdyouCD8w3uxTqCDvuJYymnp4tYtcG8rHLl7KTr3tXFTYkF7sM4CPkaJ5DDt9/ozQ3ACPn8tyKIRa+hjwAJwZnC+XnYl0sGS7R/CUIbhJD4n+RqdfMbxaW1kCdEW9xGgtzlajoMFtoaETdvPomPuuZ+5jQ=="
decripted_message= decrypt_message(message_cryptated , key_pair)
print(f"Decripted message:  {decripted_message}")