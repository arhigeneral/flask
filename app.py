from flask import Flask, request

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут (endpoint)

@app.route('/')
def hello():
    # Получение значения параметра 'name' из GET-запроса
    name = request.args.get('name')
    message = request.args.get('message')
    # Проверка наличия параметра 'name'
    if name:
        return f'Hello, {name}! {message}!'
    else:
        return 'Привет, незнакомец!'

if __name__ == '__main__':
    app.run()