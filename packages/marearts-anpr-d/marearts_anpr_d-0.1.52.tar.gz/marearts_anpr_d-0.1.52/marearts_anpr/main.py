# marearts_anpr/main.py
from marearts_anpr import encryption, decryption

def anpr_d():
    print("detect license plate")
    print(encryption(1))
    print(decryption(1))

if __name__ == "__main__":
    anpr_d()