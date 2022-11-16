from Encoding import Encoding

def main():
    message = "Hello world"
    my_encoding = Encoding("* # \ /")
    encoded_code = my_encoding.encode_message(message)
    my_encoding.write_message(encoded_code)
    encoded_message = my_encoding.read_message(f"encoded_message")
    decoded_message = my_encoding.decode_message(encoded_message)
    print(decoded_message)

if __name__ == '__main__':
    main()