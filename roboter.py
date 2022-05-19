import collections
import csv
import os

from termcolor import colored

output_file: str = 'robot.txt'
fieldnames = ['NAME', 'COUNT']


def write_to_file(fname: str, d: dict):
    with open(fname, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in d.items():
            writer.writerow({'NAME': k, 'COUNT': v})


def read_file(fname: str) -> dict:
    exist = os.path.exists(output_file)
    if exist:
        with open(fname, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            d = {row['NAME']: int(row['COUNT']) for row in reader}
        return d
    else:
        return {}


if __name__ == '__main__':
    x = read_file(output_file)
    current_dic = collections.defaultdict(int)
    for k, v in read_file(output_file).items():
        current_dic[k] = v

    name_question = colored('I am roboko, What is your name?', 'green')
    print(name_question)
    _ = input()

    sorted_dict = sorted(current_dic, key=current_dic.get, reverse=True)

    for k in sorted_dict:
        print(f'Do you like [{k}]? [Yes/No]')
        re = input()
        if re == 'Yes':
            current_dic[k] += 1

    restaurant_question = colored('What is your favorite restaurant name?', 'green')
    print(restaurant_question)
    name = input().capitalize()

    current_dic[name] = current_dic[name] + 1
    write_to_file(output_file, current_dic)
