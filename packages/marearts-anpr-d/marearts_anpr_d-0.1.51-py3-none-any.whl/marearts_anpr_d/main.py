# marearts_anpr_d/main.py
from crypto_mng import encryption, decryption

def anpr_d():
    print("detect license plate")
    print(encryption(1))
    print(decryption(1))

if __name__ == "__main__":
    anpr_d()