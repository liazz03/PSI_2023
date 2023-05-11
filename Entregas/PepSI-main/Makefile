dropdb:
	dropdb -U alumnodb -h localhost psi
createdb:
	createdb -U alumnodb -h localhost psi
	./migration.sh
	python3 populate_catalog.py
tests_all: tests_1 tests_2 tests_3
tests_1:
	python3 manage.py test catalog.tests.test_first_week --verbosity 2
tests_2:
	python3 manage.py test catalog.tests.test_second_week --verbosity 2
tests_3:
	echo "no test defined"
