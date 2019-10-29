CREATE DATABASE IF NOT EXISTS betterment;

USE betterment;

CREATE TABLE IF NOT EXISTS companies (name varchar(32), country varchar(50), PRIMARY KEY(name));

CREATE TABLE IF NOT EXISTS trades (id INT, seller varchar(32), buyer varchar(32), value INT, PRIMARY KEY (id), FOREIGN KEY (seller) REFERENCES companies (name), FOREIGN KEY (buyer) REFERENCES companies (name));

INSERT INTO companies VALUES ('Alice s.p.', 'Wonderland');
INSERT INTO companies VALUES ('Y-zap', 'Wonderland');
INSERT INTO companies VALUES ('Absolute', 'Mathlands');
INSERT INTO companies VALUES ('Arcus t.g.', 'Mathlands');
INSERT INTO companies VALUES ('Lil Mermaid', 'Underwater Kingdom');
INSERT INTO companies VALUES ('None at all', 'Nothingland');

INSERT INTO trades VALUES (20121107, 'Lil Mermaid', 'Alice s.p.', 10);
INSERT INTO trades VALUES (20123112, 'Arcus t.g.', 'Y-zap', 30);
INSERT INTO trades VALUES (20120125, 'Alice s.p.', 'Arcus t.g.', 100);
INSERT INTO trades VALUES (20120216, 'Lil Mermaid', 'Absolute', 30);
INSERT INTO trades VALUES (20120217, 'Lil Mermaid', 'Absolute', 50);


SELECT nm.country,
       ISNULL(SUM(TdS.value), 0) AS export,
       ISNULL(SUM(TdB.value),0) AS import
FROM dbo.Names nm
    LEFT JOIN dbo.Trades TdS
        ON TdS.seller = nm.name
        LEFT JOIN dbo.Trades TdB ON TdB.buyer = nm.name
GROUP BY nm.country;
