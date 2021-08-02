#!/usr/bin/python3

import os

if __name__ == "__main__":

    file_input = r"C:\Users\roman\Desktop\test.txt"
    print(file_input)
    
    in_data = []
    with open(file_input) as f:
        in_data = f.readlines()
    
    for s in in_data:
        s = s.split(",")
        print(f"{s[1]}")
    
    print("\n")
    
    for s in in_data:
        s = s.split(",")
        print(f"{s[9]}".replace(".",","))
    