import logging

import torch

from tokenizer import Tokenizer, read_txt

text: str = read_txt("./training/poe.txt")
tokenizer: Tokenizer = Tokenizer(text)
data = torch.tensor(tokenizer.encode(text), dtype=torch.long, device="cpu")
logging.info(f"Tokenizer loaded. Shape: {data.shape}, Type: {data.dtype}, Device: {data.device}")
logging.debug(f"First 1000: {data[:1000]}")
