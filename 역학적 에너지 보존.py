# 2022/4/28 produced by JunWoo LEE, Soongsil Univ. This code is activated by python for physics experience law of conservation of mechanical energy

import math

def velocity1():
    print("sqrt.2gh입니다")
    velo = round(math.sqrt(2*g*max), 3)
    print("결과 값은 %.3f 입니다" %velo)
    a.append(velo)
    print("")

def velocity2():
    print("sqrt.(g/h)*D/sqrt.(H)")
    velo2 = round(math.sqrt(g/2)*(horizon/math.sqrt(vertical)), 3)
    print("결과 값은 %.3f 입니다" %velo2)
    a.append(velo2)
    print("")

def percentage():
    print("퍼센트 오차")
    velo = math.sqrt(2*g*max)
    velo2 = math.sqrt(g/2)*(horizon/math.sqrt(vertical))
    percent = round(((velo-velo2)/velo)*100, 1)
    print("결과 값은 %.1f 입니다" %percent)
    a.append(percent)
    print("")

def energymax():
    print("최고점에서 퍼텐셜에너지")
    energy = round(mass*g*max, 3)
    print("결과 값은 %.3f J입니다" %energy)
    b.append(energy)
    print("")

def energymim():
    print("최저점에서 에너지")
    velo2 = math.sqrt(g/2)*(horizon/math.sqrt(vertical))
    energy2 = round(0.5 * mass * velo2 * velo2, 3)
    print("결과 값은 %.3f J입니다" %energy2)
    b.append(energy2)
    print("")

def energychange():
    print("에너지 변화율")
    energy = mass*g*max
    velo2 = math.sqrt(g/2)*horizon/math.sqrt(vertical)
    energy2 = 0.5 * mass * velo2 * velo2 
    change = round(((energy - energy2)/energy)*100, 1)
    print("결과 값은 %.1f 입니다" %change)
    b.append(change)
    print("")

while True:
    try:
        print("이 계산기는 물리 실험 중 역학적 에너지 보존 실험 계산을 위해 제작했습니다")
        print("")

        print("MKS단위계에 맞게 변형하여 대입하세요")

        mass = float(input("추의 질량을 입력하세요: "))

        max = float(input("추의 최고점 높이 h 를 입력하세요: "))

        vertical = float(input("추의 낙하 거리 H 를 입력하세요: "))

        horizon = float(input("추의 수평이동 거리 D 를 입력하세요: "))

        print("")

        g = 9.80

        list1 = ["실험차수","vb","Vb","(vb-Vb)/vb"]
        list2 = ["실험차수","Et","Eb","(Et-Eb)/Et"]
        a = ["결과값"]
        b = ["결과값"]


    except Exception as e:
        print('Input Error!!! => ', e)
        print('처음부터 다시 입력해주세요...')
        print()

        continue

    else:
        velocity1()
        velocity2()
        percentage()
        energymax()
        energymim()
        energychange()

        list1.append(a)
        list2.append(b)

        print("대괄호 속에 있는 대괄호의 3개의 수가 실험책에 있는 표랑 동일한 배열입니다")

        print("표2번")
        print("")

        print(list1)
        print("")

        print("표 3번")
        print("")

        print(list2)
        print("")

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
