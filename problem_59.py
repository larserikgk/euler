f = open('problem_59_cipher.txt', 'r')
cipher_text = f.read()
cipher_text_list = list(map(int, cipher_text.split(',')))
cipher_text_characters = [(chr(char)) for char in cipher_text_list]

print(cipher_text_list)
