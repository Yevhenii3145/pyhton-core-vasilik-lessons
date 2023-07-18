# работа с секундами
from datetime import datetime, MINYEAR, MAXYEAR

d = datetime.now()
print(d.toordinal()) # 738718 кол-во дней с 01.01.01
print(d.timestamp()) # 1689590626.423964 кол-во секунд с 01.01.1970
