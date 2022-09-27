# 2022/4/28 produced by JunWoo LEE, Soongsil Univ. This code is activated by python for physics experience law of conservation of mechanical energy

 

import math

 

def avecycle():

    average = (cycle + cycle2 + cycle3)/3

    print("평균 주기 입니다")

    print("(%.3f + %.3f + %.3f)/3 = %.3f" %(cycle, cycle2, cycle3, average))

    

def expercycle():

    experience = 2*math.pi*math.sqrt(mass/k)

    average = (cycle + cycle2 + cycle3)/3

    relative = ((experience - average)/experience) * 100

    print("주기 실험값입니다")

    print("2*%.3f*(%.3f / %.3f)^1/2 = %.3f" %(math.pi, mass, k, experience))

    print("")

    print("상대 오차입니다")

    print("((%.3f - %.3f)/%.3f) * 100 = %.3f" %(experience, average, experience, relative))

    

 

while True:

   try:

       print("이 계산기는 물리 실험 중 조화진동 실험을 위해 제작했습니다")

       print("<표3> 추의 질량에 따른 주기의 변화에 작성한 실험값을 입력하셔야합니다.")

       print("")

 

       print("MKS단위계에 맞게 변형하여 대입하세요")

 

       mass = float(input("추걸이 포함 추의 질량을 입력하세요: "))

       

       cycle = float(input("주기 1을 입력하세요: "))

       

       cycle2 = float(input("주기 2을 입력하세요: "))

       

       cycle3 = float(input("주기 3을 입력하세요: "))

       

       k = float(input("용수철 상수를 입력하세요: "))

 

   except Exception as e:

       print('Input Error!!! => ', e)

       print('처음부터 다시 입력해주세요...')

       print()

 

       continue

 

   else:

       avecycle()

       expercycle()

 

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
