### poetry add django 해도 venv 폴더가 생성 되지 않을떄 사용하는 코드

poetry config virtualenvs.in-project true

poetry config virtualenvs.path "./.venv"

### poetry 가상환경 들어가기/나가기

1. 가상환경 들어가기  
poetry shell

2. 가상환경 나가기
exit

### 관리자 페이지 들어가기 / 나가기

1. 관리자 페이지 들어가기
python manage.py shell

2. 관리자 페이지 나가기
ctrl + D

### startapp + '이름' 사용
새로운 테이블 생성
'이름'이 테이블 이름에 됨

### makemigretions 사용
새로운 모델 추가, 혹은 모델객체 업데이트시 사용한다.
(각 테이블 안에 apps에 있는 class 네임을 config.settings.py >> INSTALLED_KEY 에 테이블.apps.클래스 로 입력해줘야 사용이 가능해짐)

### Common Model
- created_at: 데이터 생성 시간
- updated_at: 데이터 업데이트된 시간 (계속 최신화가 됩니다. 언제? 업데이트(수정)가 발생했을 때)

- boards (common) 
    - ~~created_at~~
    - ~~updated_at~~
- reviews (common)
    - ~~created_at~~
    - ~~updated_at~~
- common(models.Model)
    - created_at
    - updated_at

여러 곳에서 같은 필드를 사용하고 싶다면 각각 사용하수도 있지만
common 모델에 넣어두고 여기저기서 사용할수 있다.

### python 코딩 환경

1. 들어가는 법
python manage.py shell

들어가면 파이썬처럼 작성하면 됨

- 폴더.objects.명령어
- 객체 = 위 코드 를 사용해서 지정하고, dir(객체) 로 명령어를 알아볼수 있다.
  