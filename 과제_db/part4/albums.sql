-- 앨범 목록 조회(순위 없이)
SELECT 앨범, 연도 FROM albums;

-- 2000년 발매 앨범 조회
SELECT * FROM aldums WHERE 연도 = '2000';

-- 최고 순위가 10위 이내 앨범 조회
SELECT * FROM albums WHERE 최고순위 <= 10;

-- 차트 순위 없는 앨범
SELECT * FROM albums WHERE 최고순위 = '-';

-- 연도 별 발매 앨범 개수
SELECT 연도, COUNT(*) FROM albums GROUP BY 연도;

-- 가장 최근 발매 앨범
SELECT * FROM albums ORDER BY 연도 DESC LIMIT 1;

-- 가장 오래된 앨범
SELECT * FROM albums ORDER BY 연도 ASC LIMIT 1;

-- 차트 10위 이상 앨범 조회
SELECT * FROM albums WHERE 최고순위 >= 10;

-- white 가 포함된 앨범 조회
SELECT * FROM albums WHERE 앨범 LIKE '%White%';

-- 2000년부터 2005년 사이 앨범 조회
SELECT * FROM albums WHERE 연도 BETWEEN '2000' AND '2005';

-- 연습 문제
-- 앨범 추가
INSERT INTO albums (앨범, 연도, 최고순위) VALUES ('New Album', '2024', '1');

-- 앨범 정보 업데이트
UPDATE albums SET 최고순위 = '2' WHERE 앨범 = 'New Album';

-- 수정 앨범 삭제
DELETE FROM albums WHERE 앨범 = 'New Album';