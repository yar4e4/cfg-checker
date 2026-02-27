# Config Checker
Простой CLI-инструмент на Go, который проверяет YAML-конфигурацию на наличие обязательных полей и корректность значений (например, version, host, port).

Проект создан для демонстрации навыков работы с Go + YAML + тестированием на Python/pytest.

# Функциональность
- Проверяет наличие полей `version` и `host`
- Проверяет диапазон порта (1–65535)
- Выводит ошибки в stderr и возвращает exit code 1 при проблемах
- При успехе выводит "Configuration is valid"

# Требования
- Go 1.22+
- Python 3.8+ с pytest

# Установка 
git clone https://github.com/твой_ник/config-validator.git
cd config-validator
go mod tidy

# Сборка
Bashgo build -o validator main.go
# С Makefile:
make build 

# Использование
Bash./validator path/to/config.yaml
Примеры:
Bash# Успех
./validator tests/data/valid.yaml
# → Configuration is valid

# Ошибка
./validator tests/data/missing_version.yaml
# → Validation failed:
#     - field 'version' is required

# Тестирование
Тесты написаны на Python + pytest (black-box подход: запускаем бинарник и проверяем вывод/код возврата).
make test
# или вручную:
cd tests
pytest -v

# Покрытие:
1. Валидный конфиг
2. Отсутствующие поля
3. Некорректные значения
4. Несуществующий файл

# Структура проекта
├── main.go               # основной код Go
├── go.mod / go.sum
├── Makefile              # удобные команды (build, test, clean)
├── tests/
│   ├── conftest.py
│   ├── test_validator.py
│   └── data/             # тестовые YAML-файлы
└── bin/                  # собранный бинарник (после запуска)

