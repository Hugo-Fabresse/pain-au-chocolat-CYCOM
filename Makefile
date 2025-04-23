APP_NAME := Audit

ENTRY_POINT := main.py

all: clean build

build:
	pyinstaller --onefile --name $(APP_NAME) --icon="image/logo.ico" $(ENTRY_POINT)
	mv dist/$(APP_NAME) ./
	rm dist

clean:
	rm -rf build dist __pycache__ $(APP_NAME).spec

fclean: clean
	rm $(APP_NAME)
