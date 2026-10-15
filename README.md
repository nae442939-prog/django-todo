# Django Todo List

Django + MySQL로 만든 할 일 관리 웹 애플리케이션입니다.

## 기능
- 할 일 등록 / 목록 / 수정 / 삭제 (CRUD)
- 동그라미 버튼으로 완료 체크 (완료 항목은 취소선 + 회색 배경)
- 등록·수정 시 유효성 검사 (제목 필수, 2자 이상, 200자 이내) 및 에러 메시지 출력
- Admin 페이지에서 Todo 관리

## 모델 (todos.Todo)
| 필드 | 타입 | 설명 |
|---|---|---|
| title | CharField(200) | 할 일 제목 (필수) |
| content | TextField | 세부 내용 (선택) |
| is_completed | BooleanField | 완료 여부 (기본값 False) |
| created_at | DateTimeField | 생성 일시 (자동 입력) |

## 실행 방법
1. MySQL에 데이터베이스 생성
   ```sql
   CREATE DATABASE todo_db DEFAULT CHARACTER SET utf8mb4;
   ```
2. `.env.example`을 복사해 `.env` 파일을 만들고 `DB_USER` / `DB_PASSWORD`를 본인 MySQL 계정으로 입력 (`.env`는 GitHub에 올라가지 않음)
3. 패키지 설치 및 실행
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
4. http://127.0.0.1:8000/ 목록 페이지, http://127.0.0.1:8000/admin/ 관리자 페이지

## 테이블 생성 DDL
`schema.sql` 참고
