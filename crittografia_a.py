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
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAmcATnIt4I1IzjkPp350hct/+civ4B8rLPWg+rSpbnFnTJS0p\nmBJrN6C01tedThDCN+Jg2B9nROOalnz7JsN73yk1SHw+Z60LKS1Uuy4wU3IVMkiN\nBwgfkznHPjWDYrXwGj2cdmzHBvCKxYxQD1mMtHuuG+L91kQa3x1hq5723WCV7KyX\nX7hZ0laVQwo4gP2lD5RQitNojAI11HjkqISaFr74pz+yLnlImToCbWdG3EG1pz0a\ndRmtQIDaIcwP6TFrgn40ztMliMedldfG8gwMbcZwROOmt8AryGFfG4eee5JOYNqz\nbHok6iLFKwWR5EHKHjdtFn6lw37JPvQ+eOMj2QIDAQABAoIBACo+m2Tc8WKLGH1T\nbbQyQVmF8CzApgLGFrfFp8r+o3M/PwOs+Au/q9P6BRYu4hrsAeFHAyL+5eoIu5Xz\nuzI4bhWwBeLnuGHWKwXiXbCcjUywQOCzDITNF5flPTh7jaEWqmUbXp0vYDQo7Yg/\n+FNvYHjKrtkcsnAoAFYjhY2ZPO0wSpgW45cGYkzZWFqp66AtAos72ziLDMjtM4Ey\nyxsR9hfmOzuBaTmgSbOGIz/W1MD6rC517hvygSWHyTPMtA6UG42dLrXuSV601sd4\nhC+QcFLYDMDVC8u6ky6kT30pOGVrG0+9B4ntvVdEUMPc5MTR82qU0wvBAPnqVHFE\n5J1TKa0CgYEAw1vhd73Qq++b+RDjQcWnH1aM/NlxhqpDy+Bb+BOpqMl5yh+QRXPp\nFJeRopoYRamiCBEJVpwvoixjAC6z8lzCpqkJI40rHXc3HIQpE8EWcDsIzLTvxv6w\nrGZc4H7QxWy8rPOk54jjKgOA+cSufnXeWOdeUp9erSbzJeKrgh2yu88CgYEAyXnI\nsnMPtXW4avpDMaw+ukOivMNG/nGIGZharVj5PGzBbwyS4aV1W30pESoviOJzIogG\nzcIS0L86zOPtI/Erer3lFyBYwUUC/58mBormSUEF82QGoYrSlJALURVnZabnP7es\nHjfu9p8gfkWMDXM2PnehTuNmBUecTykkVBZ/R9cCgYEAgGVl5W4StL4xc9vekP7X\n3SfkV9aN36UOE/PsXjqGGlH4wphGGO+adBc993FxnG9l+AlCavMR93NWyeroB9Vh\ndWnJgN0qRh5xUUOnP717At455VjR8qa39Ub9qeqPSgIyazVi322/Z4CQBxh2WtUb\nArFl88Wc0w6zZeX5NPZR308CgYBuAU+il45hLph12JUtnvVU8C7/z8OIk+aSywvf\nkC/tXRg0kPH1wEiWnnz4wUbY/4OLvCey2p85WOA7FMvbDwgFaX+XI/Mx+4NKnNO/\nSMG6B4W/QcMZGtolgYycRgqBhyLGOHwCt9mC0JmGOGTixyA79Uee8iw2/8WJt1X9\nj5cJWwKBgFNCuDQYolmBwEi6VG+RgiNiWxLDkS9pQ+VGeLC1V0F7isToMobDN1J7\npOBIaCGpZn4j3ZHaA+5bK7l144V2dnzYM0saJTSXth3obewDyFAcsobJ+ryDm/Dz\nQosfYf7MjI4uPRZw2vmQfSt52g2ctJc0Iyp0FV/kCJ/YCbORIqvW\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmcATnIt4I1IzjkPp350h\nct/+civ4B8rLPWg+rSpbnFnTJS0pmBJrN6C01tedThDCN+Jg2B9nROOalnz7JsN7\n3yk1SHw+Z60LKS1Uuy4wU3IVMkiNBwgfkznHPjWDYrXwGj2cdmzHBvCKxYxQD1mM\ntHuuG+L91kQa3x1hq5723WCV7KyXX7hZ0laVQwo4gP2lD5RQitNojAI11HjkqISa\nFr74pz+yLnlImToCbWdG3EG1pz0adRmtQIDaIcwP6TFrgn40ztMliMedldfG8gwM\nbcZwROOmt8AryGFfG4eee5JOYNqzbHok6iLFKwWR5EHKHjdtFn6lw37JPvQ+eOMj\n2QIDAQAB\n-----END PUBLIC KEY-----"

sPub_b="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAylN7vEix6t3w/zHnODL7\n1AkYb3eZ32nRBOMzQLR7fagYh/sDBkOPS5wlcADL8TWMRyMu1CmcHD3vl9wA58pq\n/ZEFiDGb2npEpAdYoe9hpkVFs3zGWDIZrIg1S/mQqlXUmHTr1XCiVYWmOIFgoWTp\nJRVTgWXrbgc74bn13mNJf8OnjyO6zc+I0LRqlYWagc+NVXAHQ1hxzVn7jgJA0n+5\necpzZBGLE+Py7+JPQbjXZmB2u0eHYgrKCX0/k+TBvRSV8xWJTm7/kZDWuQa7jtaZ\nL7T4MoFi0eb1hb5jzD39zeehF+xi04LwdFus9mKTFcgDDYN+TmuGcp3VX5KW8TPI\nOQIDAQAB\n-----END PUBLIC KEY-----"
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)

PK_b= RSA.import_key(sPub_b)


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
message_from_b ="NVCvHIWmK3lsQ0Q2a6lAYwyEY/p7iVWTotqQVQyfXjx7Zcmg7almfzbmgCPbxUZmyUcMjS7y/G8hW35pOpaKs1BRNhf2ULn5eoeZn+Hvf9rKArGq8hZtkGJB1gOMPM94Dd0t2rQE9V//ROMyfqBFFsBk9t5XvZp5X5MBtdHAbaxtKuilUwsffXjW8YWzQJ1US0nuib8/6i3uIS6oVDkBDfrWtm0QaqAqy1JqKmPGeqQN4d5uKkZkkPyfi2JUw/BqeKnyluHxVBYiO0JIWgUZKPZqGJX16wVn7XnAbmPtt040vO3yoTINzTrfWsxTBWq4xG0AqIPmRc8iOnQwJgCCJg=="
decrypted_message = decrypt_message(message_from_b, key_pair)
print(f"Decrypted Message: {decrypted_message} \n")

#Risposta
message_risposta = "tutto bene"
encrypted_message = encrypt_message(message_risposta, PK_b)
# print("Original Message:", message)
print(f"Encrypted Message: {encrypted_message} \n")