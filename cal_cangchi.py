'''
Can được tính là lấy năm sinh chia cho 10 và lấy số dư. 
Số dư bằng 0 (chia hết) thì tương ứng với Canh, 1 thì tương ứng với Tân và cứ tiếp tục như thế đến số dư là 9 tương ứng với Kỷ.
Tiếp theo là tính Chi. Chắc các bạn cũng đoán được là mình sẽ lấy năm sinh chia cho 12 và lấy số dư để suy ra chi. 
Tuy nhiên một điều lưu ý là với số dư bằng 0 (chia hết) thì sẽ tương ứng với Thân, 
1 tương ứng với Dậu và cứ tiếp tục như vậy đến hết.
'''

CAN = ['Canh', 'Tan', 'Nham', 'Quy', 'Giap', 'At', 'Binh', 'Dinh', 'Mau', 'Ky']
CHI = ['Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu', 'Dan', 'Meo', 'Thin', 'Ty', 'Ngo', 'Mui', ]

year = int(input("Nhap so nam can tinh can chi: "))
_can = year%10
_chi = year%12

canchi = CAN[_can] + " " + CHI[_chi]


print('can chi nam {} se la: {}'.format(year, canchi))
