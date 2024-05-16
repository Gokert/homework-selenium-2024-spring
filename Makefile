.PHONY: GetReq RunAllTests RunFallTests RunCurrentTest

GetReq:
	pip freeze > requirements.txt

RunAllTests:
	pytest hw/code/

RunFallTests:
	pytest hw/code/ --lf --setup-show --capture=no

RunCurrentTest:
	pytest hw/code/$(testName) --lf --setup-show --capture=no

#
#pytest	--setup-show
#pytest	--setup-show --capture=no