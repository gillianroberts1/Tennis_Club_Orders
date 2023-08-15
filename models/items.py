from models.item import *
import datetime

wilson_pro = 'wilson_pro_staff.jpg'
babolat_aero = 'babolat_aero_rafa.jpg'
head_radical = 'head_radical.jpg'

item1 = Item(datetime.date(2023, 8, 4), "Gillian", 1, "Wilson, Pro Staff", 150.00, wilson_pro)
item2 = Item(datetime.date(2023, 7, 30), "Carmen", 2, "Babolat, Pure Aero Rafa", 260.00, babolat_aero)
item3 = Item(datetime.date(2023, 8, 2), "Louise",3, "Head, Radical Pro",  280.00, head_radical)

items = [item1, item2, item3]
 


