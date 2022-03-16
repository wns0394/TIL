# a = 1

# def enclosed():
#     global a
#     a = 20

#     def local():
#         a = 300
#         print(a)
#     local()
#     print(a)

# enclosed()
# print(a)

a = 1

def enclosed(new_a):
    new_a = 20

    print(a)
    return new_a

a = enclosed(a)
print(a)
