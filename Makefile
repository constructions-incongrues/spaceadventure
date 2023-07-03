start: install
	python3 ./src/spaceadventure

venv:
	python3 -m pip install --user pipx
	python3 -m pipx ensurepath
	pipx install virtualenv
	virtualenv venv
	source .venv/bin/activate

install: venv
	pip3 install -r ./requirements.txt
