import sys
import os
import math

def prime(s):
    # your code goes here
    if s == 2 or s == 3:
        return True
    elif s % 2 == 0 or s % 3 == 0 or math.sqrt(s) == math.floor(math.sqrt(s)):
        return False
    else:
        return True
    
def solution(s):
    return prime(s)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
