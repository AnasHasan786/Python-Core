# finally
try:
    f = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found!!")
except Exception:
    print("Something is wrong, Please try again!!")
else:
    print(f.read())
finally:
    print("This will definitely get printed!!")
