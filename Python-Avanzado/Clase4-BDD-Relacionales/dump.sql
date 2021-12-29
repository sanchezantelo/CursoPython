BEGIN TRANSACTION;
CREATE TABLE alumnos(nombre TEXT, edad NUMERIC);
INSERT INTO "alumnos" VALUES('Carlos',30);
INSERT INTO "alumnos" VALUES('Jorge',50);
INSERT INTO "alumnos" VALUES('Oscar',42);
COMMIT;
