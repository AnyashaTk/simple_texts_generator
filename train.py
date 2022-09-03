import argparse
import os
import sys
import pickle

parser = argparse.ArgumentParser()

parser.add_argument('--input-dir',
                    default='stdin',
                    help='Путь к директории, в которой лежит коллекция документов. (default: stdin)')
parser.add_argument('--model',
                    default='./',
                    help='Путь к файлу, в который сохраняется модель. (default: ./)')

args = parser.parse_args()
print(args.model)

class TextModel():
    def __init__(self):
        w2v = 'w2v obj'

    def fit(self, train_data):
        pass

    def generate(self, length):
        text = ''
        return text

model = TextModel()

# Train process

# Saving model
with open(os.path.join(args.model, 'model.pkl'), 'wb') as save_path:
    pickle.dump(model, save_path)