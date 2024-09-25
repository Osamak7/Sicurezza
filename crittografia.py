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

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAnnYn30q14bl/w7vVYwkonffu8uQI/YO3BwzDfHur13G5bhB5\nfKbS7ZkPwd0FcCItRuQYQd+j3kceZ3CKz+6Smk5Q3qDsqhG41YV9Mv1JUfN7anXy\njNkoRJ6VhWa9klG7pIJ0VA6QNMyFI+cO0vnq+R1j6rtG3v1HyeP6FUkAU3D/0CCf\nXXrwyGiPGiOvHvKf8M7uTbno3vL2CLY2ekg0NIFJ+eu2Bjk1p+MkwFMMsD9vDfvZ\npTDqHWIs9UvBy4X9+ePfMZEbzYdXaFVTAgGZBQZ9IxJxHKaB5iLHnvrTjWvztPj3\n0qZS/1jpisYbYjC9R/YskG484nCtCuOHTOUR0QIDAQABAoIBACDV6pK4VEKbMfix\nCDluqSo8uVi+/Ibt34QYNrzpkpUBBZPjWY1FM2GVLUD2h/0xs9CkDMu/qCDz+z6j\ngTwvm1TaxCKx1YCzTen+8I/bkPEoo0sO+E0L5a58bw7W2JMEmT2wY6MUZnjuZWto\nYnfA3lozJyR5nKix8smI0mZNO4JOjVZNnORUf8LyYWF4/MOlEYGCcNfikb340EAf\nMI/OIKilckCyUIXEgSiWumW9gCnpoZDlHqz/Or78p+Va8m8huACuRYmKweJt+hcq\nv1w+bzXr7Pz4YtcQpKycI9z7vvztwe99craXByncu5Vbewv4jQ2qlqOfJT3rvuNv\njR5Tpv0CgYEAx8rn65VYAVkaIgvzQtreL4jg2xUHjFultg6J4wMR859sYYkmLlbw\nxp4HMNBAofSYt30v7G49Dn0y99EkBG9tETT1IPx76MKLO/V79EqHEO1C4NuS0rQX\n8EjTLqSfaq1WrOpdWslO7q0eSlxjV+DhLhQ9NI/CUZDQDhanJu3/v7UCgYEAywqU\nr7E01lOPUtAia/FnJjizNhDha5aPxnhhjrpx36e/LkCMumWUggnY4WTQE+N2qDYH\n22X6WiiI69ba9/hvOMcrsXtW28TlIKm0HYkAOlET5Lmr3/afUp/HeJIoGRmG0DlY\nUQsGI8N97N5o3R/ZicJr1G6FFFnvqpYa4Js0Qy0CgYBlML6gEibdn+xdfCH8JXBN\nMQ15yL/m9fALMnfh84cfFgrFp7of1EbkwdswfPmPTZwfqxcfr4HbGcw7ucB9QpZC\nFcllqJt1ezsb5iyewTSBfTnXOz602yQYvjm/sP9Q/3Qb5iPcPINu3V2vGfXy52IF\nfZi2S22G9Ep8KDsGu5pB1QKBgDg4ttErbWkHfEE/FrjzAE/qFV2cMP8ckrUvMjxW\nTh/TEDIbd5xJcmTLmz1WL/PB4WJUi7pps3fxj3BWbw2Iwitjoyqi73stOxDfTNt8\nyw5a0vpbm0cJwDYdvhsZxXalxdm0d0sBlXKjuCO1ti28mvz1U+xfqgPnn2CJ7elR\nsJgFAoGBAL2eWP+gZJKLe7juI6g9p5ixy2s4n5c1pPhEsc21i5pg5KfCF6IMw2kx\n8rzF5V+L2bOi5UD81HfRcZ/1ackP6uTSsRG3mv0MNXvLGAnzre6H+Ei6fXvCDA3T\nBtwG7ZC4fWjMvjirY38LXgLZKUTAqZEdPPKCTU7y/AC1VPq+F6dj\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnnYn30q14bl/w7vVYwko\nnffu8uQI/YO3BwzDfHur13G5bhB5fKbS7ZkPwd0FcCItRuQYQd+j3kceZ3CKz+6S\nmk5Q3qDsqhG41YV9Mv1JUfN7anXyjNkoRJ6VhWa9klG7pIJ0VA6QNMyFI+cO0vnq\n+R1j6rtG3v1HyeP6FUkAU3D/0CCfXXrwyGiPGiOvHvKf8M7uTbno3vL2CLY2ekg0\nNIFJ+eu2Bjk1p+MkwFMMsD9vDfvZpTDqHWIs9UvBy4X9+ePfMZEbzYdXaFVTAgGZ\nBQZ9IxJxHKaB5iLHnvrTjWvztPj30qZS/1jpisYbYjC9R/YskG484nCtCuOHTOUR\n0QIDAQAB\n-----END PUBLIC KEY-----"

sPub2="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkYad8prkiIowSLoIDWKP\n8o+aYbA2lRfuyg10WiIIaVLLwlmjld04D992omciUXpEOrCrLbs1OMsTB53c+Wwm\n3ptbjKGCmVXLIBDni7XmBgOok652EfEMH/aJOb3DxKe9wQt80zFJkziYjr89jNzE\n97Wr0/Nq0KvoQUWuAk71MUKK5blfzZKejc9QGRH9vVPzGBiEY42VQ0vzqQXULm9W\nrBS3HC5cABrg7ZIniptKxtTd1beTbq6RC0yTD7hNyhQ3nRCFVEozdJ6Q4OnH/MCz\nOCSj8YT81su1+7T4l1udfBNXRCxfPeIsxfbuBliLXfDfX/Vl2bkXtTMrrtq6pY3B\nTwIDAQAB\n-----END PUBLIC KEY-----"
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
PK_LOREN= RSA.import_key(sPub2)

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
encrypted_message = "W5MVRu8aL3oBZWghm/eXYvDgPPdBI3mI/U648+Oy4wsCuvR6yYXsHhpdTXmebIW2988cFb0U0OBtRpkOYw92dsyCfY2DIgEtu7paNJEvMZlgBotzqxE53AUNFWj6QhFkFYRg0cN/bvj+0XBxS2FY7rXO1/kT/EYtNY/fWIVLFo7xydeucsQFv5P1YOjnlIZrXYOkdmlSV2dGlT4r0CohqG0n/u4c9ThBqML/Sg/5sAo0WYBBRIdc8Dfjm1ago3Rv+y+xp25FteyMjp3+iCCRIxli+irnw5VetMM+VwjqPrNMEm8PVc+NJZzUv/1Y9sczNnYP0as81LMwNGaK4u335Q=="
# message="aaa"
# encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
messagge="poi ti spiego"
decri_message= encrypt_message(messagge , PK_LOREN)
print("messaggio criptato \n"+decri_message)