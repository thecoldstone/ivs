.PHONY: all prepare-dev venv lint test run shell clean build install
SHELL=/bin/bash

VENV_NAME?=venv
VENV_BIN=$(shell pwd)/${VENV_NAME}/bin
VENV_ACTIVATE=. ${VENV_BIN}/activate

PYTHON=${VENV_BIN}/python3


all: build

prepare-dev:
	which dpkg-buildpackage || apt install -y debhelper dh-virtualenv dh-systemd lintian

	which python3 || apt install -y python3 python3-pip
	which virtualenv || python3 -m pip install virtualenv
	which python-tk || apt install -y python-tk
	make venv

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip setuptools
	${PYTHON} -m pip install -e .[devel]
	${PYTHON} -m pip install pyinstaller
	touch $(VENV_NAME)/bin/activate

test: venv
	${PYTHON} -m pytest -vv tests

run: venv
	${PYTHON} run

shell: venv
	${PYTHON} shell

clean:
	find . -name '*.pyc' -exec rm --force {} +
	rm -rf $(VENV_NAME) *.eggs *.egg-info dist build docs/_build .cache

build: venv
	dpkg-buildpackage -us -uc -b
	lintian ../webapp_1.0_all.deb

install:
	-dpkg -i ../webapp_1.0_all.deb
	apt install -f
