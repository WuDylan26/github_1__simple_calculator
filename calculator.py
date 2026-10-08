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

def calculator():
    print("===== 简易计算器 =====")
    print("支持运算：+  -  *  /")
    print("输入 q 随时退出程序\n")
    while True:
        # 获取第一个数字
        num1_input = input("请输入第一个数字：").strip()
        if num1_input.lower() == "q":
            print("程序退出👋")
            break
        try:
            num1 = float(num1_input)
        except ValueError:
            print("⚠️ 输入不是有效数字，请重试\n")
            continue

        # 获取运算符
        op = input("请输入运算符(+ - * /)：").strip()
        if op.lower() == "q":
            print("程序退出👋")
            break
        if op not in ["+", "-", "*", "/"]:
            print("⚠️ 运算符仅支持 + - * /\n")
            continue

        # 获取第二个数字
        num2_input = input("请输入第二个数字：").strip()
        if num2_input.lower() == "q":
            print("程序退出👋")
            break
        try:
            num2 = float(num2_input)
        except ValueError:
            print("⚠️ 输入不是有效数字，请重试\n")
            continue

        # 计算
        try:
            if op == "+":
                res = add(num1, num2)
            elif op == "-":
                res = subtract(num1, num2)
            elif op == "*":
                res = multiply(num1, num2)
            else:
                res = divide(num1, num2)
            print(f"✅ 结果：{num1} {op} {num2} = {res}\n")
        except ZeroDivisionError as e:
            print(e,"\n")

if __name__ == "__main__":
    calculator()