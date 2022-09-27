# 2022/5/18 produced by JunWoo LEE, Soongsil Univ. This code is activated by python for physics experience coefficient of friction

import math

 

def CentripetalForce():

    print("구심력입니다.")

    force = round(mass*radius*(speed**2), 3)

    print("%.4f * %.2f * (%.2f^2) = %.3f" %(mass, radius, speed, force))

    print("")
    

def relativeerror():
    
    print("상대오차(힘센서 - 공식)입니다")
    
    force = round(mass*radius*(speed**2), 3)

    error = round(((n - force)/n)*100,1)

    print("((%.2f - %.3f)/%.2f)*100 = %.1f" %(n, force, n, error))

    print("")
    

 

 

while True:

   try:

       print("이 계산기는 물리 실험 중 구심력 측정 실험 계산을 위해 제작했습니다")

       print("")

 

       print("MKS단위계에 맞게 변형하여 대입하세요")

 

       mass = float(input("추질량을 입력하세요: "))

       radius = float(input("회전변경을 입력하세요: "))

       speed = float(input("각속도를 입력하세요"))

       n = float(input("구심력(힘센서 측정)을 입력하세요: "))

 

       print("")


 

 

   except Exception as e:

       print('Input Error!!! => ', e)

       print('처음부터 다시 입력해주세요...')

       print()

 

       continue

 

   else:
       
       CentripetalForce()
       
       relativeerror()

    
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

