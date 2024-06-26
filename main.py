
def main():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    num3 = float(input('Enter the third number: '))
  
    minval = int()
    maxval = int()
    median = int()

    if num1 < num2 and num1 < num3:
        minval = num1
    else:
        if num2 < num1 and num2 < num3:
            minval = num2
        else:
            minval = num3
            
    median = (num1 + num2 + num3) / 3 
            
    if num1 > num2 and num1 > num3:
        maxval = num1
    else:
        if num2 > num1 and num2 > num3:
            maxval = num2
        else:
            maxval = num3
            

    print(f'{minval}, {median:.2f}, {maxval}')
    
    return minval, median, maxval


if __name__ == '__main__':
    main()
