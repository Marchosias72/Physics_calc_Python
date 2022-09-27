import math 


def momentumbefore():
    print("충돌 전후의 운동량의 크기")
    mb = m1*r/t
    print("충돌 전 입사구의 운동량: %.3f" % mb)
    print("")

def momentumafter():
    mx = m1*r1/t
    my = m2*r2/t
    print("충돌 후 입사구의 운동량: %.3f" %mx)
    print("충돌 후 표적구의 운동량: %.3f" %my)
    print("")


def horizonmomentum():
    print("입사 방향의 운동량 성분")
    p1 = m1*r/t
    p2 = ((m1*r1/t)*c1) + ((m2*r2/t)*c2)
    p3 = p2 - p1
    print("충돌 전 p1: %.3f" %p1)
    print("충돌 후 : %.3f" %p2)
    print("충돌 전후 차이: %.3f" %p3)
    print("")


def verticalmomentum():
    print("입사 방향의 수직인 운동량 성분")
    p1 = 0
    p2 = ((m1*r1/t)*s1) - ((m2*r2/t)*s2)
    p3 = p2 - p1
    print("충돌 전 p1: %.3f" %p1)
    print("충돌 후 : %.3f" %p2)
    print("충돌 전후 차이: %.3f" %p3)
    print("")

def energy():
    print("충돌 전후 운동 에너지 비교")
    e1 = (m1*r/t)*(m1*r/t)/(2*m1)
    e2 = (m1*r1/t)*(m1*r1/t)/(2*m1) + (m2*r2/t)*(m2*r2/t)/(2*m2)
    e3 = ((e1 - e2)/e1)*100
    print("충돌전 운동에너지: %.3f" %e1)
    print("충돌후 운동에너지: %.3f" %e2)
    print("에너지 손실률: %.1f" %e3)
    print("")



while True:
    try:
        print("MKS단위계에 맞게 변형하여 대입하세요")    
        g = 9.80    
        m1 = float(input("입사구의 질량을 입력하세요:"))
        m2 = float(input("표적구의 질량을 입력하세요:"))

        h = float(input("H을 입력하세요:"))

        r = float(input("R값 을 입력하세요:"))
        r1 = float(input("R1값, 입사구 이동거리를 입력하세요:"))
        r2 = float(input("R2값, 표적구 이동거리를 입력하세요:"))

        theta = float(input("입사구 각도를 입력하세요:"))
        theta2 = float(input("표적구 각도를 입력하세요:"))
        print("")

        c1 = math.cos(math.radians(theta))
        s1 = math.sin(math.radians(theta))
        c2 = math.cos(math.radians(theta2))
        s2 = math.sin(math.radians(theta2))

        t = math.sqrt(2*h/g)

    except Exception as e:
        print('Input Error!!! => ', e)
        print('처음부터 다시 입력해주세요...')
        print()

        continue

    else:
        momentumbefore()
        momentumafter()
        horizonmomentum()
        verticalmomentum()
        energy()

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
    
