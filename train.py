import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--input-dir',
                    default='stdin',
                    help='Путь к директории, в которой лежит коллекция документов. (default: stdin)')
parser.add_argument('--model',
                    default='./',
                    help='Путь к файлу, в который сохраняется модель. (default: ./)')

args = parser.parse_args()
print(args.model)
# if args.input-dir == ''
# data = sys.stdin.readlines()