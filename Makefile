venv:
	pipx install virtualenv
	virtualenv venv
	source .venv/bin/activate

install: venv
	pip3 install -r ./requirements.txt

start:
	python3 ./src/spaceadventure