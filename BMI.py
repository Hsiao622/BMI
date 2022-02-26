# BMI計算程式，判斷使用者為何種體型

height = input('請輸入身高: ')
height = float(height)
heightm = height * 0.01
weight = input('請輸入體重: ')
weight = float(weight)

bmi = weight / (heightm * heightm)
roundbmi = round(bmi, 2)
print('您的BMI為: ', roundbmi)

if bmi < 18.5:
    print('您的體型為', '過輕')
elif bmi >= 18.5 and bmi < 24:
    print('您的體型為', '正常')
elif bmi >= 24 and bmi < 27:
	print('您的體型為', '過重')
elif bmi >= 27 and bmi < 30:
    print('您的體型為', '輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('您的體型為', '中度肥胖')
else:
    print('您的體型為', '重度肥胖')