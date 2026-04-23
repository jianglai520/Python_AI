#异常处理

#NameError
# try:
#     print("---------------------")
#     print(my_name)
#     print("---------------------")
# except NameError as e:   #捕获NameError类型的异常
#     print("程序出错了,异常信息是:", e)  #知道错误信息点


#ZeroDivisionError
try:
    print("---------------------")
    # print(my_name)
    # print(1 / 0)
    # print("abc"[10])
    # print("abc".hello)
    print("---------------------")
except ZeroDivisionError as z:     #捕获ZeroDivisionError类型的异常
    print("0不能做除数,异常信息是:", z)     #知道错误信息点
except NameError as e:   #捕获NameError类型的异常
    print("名字不存在，请检查变量或者函数名,异常信息是:", e)  #知道错误信息点
except IndexError as i:
    print("索引错误,异常信息是:", i)
except TypeError as t:
    print("类型错误,异常信息是:", t)
except KeyError as k:
    print("关键字错误,异常信息是:", k)
except AttributeError as a:
    print("3333")
except Exception as e:  #捕获所有异常
    print("程序出错了", e)

# except:
#     print("程序出错了")

finally:   #无论程序是否正常运行，finally中的代码都会运行
    print("资源释放")

