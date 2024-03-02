x = input("want to start caeser cipher ('yes'/'no'):")
while x != 'yes':
  print("Thank you for using the program")
  break
while x == "yes":
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  select = input(
      "Type 1 for encryption, 2 for decryption and else for exit: \n")
  if select not in ['1', '2']:
    print("Bye,hava a nice day.")
    break
  text = input("Enter your message: \n")
  shift = int(input("Enter the shift number: \n"))
  if select == "1":

    def encrypt(text, shift):
      cipher_text = ""
      for letter in text:
        if letter in alphabet:
          pos = alphabet.index(letter)
          new_pos = (pos + shift) % 26
          cipher_text += alphabet[new_pos]
        else:
          cipher_text += letter
      print(f"The encoded text is {cipher_text}")

    encrypt(text, shift)
  elif select == "2":

    def decrypt(text, shift):
      cipher_text = ""
      for letter in text:
        if letter in alphabet:
          pos = alphabet.index(letter)
          new_pos = (pos - shift) % 26
          cipher_text += alphabet[new_pos]
        else:
          cipher_text += letter
      print(f"The decoded text is {cipher_text}")
    decrypt(text, shift)