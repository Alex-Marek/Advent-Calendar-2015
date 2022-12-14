with open('Day 3/input.txt') as input:
    p1x,p1y = 0,0
    x1,y1 = 0,0
    x2,y2 = 0,0
    locations1 = {(0,0)}
    locations2 = {(0,0)}
    char_Count = 0
    for line in input:
        line = line.strip("\n")
        for character in line:
            if char_Count % 2 == 0:         #Santa
                if character == ">":
                    x1 += 1
                    p1x += 1
                elif character == "<":
                    x1 -= 1
                    p1x -= 1
                elif character == "^":
                    y1 += 1
                    p1y += 1
                elif character == "v":
                    y1 -= 1
                    p1y -= 1
                locations1.add((p1x,p1y))
                locations2.add((x1,y1))

            elif char_Count % 2 == 1:       #Robo-Santa
                if character == ">":
                    x2 += 1
                    p1x += 1
                elif character == "<":
                    x2 -= 1
                    p1x -= 1
                elif character == "^":
                    y2 += 1
                    p1y += 1
                elif character == "v":
                    y2 -= 1
                    p1y -= 1
                locations1.add((p1x,p1y))
                locations2.add((x2,y2))
            char_Count += 1
    print(len(locations1))
    print(len(locations2))