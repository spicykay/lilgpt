import logging
import os

log_level = os.environ.get('LOG_LEVEL', 'INFO')
log_level = getattr(logging, log_level.upper())  # Convert the log level string to a constant

# Configure the logging system with the desired log level
logging.basicConfig(level=log_level)


# read in the text
def read_txt(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        read_text = f.read()
    logging.debug(f"Text Read: {read_text}")
    logging.info(f"Text Length: {len(read_text)}")
    return read_text


class Tokenizer:
    def __init__(self, training_text: str) -> None:
        self.unique_chars: list[str] = Tokenizer.get_unique_chars(text_str=training_text)
        self.char_to_pos_map: dict[str, int] = dict()
        self.pos_to_char_map: dict[int, str] = dict()
        for i, char in enumerate(self.unique_chars):
            self.char_to_pos_map[char] = i
            self.pos_to_char_map[i] = char

    def encode(self, thing_to_encode: str) -> list[int]:
        return [self.char_to_pos_map[char] for char in thing_to_encode]

    def decode(self, encoding: list[int]) -> str:
        return ''.join([self.pos_to_char_map[i] for i in encoding])

    @classmethod
    def get_unique_chars(cls, text_str: str) -> list[str]:
        # Get a list of each character in the text, sorted
        char_list = list(text_str)
        unique_chars_set: set = set(char_list)
        unique_chars_list: list = list(unique_chars_set)
        unique_chars_list.sort()
        logging.debug(f"Unique Char Size: {len(unique_chars_list)}")
        logging.debug(f"Unique Chars: {unique_chars_list}")
        return unique_chars_list
