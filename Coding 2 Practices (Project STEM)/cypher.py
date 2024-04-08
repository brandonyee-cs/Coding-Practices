def rotate_string(string: str, rotation: int) -> str:
    lowercase_letters = range(ord('a'), ord('z') + 1); rotated_chars = []
    for c in string:
        if ord('a') <= ord(c) <= ord('z'): new_char = chr((ord(c) - ord('a') + rotation) % 26 + ord('a')); rotated_chars.append(new_char)
        else: rotated_chars.append(c)
    return ''.join(rotated_chars)

def decode_rotated_string(s: str, rotation: int) -> str:
    return rotate_string(s, -rotation)

def find_rotation(encoded_message, decoded_word):
    for rotation in range(0, 25):
        decoded_message = decode_rotated_string(encoded_message, rotation)
        if (decoded_word in decoded_message) == True: return rotation

def main():
    quit = False
    while quit == False:
        choice = input("q for quit, d for decode via rotation, w for decoding via a correct word; e for encode: ")
        if choice == 'q': quit = True
        elif choice == 'e': string = input("Enter string: "); rotation = int(input("Enter rotation: ")); print(rotate_string(string, rotation))
        elif choice == 'd': string = input("Enter string: "); rotation = int(input("Enter rotation: ")); print(decode_rotated_string(string, rotation))
        elif choice == 'w': string = input("Enter encoded string: "); phrase = input("Enter decoded phrase: "); print(f"Rotation: {find_rotation(string, phrase)}\nDecoded Phrase: {decode_rotated_string(string, find_rotation(string, phrase))}")
        else: print("Bad command, try again")
    print('Thanks for playing')

main()