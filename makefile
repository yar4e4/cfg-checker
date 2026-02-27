.PHONY: build test clean

build:
	go build -o bin/validator main.go

test: build
	cd tests && pytest -v

clean:
	rm -f bin/validator
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +