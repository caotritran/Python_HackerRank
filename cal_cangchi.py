

CAN = ['Canh', 'Tan', 'Nham', 'Quy', 'Giap', 'At', 'Binh', 'Dinh', 'Mau', 'Ky']
CHI = ['Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu', 'Dan', 'Meo', 'Thin', 'Ty', 'Ngo', 'Mui', ]

year = int(input("Nhap so nam can tinh can chi: "))
_can = year%10
_chi = year%12

canchi = CAN[_can] + " " + CHI[_chi]


print('can chi nam {} se la: {}'.format(year, canchi))
