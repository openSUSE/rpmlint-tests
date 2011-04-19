all:
	@echo "nothing to do here"

test:
	@./run

dist:
	@./mktar

clean:
	rm -rf output

.PHONY: dist clean test all
