from logger import *
import pandas as pd

file_path = '../data/'
sys.stdout = Logger(sys.stdout)


def calculate_accuracy():
    odd_data = pd.read_csv(file_path + 'information.csv')
    code_num = [int(i) for i in odd_data['事件码']]
    react_time = [int(i) for i in odd_data['反应时间']]
    num_31, num_32, num_33, num_41, num_42, num_43, num_51, num_52, num_53 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    num_3_correct, num_3_incorrect, num_4_correct, num_4_incorrect, num_5_correct, num_5_incorrect = 0, 0, 0, 0, 0, 0
    num_3_react_time, num_4_react_time, num_5_react_time = 0, 0, 0
    effective_judge, ineffective_judge = 0, 0
    for i in range(len(code_num)):
        if code_num[i] == 31:
            num_31 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            elif code_num[i + 1] == 2:
                effective_judge += 1
                num_3_incorrect += 1
                num_3_react_time += react_time[i + 1] - react_time[i]
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 32:
            num_32 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                num_3_correct += 1
                num_3_react_time += react_time[i + 1] - react_time[i]
            elif code_num[i + 1] == 2:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 33:
            num_33 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            elif code_num[i + 1] == 2:
                effective_judge += 1
                num_3_incorrect += 1
                num_3_react_time += react_time[i + 1] - react_time[i]
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 41:
            num_41 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            elif code_num[i + 1] == 2:
                effective_judge += 1
                num_4_incorrect += 1
                num_4_react_time += react_time[i + 1] - react_time[i]
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 42:
            num_42 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                num_4_correct += 1
                num_4_react_time += react_time[i + 1] - react_time[i]
            elif code_num[i + 1] == 2:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 43:
            num_43 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            elif code_num[i + 1] == 2:
                effective_judge += 1
                num_4_incorrect += 1
                num_4_react_time += react_time[i + 1] - react_time[i]
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 51:
            num_51 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            elif code_num[i + 1] == 2:
                effective_judge += 1
                num_5_incorrect += 1
                num_5_react_time += react_time[i + 1] - react_time[i]
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 52:
            num_52 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                num_5_correct += 1
                num_5_react_time += react_time[i + 1] - react_time[i]
            elif code_num[i + 1] == 2:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
        elif code_num[i] == 53:
            num_53 += 1
            if code_num[i + 1] == 1:
                effective_judge += 1
                print(f'judge wrong at line {i + 2}')
            elif code_num[i + 1] == 2:
                effective_judge += 1
                num_5_incorrect += 1
                num_5_react_time += react_time[i + 1] - react_time[i]
            else:
                ineffective_judge += 1
                print(f'ineffective judge at line {i + 2}')
    print(f'three sectors have information correct accuracy:{num_3_correct / num_32}')
    print(f'three sectors have no information correct accuracy:{num_3_incorrect / (num_31 + num_33)}')
    print(f'the average of reaction time of three sectors is:{num_3_react_time / (num_3_correct + num_3_incorrect)}')
    print(f'four sectors have information correct accuracy:{num_4_correct / num_42}')
    print(f'four sectors have no information correct accuracy:{num_4_incorrect / (num_41 + num_43)}')
    print(f'the average of reaction time of four sectors is:{num_4_react_time / (num_4_correct + num_4_incorrect)}')
    print(f'flower and bird pattern have information correct accuracy:{num_5_correct / num_52}')
    print(f'flower and bird pattern have no information correct accuracy:{num_5_incorrect / (num_51 + num_53)}')
    print(
        f'the average of reaction time of flower and bird pattern is:{num_5_react_time / (num_5_correct + num_5_incorrect)}')


def main():
    calculate_accuracy()


if __name__ == '__main__':
    main()
