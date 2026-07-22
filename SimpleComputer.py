def simple_calculator():
    try:
        num1=float(input("请输入数字1:"))
        operation=input("请输入运算符（+，-，*，/）:")
        num2=float(input("请输入数字2:"))

        if operation=="+":
            result =num1+num2
        elif operation=="-":
            result =num1-num2
        elif operation=="*":
            result =num1*num2
        elif operation=="/":
            if num2 != 0:
                result =num1/num2
            else:
                print("除数不能为零！请重新输入")
            return
        else:
            print("输入的运算符不支持！请重新输入")
            return
        print(f"结果：{num1} {operation} {num2} = {result}")
    except ValueError:
        print("输入的数字不支持！请重新输入")
simple_calculator()