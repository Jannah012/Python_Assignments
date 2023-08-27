def most_frequent(string):
    # create a dictionary to store the frequency of each letter
    d = {}
    for i in string:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            
    sort_word=sorted(d.items(), key=lambda x: x[1],reverse=True)

    for item in sort_word:
        print(item[0], item[1])
    
string=input('please enter the string: ')            
most_frequent(string)            