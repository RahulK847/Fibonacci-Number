num_list=[0,1]
num=int(input("enter the no. "))
while True:
  if len(num_list)==num:
    print(num_list)
    break
  else:
    new_num = num_list[-1] + num_list[-2]
    num_list.append(new_num)

