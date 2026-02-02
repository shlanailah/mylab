import datetime as dt
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

data_user = dt.date(tahun, bulan, tanggal)
print(f"\nYour born day is {data_user} on {data_user:%A}\n")

hari_ini = dt.date.today()
print(f"Today date is {hari_ini}\n")

umur = hari_ini - data_user
umur_tahun = umur.days // 365
umur_bulan = (umur.days%365)//30
umur_hari = (umur.days%365)%30
print(f"Your age today is {umur_tahun} year {umur_bulan} month {umur_hari} day\n")

#ulang tahun
ultah = data_user
if hari_ini > ultah:
    ultah = data_user.replace(year=data_user.year + 1)

print(f"Your next birthday is {ultah} on {ultah:%A}\n")

umur = ultah - hari_ini 
umur_tahun = umur.days // 365
umur_bulan = (umur.days%365)//30
umur_hari = (umur.days%365)%30
print(f"There is {umur_bulan} month and {umur_hari} days left until your next birthday\n")

cek = input("Want to check your birth stone? (Yes/No)\n")
#birth stone
birth_stone = {
    1: "Garnet",
    2: "Amethyst",
    3: "Aquamarine",
    4: "Diamond",
    5: "Emerald",
    6: "Pearl",
    7: "Ruby",
    8: "Peridot",
    9: "Sapphire",
    10: "Opal",
    11: "Topaz",
    12: "Turquoise"
}
bulan = data_user.month
if cek == "Yes":
    print(f"Your birth stone is {birth_stone[bulan]}\n")
print("Press Enter to exit")