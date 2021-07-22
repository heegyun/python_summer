# import theater_module as tm
# from theater_module import price_soldier as price

# price(5)


# import travel.thailand
# from travel.thailand import ThailandPackage

# trip_to = ThailandPackage()
# trip_to.detail()

# 베트남 모듈만 import할 경우
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# trip_to2 = thailand.ThailandPackage()
# trip_to2.detail()

import inspect
import random
from bs4 import BeautifulSoup

print(inspect.getfile(random))