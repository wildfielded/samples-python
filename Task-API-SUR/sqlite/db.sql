PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE 'Users'    (
                        'uid' VARCHAR(36) NOT NULL PRIMARY KEY,
                        'name' VARCHAR(1024) DEFAULT NULL,
                        'birth' VARCHAR(10) DEFAULT NULL,
                        'login' VARCHAR(1024) DEFAULT NULL,
                        'password' VARCHAR(1024) DEFAULT NULL,
                        'phone' VARCHAR(12) DEFAULT NULL,
                        'email' VARCHAR(1024) DEFAULT NULL,
                        'tg' VARCHAR(1024) DEFAULT NULL
                        );
INSERT INTO 'Users' VALUES('00000000-1111-1111-1111-000000000000','Грин','1994-08-22','greg','qawsedrf','+70123456789',NULL,NULL);
INSERT INTO 'Users' VALUES('00000000-2222-2222-2222-000000000000','Коха','1971-05-16','koky','!Q@W#E$R','+70987654321','kkk@gomail.intra','@teleg');
INSERT INTO 'Users' VALUES('00000000-3333-3333-3333-000000000000','Вано','1980-12-15','ivyn','AzSxDcFv','+74560789123','iv@mailgo.local',NULL);

CREATE TABLE 'Errors'   (
                        'code' INT(4) NOT NULL PRIMARY KEY,
                        'text' TEXT(1024) DEFAULT NULL
                        );
INSERT INTO 'Errors' VALUES(0,'OK');
INSERT INTO 'Errors' VALUES(100,'NAME field error');
INSERT INTO 'Errors' VALUES(200,'BIRTH field error');
INSERT INTO 'Errors' VALUES(210,'User must be adult');
INSERT INTO 'Errors' VALUES(300,'LOGIN field error');
INSERT INTO 'Errors' VALUES(400,'PASSWORD field error');
INSERT INTO 'Errors' VALUES(500,'PHONE field error');
INSERT INTO 'Errors' VALUES(600,'EMAIL field error');
INSERT INTO 'Errors' VALUES(700,'TG field error');
INSERT INTO 'Errors' VALUES(800,'Authentication error');
INSERT INTO 'Errors' VALUES(900,'User not registered');
COMMIT;
