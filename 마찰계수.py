# 2022/6/01 produced by JunWoo LEE, Soongsil Univ. This code is activated by python for physics experience vibration 

import math

 

def friction():

    print("마찰계수입니다.")

    fric = round((mass2*g - (mass + mass2) * a)/(mass * g), 3)

    print("(%.4f * 9.80 - (%.4f + %.4f) * %.3f)/(%.4f * 9.80) = %.3f 입니다" %(mass2, mass, mass2, a, mass, fric))

    print("")

 

 

while True:

   try:

       print("이 계산기는 물리 실험 중 마찰 계수 측정 실험 계산을 위해 제작했습니다")

       print("")

 

       print("MKS단위계에 맞게 변형하여 대입하세요")

 

       mass = float(input("M(질량통)의 질량을 입력하세요: "))

       mass2 = float(input("m(추걸이 질량)의 질량을 입력하세요: "))

       a = float(input("가속도를 입력하세요: "))

 

       print("")

 

       g = 9.80

 

 

   except Exception as e:

       print('Input Error!!! => ', e)

       print('처음부터 다시 입력해주세요...')

       print()

 

       continue

 

   else:

       friction()

 

       

 

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
