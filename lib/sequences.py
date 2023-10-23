#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    next_el = 0
    i = 1
    while len(fib_list) < length:
        fib_list.append(next_el)
        next_el, i = i, next_el + i
    print(fib_list)

print_fibonacci(10)