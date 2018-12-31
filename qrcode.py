from pyqrcode import QRCode
ur1 = QRCode ('http://www.ntu.edu.tw')
ur1.svg('ur1.svg', scale = 10)
ur1.png('ur1.png', scale = 10)
