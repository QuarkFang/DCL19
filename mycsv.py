import csv


def raw_reader(path='data/Raw.csv', encoding='utf-8'):
    csv_reader = csv.reader(open(path, encoding=encoding))
    data = []
    for row in csv_reader:
        data.append(row[1])
    return data[1:]


def EEG_reader(path='data/EEG.csv', encoding='utf-8'):
    csv_reader = csv.reader(open(path, encoding=encoding))
    data = []
    for row in csv_reader:
        data.append(row[1:])
    return data[1:]


def ECG_reader(path='data/ECG.csv', encoding='utf-8'):
    csv_reader = csv.reader(open(path, encoding=encoding))
    data = []
    for row in csv_reader:
        data.append(row[0])
    return data


if __name__ == '__main__':
    csv_reader = ECG_reader()
    for row in csv_reader:
        print(row)
    # print(csv_reader[1][3])
