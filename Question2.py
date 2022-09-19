number = int(input("Enter a number: "))
# if len(number) == 2:
#     tens = int(number)//10
#     print('tens')
# elif len(number) == 3:
#     hundred = int(number)// 100
#     print("hundred")
# elif len(number) == 4:
#     thousand = int(number) // 1000
#     print('thousand')
# elif len(number) == 5:
#     ten_thousand = int(number) // 10000
#     print('ten_thousand')
# elif len(number) == 6:
#     hundred_thousand = int(number) // 100000
#     print('hundred_thousand')
# elif len(number) == 7:
#     million = int(number) // 1000000
#     print('million')
# else:
#     print(None)
if number // 100 == 0:
    print('tens')
elif number // 1000 == 0:
    print('hundred')
elif number // 10000 == 0:
    print('thousand')
elif number // 100000 == 0:
    print ('Ten thousand')
elif number // 1000000 == 0:
    print('Hundred Thousand')
elif number // 10000000 == 0:
    print('Million')