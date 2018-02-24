import vk, time

print("Добро пожаловать!")
print("Данный скрипт создан с целью троллинга пользователей ВК, постоянно набирающимся текстом.")
print("Что бы начать использование, неаоходимо авторизоваться под реальными данными ВК и указать ID чата.")
print("Автор скрипта: Осипов Илья.\nВерсия 0.2 beta.")
input("Что бы начать, нажмите Enter")
print("\n")

multi = False
login = input("Телефон или Email: ")
password = input("Пароль: ")
chatID = input("ID чата: ")
more = input("Больше 2х участников(y/n): ")
if more == "y":
	chatID = int(chatID)
	multi = True
print("\n")

session = vk.AuthSession('6240306', login, password, scope='messages')
print("Запуск сессии...")
vk_api = vk.API(session, v=5.38)
print("Подкллючение API...")
print("Понеслась))\n")

while True:
	if multi == True:
		var = vk_api.messages.setActivity(chat_id=chatID, type='typing', peer_id=2000000000+chatID)
		if var == 1:
			print("Успешно")
			time.sleep(5)
	else:
		var = vk_api.messages.setActivity(chat_id=chatID, type='typing', peer_id=chatID)
		if var == 1:
			print("Успешно")
			time.sleep(5)