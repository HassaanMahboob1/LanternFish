data = [3,4,3,1,2]
RESET = 7
NEWFISH = 8
for y in range(18):
  for i in range(len(data)):
    if(data[i] == 0):
      data.append(NEWFISH)
      data[i] = RESET
    data[i] = data[i] - 1 

print(len(data))