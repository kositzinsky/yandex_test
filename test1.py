class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        text = text.lower()
        cipher_text = ''
        if not is_encrypt:
            shift = 0 - shift
        for leter in text:
            if leter not in CipherMaster.alphabet:
                cipher_text += leter
            else:
                index = (CipherMaster.alphabet.find(leter) + shift) % 33
                cipher_text += CipherMaster.alphabet[index]
        return cipher_text
        

cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 