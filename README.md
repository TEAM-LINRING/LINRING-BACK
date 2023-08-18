LINRING - Server
================
![Python](https://img.shields.io/badge/python-3.11-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![Django](https://img.shields.io/badge/django-4.24-092e20?style=for-the-badge&logo=django&logoColor=ffffff)

최종 사용자를 위한 LINRING API 서버

LINRING API server for End-user

Branches
================
- `main` : 최신 릴리즈 브랜치(Latest release branch)
- `develop` : 개발 브랜치(development branch)
- `[issue-type]/[issue-contents]` : 이슈 관련 브랜치, `git flow` 개발 계획의 브랜치 전략을 일부 참고하였습니다. source branch는 `develop`입니다.

Development Guide
================
## Initializing

❗️ **주의 사항** ❗️
1. LINRING API 서버는 Python 가상 환경 `venv`에서 생성 되었습니다.
2. 프로젝트의 root 디렉토리에 `secrets.json` 파일이 존재해야 정상적으로 동작합니다.

**secrets.json**
```json
{
	"SECRET_KEY": "LINRINGSECRETKEY"
}
```
기본적으로 secret key는 TEAM LINRING 안에서 공유됩니다.


Clone repository(레포지토리 클론):
> $ git clone https://github.com/TEAM-LINRING/LINRING-BACK.git

Install dependencies(의존성 설치):
> $ pip install -r requirements.txt

Create development database(개발용 DB 생성):
> $ ./manage.py migrate

Start Django development server(개발용 Django 서버 시작):
> $ ./manage.py runserver

브라우저를 통하여 [http://127.0.0.1:8000](http://127.0.0.1:8000)에 접속하여 결과를 확인할 수 있습니다.  