import os
import pandas as pd
from dotenv import load_dotenv
from src.load_data import load_data
from src.preprocessing import preprocessing, mapper, tokenize_text

load_dotenv()  # Load environment variables from .env file

data_path = os.getenv("data")
data = load_data(data_path)
data = preprocessing(data)
data = mapper(data)
data = tokenize_text(data)

