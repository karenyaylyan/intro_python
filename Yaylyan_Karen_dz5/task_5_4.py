import re

class RLE:
    @staticmethod
    def encode(line):
        if not line:
            return ''
        result = ''
        count = 1
        for i in range(1, len(line)):
            if line[i] == line[i-1]:
                count += 1
            else:
                result += f'{line[i-1]}{count}'
                count = 1
        result += f'{line[-1]}{count}'
        return result


    @staticmethod
    def decode(line):
        result = ''
        counts = re.findall(r'\d+', line)
        i = 0
        for el in line:
            if not el.isdigit():
                result += el * int(counts[i])
                i += 1
        return result


if __name__ == '__main__':
    with open('input.txt', 'r') as inf, open('output.txt', 'w') as ouf:
        line = inf.read()
        decoding_line = RLE.decode(line)
        print(decoding_line)
        encoding_line = RLE.encode(decoding_line)
        ouf.write(encoding_line)
