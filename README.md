# Django REST Framework Test Repository

이 레포지토리는 `Django REST Framework (DRF)`의 기능을 테스트하고, RESTful API를 개발 및 테스트하는 방법을 학습하기 위한 샘플 프로젝트입니다.

## 목차

- [프로젝트 개요](#프로젝트-개요)
- [기술 스택](#기술-스택)
- [설치 및 실행 방법](#설치-및-실행-방법)
- [API 엔드포인트](#api-엔드포인트)
- [테스트](#테스트)

## 프로젝트 개요

`Django`와 `Django REST Framework`를 사용하여 간단한 API 서버를 구축하고, 이를 통해 REST API 기능을 테스트합니다. 이 프로젝트는 `Django`를 처음 접하거나, REST API 서버 개발 및 테스트에 관심 있는 개발자를 대상으로 합니다.

## 기술 스택

- Python 3.x
- Django
- Django REST Framework
- SQLite (기본 데이터베이스)

## 설치 및 실행 방법

1. **프로젝트 클론**

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **가상 환경 생성 및 활성화**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows의 경우: venv\Scripts\activate
   ```

3. **필요 패키지 설치**

   ```bash
   pip install -r requirements.txt
   ```

4. **마이그레이션 수행**

   ```bash
   python manage.py migrate
   ```

5. **서버 실행**

   ```bash
   python manage.py runserver
   ```

6. **서버 확인**

   브라우저 또는 API 클라이언트를 통해 [http://127.0.0.1:8000](http://127.0.0.1:8000)으로 접근하여 API를 테스트합니다.

## API 엔드포인트

기본 엔드포인트에 대한 간단한 설명을 작성하세요. 예시는 다음과 같습니다:

- `GET /users/` - 전체 아이템 목록 조회
- `POST /users/` - 새 아이템 생성
- `GET /users/<id>/` - 특정 아이템 조회
- `PUT /users/<id>/` - 특정 아이템 업데이트
- `DELETE /users/<id>/` - 특정 아이템 삭제

각 엔드포인트에 대한 요청/응답 예시 및 설명을 추가할 수도 있습니다.

## 테스트

이 프로젝트에는 간단한 테스트가 포함되어 있습니다. 다음 명령을 통해 테스트를 실행할 수 있습니다:

```bash
python manage.py test
```

### 테스트 커버리지 확인 (선택 사항)

`coverage` 패키지를 설치한 경우, 커버리지를 확인할 수 있습니다.

```bash
pip install coverage
coverage run manage.py test
coverage report
```

## 기여

버그 제보, 개선 사항 제안 및 코드 기여를 환영합니다. 기여를 원하시면 새로운 브랜치를 생성하여 PR(Pull Request)을 생성해주세요.

---

이 문서가 프로젝트를 이해하고 사용하는 데 도움이 되길 바랍니다. 질문이 있는 경우 Issues 섹션에 남겨주세요.
