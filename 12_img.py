# 이미지보여주기
import matplotlib.pyplot as plt
from PIL import Image

digitImg = Image.open("digit_5.png")
plt.imshow(digitImg)
plt.show()

