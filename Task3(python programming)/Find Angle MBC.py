# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=float(input())
BC=float(input())
AC=math.sqrt(pow(AB,2)+pow(BC,2))

MC=AC/2.0


angle=math.degrees(math.asin(MC/BC))

print str(int(round(angle)))