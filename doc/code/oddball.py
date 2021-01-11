from logger import *
import pandas as pd
import os

file_path = '../data/'
sys.stdout = Logger(sys.stdout)


def calculate_accuracy():
    odd_data = pd.read_csv(file_path + 'oddball.csv')
    code_num = [int(i) for i in odd_data['事件码']]
    react_time = [int(i) for i in odd_data['反应时间']]
    num_11 = 0
    num_22 = 0
    num_11_correct = 0
    num_11_incorrect = 0
    num_22_correct = 0
    num_22_incorrect = 0
    num_11_react_time = 0
    num_22_react_time = 0
    for i in range(len(code_num)):
        if code_num[i] == 11:
            num_11 += 1
            num_11_correct += 1 if code_num[i + 1] == 2 else num_11_incorrect + 1
            print(f'react time is {react_time[i + 1] - react_time[i]}')
            num_11_react_time += react_time[i + 1] - react_time[i]
        elif code_num[i] == 22:
            num_22 += 1
            num_22_correct += 1 if code_num[i + 1] == 1 else num_22_incorrect + 1
            print(f'react time is {react_time[i + 1] - react_time[i]}')
            num_22_react_time += react_time[i + 1] - react_time[i]
    print(f'the number of high frequency(11) is {num_11}')
    print(f'the number of low frequency(22) is {num_22}')
    print(f'the response accuracy of high frequency(11) is {num_11_correct / num_11}')
    print(f'the response accuracy of low frequency(22) is {num_22_correct / num_22}')
    print(f'the average of reaction time of high frequency(11) is {num_11_react_time / num_11}')
    print(f'the average of reaction time of low frequency(22) is {num_22_react_time / num_22}')


def main():
    calculate_accuracy()


if __name__ == '__main__':
    main()
