H = float(input('input your height '))/100
W = float(input('input your weight '))
BMI = W/(H*H)

if BMI < 18.5:
  print("too thin")
elif BMI >= 18.5 and BMI <= 25:
  print("in normal range")
else:
  print("too heavy")