def main():
    with open('Day 1/input.txt') as input:
        char_Count = 0
        count = 0
        values = []
        for line in input:
            for character in line:
                if char_Count == -1:
                    values.append(count)
                if character == "(":
                    char_Count += 1
                elif character == ")":
                    char_Count -= 1
                count += 1
        print(f'Problem 1 Solution: {char_Count}')
        print(f'Problem 2 Solution: {values[0]}')

if __name__ == "__main__":
    main()