--drop table member;
--drop table date_tap;
--drop table no_tap;
--drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
create table member(
no number(4),
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20),
mdate date
);

-- insert 데이터 입력, select 데이터 검색, update 데이터 수정, delete 데이터 삭제
insert into member values(
1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

insert into member values(
2,'bbb','1111','유관순','010-2222-2222','2024-09-20'
);


-- select 데이터 검색
select * from member;

commit;
rollback;

---- 삭제
--delete member where no2;
--delete member;

-- updqte 수정
update member set name='홍길자' where no=1;

update member set name='김구';

select * from member;

-- create 테이블 생성
create table students(
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

insert into students values(
1,'홍길동',100,100,100+100,sysdate
);

commit;

desc member;

SELECT * FROM MEMBER;
select * from member;
select memberno from member;
SELECT MEMBERNO FROM MEMBER;
SELECT memberNo from member;

-- 데이터 값이 대소문자를 구별함
select * from member;
SELECT * FROM MEMBER;
select * from member where id='aaa';
SELECT * FROM MEMBER WHERE ID='AAA';




update member set no='';
select * from member;
commit;
alter table member modify no varchar2(10);
select * from member;

desc member;

--drop table emp3;



select * from member2;
commit;




-- * 모든 컬럼 검색
select * from students;

-- 특정컬럼을 입력하면 컬럼만 검색
select name,sdate from students;

-- 특정컬럼만 입력하면 컬럼 입력
insert into students (stuno,name) values(
2,'유관순'
);

select * from students;

--
select * from employees;
select count(*) from employees;

-- 테이블 복사
create table emp2 as select * from employees;
select * from emp2;
select count(*) from emp2;  -- 데이터 개수

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
insert into member2 select * from member;

-- 테이블 컬럼
-- 컬럼데이터 타입, 길이 변경
-- alter는 변경 member 테이블 no 컬럼의 타입 길이를 변경
alter table member modify no number(10);
-- alter변경, 컬럼의 이름을 변경
alter table member rename column no to memberNo;


-- 테이블 구조
desc employees;

-- employees 테이블에서 사원번호, 사원 이름, 입사일만 출력
select employee_id,emp_name,hire_date from employees;




create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
select * from member;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

select * from students;

commit;

-- 연산자: 산술연산자, +,-,*,/
select kor,eng,(kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students;

select * from employees;

select concat(employee_id,emp_name) from employees;
select employee_id||emp_name from employees;

-- 달러 환산 1384
select salary from employees;
select salary*1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;

select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);


-- null 값 검색은 is null;
select * from stu where name is null;


select * from employees;
-- null이 아닌것 출력 : is not null
select commission_pct from employees where commission_pct is not null;

select salary from employees;
-- 연봉계산 * 12
select salary, salary*12 from employees;
select salary, salary*12, salary*12*1384 from employees;

-- 커미션이 없는 사원은 null 값이 있는데, null +,-,*,/을 하면 null 값으로 변경
select salary, salary*12, salary*12+(salary*12)*commission_pct*0.01 from employees;
-- 컬럼명 별칭 사용 as  ""은 특수문자, 사이 공간까지 있는 그대로 컬럼명으로 사용가능
select salary, salary*12 as "연 봉", salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as "r e a l _ y e a r Salary" from employees; 

-- nvl() 함수, nvl(kor,0) : kor컬럼에 null 값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;


select * from students;
-- 국영수합평 등수 입력일 컬럼명 별칭을 사용해서 출력.
select name as "이름", kor as "국어", eng as "영어", math as "수학", total as "합계", avg as "평균", rank as "등수", sdate as "등록일"
from students;
select * from students;


-- 사원번호, 이름, 이메일을 합쳐서 출력
select employee_id||emp_name||email from employees;
select concat(concat(employee_id,emp_name),email) from employees;
select emp_name||' is a '||job_id from employees;

-- 중복제거
select department_id from employees;
select distinct department_id from employees;
-- 정렬 : order by - asc(생략가능) : 순차정렬, desc : 역순정렬
select distinct department_id from employees order by department_id desc;

-- job_id 중복제거 출력하시오.
select distinct job_id from employees;
select job_id from employees;


--  문자열 자르기 substr(0,2) 0부터 2까지 출력
select substr(job_id,0,2) from employees;
-- 4번째 컬럼데이터를 가져와서 중복을 제거 함.
select distinct substr(job_id,4) from employees;




-- where절 : 조건비교연산자
select * from employees;

select * from employees where manager_id=124;
select * from employees where job_id = 'SH_CLERK';

select * from employees where employee_id >100;

-- students 테이블에서 합계가 250점 이상인 사람만 출력
select * from students;
select * from students where total >=250;

-- 합계가 250 이상이면서 kor 90점 이상인 사람들만 출력
select * from students where total >=250 and kor >=90;

-- 영어점수 70점 이상, 90점 이하 출력하시오.
select * from students where eng >=70 and eng <= 90;

-- employees에서 월급이 5000이상 7000 이하 검색
select * from employees where salary >= 5000 and salary <= 7000;

-- 7000이 아닌 것을 출력  !=, <>, ^=
select * from employees where salary != 7000;

-- department_id = 50번 개수 확인.
select count(*) from employees where department_id = 50;  --45개

-- 50번이 아닌거
select * from employees where department_id !=50;
select count(*) from employees where department_id != 50;    --106개

-- null 값은 count() 포함되지 않음.
select count(*) from employees where department_id is null; -- 1개

select count(employee_id) from employees;   -- 107개
select count(department_id) from employees;  --106개

-- 급여 4000이하 사원번호, 사원명, 급여 컬럼만 출력하시오.
select employee_id as "사원번호", emp_name as "사원명",salary as "급여" from employees where salary < 4000;

-- 숫자 비교연산자 가능, 날짜 비교연산자가 가능
select emp_name,hire_date from employees;
select emp_name,hire_date from employees where hire_date >= '2002/01/01';

-- 1999/12/31 이전에 입사한 사원 출력
select emp_name, hire_date from employees where hire_date <= '1999/12/31';

-- 2001/01/01 부터 2004/12/31/까지 출력
select emp_name, hire_date from employees where hire_date >= '2001/01/01' and hire_date <= '2004/12/31';


-- 논리연산자
-- 국어 점수가 90점 이상 또는 영어점수가 90점 이상을 출력하시오.
select count(*) from students where kor>=90 or eng>=90; --41개
select count(*) from students where kor>=90 and eng>=90; --3개
select count(*) from students where not kor>=90;

-- 부서번호 -80이면서  job-man
select * from employees;
select * from employees where department_id = 80 and substr(job_id,4)='MAN';
select * from employees where department_id = 80 and job_id ='SA_MAN';

-- 커미션이 0.2, 0.3, 0.5인 경우만 출력
select commission_pct from employees where commission_pct is not null;
select commission_pct from employees
where
commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;
-- in 연산자
select commission_pct from employees
where
commission_pct in (0.2,0.3,0.5);

-- 사원번호가 110,120,130만 출력
select * from employees where employee_id in (110,120,130);
select * from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;

-- 150-170 사원번호를 출력
select * from employees where employee_id > 150 and employee_id < 170; --151~169
-- between - and : <= 포함이 되어 있는 경우만 해당
select *from employees where employee_id between 150 and 170;   -- 150~170

-- 날짜 in
select hire_date from employees;
select hire_date from employees where hire_date in('2004/02/17','2002/06/07');
-- 날짜 between
select hire_date from employees
where hire_date between '2002/06/17' and '2004/12/31';

-- job MAN 출력하시오.
select * from employees where substr(job_id,4) = 'MAN';

-- LIKE연산자 : 포함되어 있는 글자 검색
select * from employees
where job_id = 'MAN';

select * from employees
where job_id like '%MAN';

select * from employees
where job_id like 'ST%';

-- EMP_NAME a가 들어가 있는 이름 출력
select * from employees
where emp_name like '%a%';

-- 2번째 자리에 t가 들어가 있는 이름을 출력.
select * from employees
where emp_name like '_t%';

-- 4번쨰가 v가 들어가 있는 이름 출력.
select * from employees
where emp_name like '___v%';

-- 뒤에서 2번째 자리에 l이 있는 이름을 출력.
select * from employees
where emp_name like '%l_';


-- 첫번쨰 D가 들어가 있는 이름을 출력하시오.
select * from employees
where emp_name like 'D%';

