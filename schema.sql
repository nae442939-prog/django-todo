-- 데이터베이스 생성
CREATE DATABASE todo_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE todo_db;

-- Todo 테이블 생성 (todos.Todo 모델과 동일)
CREATE TABLE `todos_todo` (
    `id`           BIGINT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title`        VARCHAR(200) NOT NULL,
    `content`      LONGTEXT     NOT NULL,
    `is_completed` TINYINT(1)   NOT NULL DEFAULT 0,
    `created_at`   DATETIME(6)  NOT NULL
);
