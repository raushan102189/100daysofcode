

word = "abcdefghijklmnopqrstuvwxyz"
for each_letter in word:
    alphabate = []
    alphabate += word
    alphabate += word

encode_or_decode = input("""want to "encode" or "decode" """)
text = input("write your message: ")
shift_value = int(input("shiftvalue "))
while shift_value > 26:
    shift_value %= 26
   

    
print(shift_value)
def encodeDecode(text,shift_value,direction):
    coded_text = ""
    for letter in text:
        if letter in alphabate:
            position = alphabate.index(letter)
            if direction == "encode":
                new_position = position + shift_value
            elif direction == "decode":
                new_position = position - shift_value
            new_letter = alphabate[new_position]#I have no idea how it work
            coded_text += new_letter
        else:
            coded_text += letter
    print(f"this is your {direction}d text: {coded_text}")

encodeDecode(text,shift_value,encode_or_decode)


