import argparse

parser = argparse.ArgumentParser(description='Fixes cp1256 encoded subtitles')
parser.add_argument("path", help="Path of subtitle", type=str)

parser.add_argument('-e', '--encoding', help='Default encoding. Defaults to\'cp1256\'', default='cp1256')

args = parser.parse_args()

path = args.path
enc = args.encoding

with open(path, 'r', encoding=enc) as src:
    tmp = src.read()
    with open(path, 'w') as dst:
        dst.write(tmp)





