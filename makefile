all:
	@python setup.py build_ext -i -c mingw32
run:
	@python main.py
	@python one_line.py
clean:
	@rm build -rf
	@rm *.c *~
