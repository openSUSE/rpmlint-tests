all:
	@echo "nothing to do here"

test:
	@./run

dist:
	@obs/mktar

package:
	@obs/mkpackage

clean:
	rm -rf output rpms

.PHONY: dist clean test all
