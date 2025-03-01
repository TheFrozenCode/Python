import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenth = ""
password = ""
mode = 0

def generate():
  global password
  lenth = input("введите длинну вашего пароля")

  for i in range(int(lenth)):
    password += random.choice(symbols)

  print(password)

while True:
  mode = input('Что вы хотите сделать: Сгенерировать пароль(1) или добавить новый пароль(в разработке)')

  if mode == '1':
    generate()