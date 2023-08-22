from control_flow import admin_login, hows_the_weather, fizzbuzz, calculator

print(admin_login("sudo", "12345"))
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))

print(hows_the_weather(33))
print(hows_the_weather(99))
print(hows_the_weather(75))

print(fizzbuzz(1))
print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(5))
print(fizzbuzz(15))

print(calculator("+", 1, 1))
print(calculator("-", 3, 1))
print(calculator("*", 3, 2))
print(calculator("/", 4, 2))
print(calculator("nope", 4, 2))
