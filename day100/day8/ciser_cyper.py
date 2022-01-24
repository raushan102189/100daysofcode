word = "abcdefghijklmnopqrstuvwxyz"
for each_letter in word:
    alphabate = []
    alphabate += word
    alphabate += word

encode_or_decode = input("""want to "encode" or "decode" """)
text = input("write your message: ")
shift_value = int(input("shiftvalue "))

def encode(text,shift_value):
    coded_text = ""
    for letter in text:
        position = alphabate.index(letter)
        new_position = position + shift_value
        new_letter = alphabate[new_position]#I have no idea how it work
        coded_text += new_letter
    print(f"this is the encoded text :{coded_text} ")


def decode(text,shift_value):
    coded_text = ""
    for letter in text:
        position = alphabate.index(letter)
        new_position = position - shift_value
        new_letter = alphabate[new_position]#I have no idea how it work
        coded_text += new_letter
    print(f"this is the message :{coded_text} ")

if encode_or_decode == "encode":
    encode(text,shift_value)
elif encode_or_decode == "decode":
    decode(text,shift_value)

else:
    print("you have to choose encode or decode first")    



    

   
