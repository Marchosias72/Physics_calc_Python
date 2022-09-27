import math


while True:
    try:
        v = float(input("초기속도를 입력하세요:"))#초기속도
        g = 9.80 #중력가속도
        x= int(input()) #각도

        c = math.cos(math.radians(x)) #cos(x)
        s = math.sin(math.radians(x)) #sin(x)

    except Exception as e:
        print('Input Error!!! => ', e)
        print('처음부터 다시 입력해주세요...')
        print()

        continue

    else:
        formula = ((v*v*c)/g)*(s + math.sqrt(s**2 + ((2*9.80*0.1)/v**2)))

        print(formula)

        while True:
            repeat = input('Continue?(y/n): ')
            print()

            if repeat == 'y':
                break
            elif repeat == 'n':
                sys.exit()    # 프로그램 강제종료
            else:
                print('Please try again?')
                continue
    finally:
        pass
