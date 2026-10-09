import math

"""
简易命令行计算器
支持 + - * /，带异常捕获：除零错误、非法输入
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("❌ 除数不能为0！")
    return a / b

# ====== 新增阶乘函数 ======
def factorial(n):
    if not n.is_integer():
        raise ValueError("❌ 阶乘只支持整数！")
    n = int(n)
    if n < 0:
        raise ValueError("❌ 负数没有阶乘！")
    return math.factorial(n)

def calculator():
    print("===== 简易计算器 =====")
    print("支持运算：+ - * /")
    print("阶乘使用示例：5 !")
    print("输入 exit 退出程序\n")

    # 运算字典
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "!": factorial
    }

    while True:
        user_input = input("请输入计算式：")
        if user_input.lower() == "exit":
            print("程序退出")
            break
        
        parts = user_input.split()
        try:
            # 处理阶乘：一元运算，格式：数字 !
            if len(parts) == 2 and parts[1] == "!":
                num = float(parts[0])
                op = parts[1]
                res = operations[op](num)
                print(f"结果：{res}\n")
                continue
            
            # 处理加减乘除：二元运算，格式：数字 op 数字
            if len(parts) != 3:
                print("⚠️ 格式错误！")
                print("二元运算示例：10 + 3")
                print("阶乘示例：5 !\n")
                continue

            num1, op, num2 = parts
            num1 = float(num1)
            num2 = float(num2)

            if op not in operations:
                print("⚠️ 不支持该运算符\n")
                continue
            
            res = operations[op](num1, num2)
            print(f"结果：{res}\n")
        
        # 捕获异常，和你原来代码风格保持一致
        except ZeroDivisionError as err:
            print(err,"\n")
        except ValueError as err:
            print(err,"\n")
        except Exception:
            print("⚠️ 输入非法，请重试！\n")

if __name__ == "__main__":
    calculator()