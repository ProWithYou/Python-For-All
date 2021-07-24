array = ['1등','2등','3등','4등','5등']
print(len(array))
array_lib = {}
for i in array:
    input_data = input('{0}은 누구입니까? : '.format(i) )
    array_lib[i] = [input_data]
    # input_data = input(array[i],"를 입력하세요 : ")
    # array_lib = { array[i] : input_data}
print("입력이 완료 되었습니다\n")
for i in array_lib :
    print(i, " : ", array_lib[i])
array_lib
print("끝")
