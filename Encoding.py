from typing import List, Union, Any

class Encoding:
    def __init__(self, symbols):
        self.symbols = symbols.split(' ')
        self.foot  = len(self.symbols)

    def encode_message(self, message: str) -> str:
        encoded_to_foot = Encoding.encode_text_to_foot(message, self.foot)
        encoded_text = self.encode_to_symbols(encoded_to_foot)
        return encoded_text

    def decode_message(self, message:str) -> str:
        decoded_to_foot = self.decode_to_symbols(message)
        decoded_text = Encoding.decode_foot_to_text(decoded_to_foot, self.foot)
        return decoded_text

    def encode_to_symbols(self, message:str) -> str:
        encoded_text = ''
        symbols_list = message.split(' ')
        for symbol in symbols_list:
            encoded_symbol = ''
            for char in symbol:
                encoded_symbol += self.symbols[int(char)]
            encoded_text += ' ' + encoded_symbol
        return encoded_text[1:]

    def decode_to_symbols(self, message:str) -> str:
        decoded_text = ''
        symbols_list = message.split(' ')
        for symbol in symbols_list:
            decoded_symbol = ''
            for char in symbol:
                decoded_symbol += str(self.symbols.index(char))
            decoded_text += ' ' + decoded_symbol
        return decoded_text[1:]

    @staticmethod
    def encode_text_to_foot(message: str, foot) -> str:
        encoded_text = ''
        for char in message:
            asci_value = ord(char)
            translated_values = Encoding.dec_to_foot(asci_value, foot)
            translated_values = ''.join(str(x) for x in translated_values)
            encoded_text += ' ' + translated_values
        return encoded_text[1:]

    @staticmethod
    def decode_foot_to_text(message: str, foot) -> str:
        decoded_text = ''
        message_list  = message.split(' ')
        for foot_value in message_list:
            asci_value = Encoding.foot_to_dec(foot_value, foot)
            decoded_text += chr(asci_value)
        return decoded_text

    @staticmethod
    def dec_to_foot(dec_value: int, foot: int) -> list[Union[int, Any]]:
        dec_def_val = dec_value
        foot_value = []
        while dec_value > foot:
            foot_value.append(dec_value % foot)
            dec_value = dec_value // foot
        foot_value.append(dec_value % foot)
        if len(foot_value) < 4 and dec_def_val > 64:
            foot_value.append('1')
        return(foot_value[::-1])

    @staticmethod
    def foot_to_dec(foot_value: str, foot: int) -> int:
        dec_value = 0
        for i in range(len(foot_value)):
            dec_value += int(foot_value[i]) * foot ** (len(foot_value) - i - 1)
        return dec_value

    @staticmethod
    def write_message(message):
        with open(f"encoded_message.txt", "w") as file:
            file.write(message)

    @staticmethod
    def read_message(filename):
        with open(f"{filename}.txt", "r") as file:
            message = file.readline()
        return message
