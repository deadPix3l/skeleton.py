VENV_PATH = .venv

#================
# Git Submodules
#================
.PHONY: submodules
submodules: .gitmodules
.gitmodules:
	git submodule update --init

#=========
#  venv
#=========
venv: ${VENV_PATH}/bin/activate

${VENV_PATH}/bin/activate:
	uv venv ${VENV_PATH}
	${VENV_PATH}/bin/activate

.PHONY: clean-venv
clean-venv:
	rm -rf ${VENV_PATH}


install: submodules venv
	uv pip install -e .

