

def double_remover(input):
    cnt = 0
    remove_index = []
    ############ indexes of the string that are double letters ##########
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            cnt += 1 
        else:
            if cnt == 1:   
                remove_index.append(i)
                remove_index.append(i-1)
            cnt = 0
    if cnt == 1:   
                remove_index.append(i)
                remove_index.append(i+1)
    #####################################################################
    temp  = ''
    for i in range(len(input)):
        if not i in remove_index:
            temp += input[i]
    return temp

  
  
print(double_remover("aabbccccaa"))
            
