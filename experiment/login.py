username = "vicky"
password = "12345"

usern = input("Masukkkan Username : ")
Pass = input("Masukkan Password :" )

def calculator():
    print("Login Success")
    print("===Menu Calculator===")
    print("1.Tambahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    input("Pilih Operasi : ")

if usern == username and Pass == password:
    calculator()

elif usern != username and Pass == password:
    print("Username Wrong")

elif usern == username and Pass != password:
    print("Password wrong")

else:
    print("Please register")