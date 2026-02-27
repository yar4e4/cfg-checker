# Config Checker

Простой CLI-инструмент на Go, который проверяет YAML-конфигурацию на наличие обязательных полей и корректность значений (например, `version`, `host`, `port`).

Проект создан для демонстрации навыков работы с Go + YAML + тестированием на Python/pytest.

## Функциональность

- Проверяет наличие полей `version` и `host`
- Проверяет диапазон порта (1–65535)
- Выводит ошибки в stderr и возвращает exit code 1 при проблемах
- При успехе выводит «Configuration is valid»

## Требования

- Go 1.22+
- Python 3.8+ с установленным `pytest`

## Установка

```bash
git clone https://github.com/твой_ник/config-checker.git
cd config-checker
go mod tidy
Сборка
Bash# Простой способ
go build -o validator main.go

# Или с Makefile (рекомендуется)
make build
Использование
Bash./validator path/to/config.yaml
Примеры
Успешный запуск:
Bash./validator tests/data/valid.yaml
Вывод:
textConfiguration is valid
Запуск с ошибкой:
Bash./validator tests/data/missing_version.yaml
Вывод:
textValidation failed:
  - field 'version' is required
Тестирование
Тесты написаны на Python + pytest (black-box подход: запускаем бинарник и проверяем вывод / код возврата).
Запуск тестов:
Bash# С Makefile
make test

# Вручную
cd tests
pytest -v
Покрываемые сценарии:

Валидный конфиг
Отсутствующие обязательные поля
Некорректные значения (например, порт вне диапазона)
Несуществующий файл

Структура проекта
text.
├── main.go               # основной код Go
├── go.mod
├── go.sum
├── Makefile              # удобные команды: build, test, clean
├── pytest.ini
├── tests/
│   ├── conftest.py
│   ├── test_validator.py
│   └── data/             # тестовые YAML-файлы
└── bin/                  # (опционально) собранный бинарник