def num_to_words(n):
    number = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    nty = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teen = ["Ten", "Eleven", "Twelve", "Thirteen", "Forteen", "Fifteen", "Sixteen", "Seventeen", "Eiighteen", "Nineteen"]
    if n>9999999:
        print("Error! Can't solve for more than 7 digits!")
    else:
        d = [0,0,0,0,0,0,0]
        i = 0
        while n>0:
            d[i]=n%10
            i+=1
            n=n//10
        num=""
        if d[6]!=0:
            if(d[6]==1):
                num += teen[d[5]] + " Lac "
            else:
                num += nty[d[6]] + " " + number[d[5]] + " Lac "
        else:
            if d[5]!=0:
                num += number[d[5]] + " Lac "
        if d[4]!=0:
            if(d[4]==1):
                num += teen[d[3]] + " Thousand "
            else:
                num += nty[d[4]] + " " + number[d[3]] + " Thousand "
        else:
            if d[3]!=0:
                num += number[d[3]] + " Thousand "
        if d[2]!=0:
            num += number[d[2]] + " Hundred "
        if d[1]!=0:
            if (d[1] == 1):
                num += teen[d[0]]
            else:
                num += nty[d[1]] + " " + number[d[0]]
        else:
            if d[0] != 0:
                num += number[d[0]]
    return num
    
n = int(input("Enter a number upto 7 digits: "))
print((num_to_words(n)))