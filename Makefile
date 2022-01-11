install:
	poetry install

build: install
	poetry build

package-install: build
	python3 -m pip install --user dist/*.whl --force-reinstall

clean:
	rm /tmp/i3-show-desktop.log 2> /dev/null

show-desktop:
	poetry run i3-show-desktop
