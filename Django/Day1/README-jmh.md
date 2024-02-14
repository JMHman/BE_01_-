### poetry add django 해도 venv 폴더가 생성 되지 않을떄 사용하는 코드

poetry config virtualenvs.in-project true

poetry config virtualenvs.path "./.venv"