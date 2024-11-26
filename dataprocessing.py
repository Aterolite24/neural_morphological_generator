import numpy as np
import pandas as pd
import os
from google.colab import drive
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras import Model, Input
from tensorflow.keras.layers import LSTM, Embedding, Dense, Attention, MultiHeadAttention, LayerNormalization, Dropout, Add, GRU, Bidirectional

drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/nmg/hin/hin'

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Explore data
print(f"Number of lines in the dataset: {len(data)}\n")

print("Sample lines:")
for i, line in enumerate(data[:5]):
    print(f"{i + 1}: {line.strip()}")
print()

parsed_data = [line.strip().split('\t') for line in data]
print(f"First parsed entry: {parsed_data[0]}")
print(f"Second parsed entry: {parsed_data[1]}")

cleaned_data = [line.strip() for line in data if line.strip()]
print(f"Number of non-empty lines: {len(cleaned_data)}")

structured_data = [line.split('\t') for line in cleaned_data if len(line.split('\t')) == 3]

columns = ['Base Word', 'Transformed Word', 'Attributes']
df = pd.DataFrame(structured_data, columns=columns)

print(f"Number of valid entries: {len(df)}")
print("Sample entries:")
print(df.head())

df[['POS', 'Person', 'Number', 'Tense', 'Aspect', 'Gender']] = df['Attributes'].str.split(';', expand=True)

print("Data with split attributes:")
print(df.head())

print(df.isnull().sum())

df['Tense'] = df['Tense'].fillna('UNK')
df['Aspect'] = df['Aspect'].fillna('UNK')
df['Gender'] = df['Gender'].fillna('UNK')

print(df.isnull().sum())

df.to_csv('/content/drive/MyDrive/nmg/hin/processed_dataset_hin.csv', index=False)