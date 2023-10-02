CREATE TABLE company(
	company_id int not null auto_increment,
    name varchar(50) not null,
    description varchar(2000),
    primary key (company_id)
);

CREATE TABLE job(
	job_id int not null auto_increment,
    company_id int not null,
    tittle varchar(1000),
    info varchar(1000),
    date varchar(100),
    primary key (job_id)
);

/* ALTER TABLE job CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; */