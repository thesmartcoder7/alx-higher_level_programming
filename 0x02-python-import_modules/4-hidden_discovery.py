#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    func_names = dir(hidden_4)

    for i in range(len(func_names)):
        if func_names[i][:2] != '__':
            print(func_names[i])

    exit()
