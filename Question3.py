sentence = input('Enter a sentence: ')
keyword = input("Enter the word: ")
input_sentence = sentence.split()
# for i in input_sentence:
#     print (i)
    # if i in input_sentence > 1:
        # pass
        # print(i)
    # print(i)
    # pass
# print(sentence)
    # if i in sentence>1:
    #     pass
    # else:
    #     index = input_sentence(keyword)
    #     print(input_sentence)
# index = input_sentence.index(keyword)
# print(index+1)
# 
if keyword in input_sentence:
    for index, word in enumerate(input_sentence):
        if word == keyword:
            print(F"{keyword} : { index}")
else:
    print(0)