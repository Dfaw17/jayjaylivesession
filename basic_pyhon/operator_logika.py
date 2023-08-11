# and | or

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

nilai_wajib = 60
nilai_optional = 50

nilai_kepribadian = 65

# agar kita bisa lulus nilai wajib atau nilai optional kita minimal 70

# (FALSE) or TRUE
if nilai_wajib > 70 and (nilai_optional >70 or nilai_kepribadian >70):
    print("Saya Lulus")
else:
    print("kamu tidak lulus")
