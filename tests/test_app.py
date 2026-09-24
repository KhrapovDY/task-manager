from flask import Flask 
import unittest 
 
def create_app(): 
    """Функция создает тестовый экземпляр приложения""" 
    app = Flask(__name__) 
    @app.route('/') 
    def index(): 
        return "Welcome to Task Manager!" 
    return app 
 
class TestTaskManager(unittest.TestCase): 
    """Класс тестов для приложения""" 
 
    def setUp(self): 
        """Вызывается перед каждым тестом — создаём тестовый клиент""" 
        self.app = create_app() 
        self.client = self.app.test_client() 
 
    def test_index(self): 
        """Тест проверяет, что главная страница возвращает ожидаемый результат""" 
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.data.decode(), "Welcome to Task Manager!") 
 
if __name__ == '__main__': 
    import pytest 
    pytest.main()