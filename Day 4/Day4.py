from hashlib import md5

SECRET_KEY = "bgvyzdsv"
def main():
    count = 0
    has_Hit = False
    while True:
        cur_String = SECRET_KEY + str(count)
        result = md5(cur_String.encode()).hexdigest()
        str_Hash = str(result)
        if str_Hash[0:5] == "00000" and has_Hit == False:
            print(f'Problem 1 solution:{str_Hash} found at: {count}')
            has_Hit = True
        if str_Hash[0:6] == "000000":
            print(f'Problem 2 solution:{str_Hash} found at: {count}')
            break
        count += 1

if __name__ == "__main__":
    main()