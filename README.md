# API тесты для сервиса «Яндекс Самокат»
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска тестов с созданием отчёта — pytest -v tests/ --alluredir=allure_results.
4. Посмотреть отчёт о тестировании — allure serve allure_results.