.PHONY: GetReq RunAllTests RunFallTests RunCurrentTest

GetReq:
	pip freeze > requirements.txt

RunAllTests:
	pytest hw/code/

RunFallTests:
	pytest hw/code/ --lf --setup-show --capture=no

RunCurrentTestSuit:
	pytest hw/code/$(testName)

RunCurrentTestCase:
	pytest hw/code/$(testName) -k "$(testSuit)"

#
#pytest	--setup-show
#pytest	--setup-show --capture=no