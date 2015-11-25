
all: test doc sdist

clean: clean_doc clean_py clean_dist

clean_py: 
	rm -rf *.pyc

clean_doc:
	rm -rf docs/build/*

clean_dist:
	rm -rf dist/

doc: 
	cd docs; make html

sdist: clean_dist clean_py
	python setup.py sdist

upload: sdist
	python setup.py upload

test:
	nosetests tests/*

install:
	pip install -e .
