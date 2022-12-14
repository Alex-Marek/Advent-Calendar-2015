def main():
    with open('Day 2/input.txt') as input:
        P1_Count = 0
        P2_Count = 0
        for line in input:
            line = line.strip("\n")
            values = line.split('x')
            values[0], len = int(values[0]), int(values[0])
            values[1], wid = int(values[1]), int(values[1])
            values[2], hei = int(values[2]), int(values[2])
            surface_Area = (2*len*wid) + (2*wid*hei) + (2*hei*len)
            values.sort()
            ribbon = (2*(values[0]) + 2*(values[1])) + (values[0]*values[1]*values[2])
            P2_Count += ribbon
            P1_Count += surface_Area + (values[0] * values[1])
        print(f'Problem 1 Solution: {P1_Count}')
        print(f'Problem 1 Solution: {P2_Count}')

if __name__ == "__main__":
    main()
