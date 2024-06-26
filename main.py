def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
  
    minval, median, maxval = int()
    
    if num1 < num2 and num1 < num3:
        minval = num1
    else:
        if num2 < num1 and num2 < num3:
            minval = num2
        else:
            minval = num3
            
    median = num1 + num2 + num3 % 3
            
    if num1 > num2 and num1 > num3:
        maxval = num1
    else:
        if num2 > num1 and num2 > num3:
            maxval = num2
        else:
            maxval = num3
            

    print(minval, median, maxval)
    
    return minval, median, maxval


if __name__ == '__main__':
    main()
