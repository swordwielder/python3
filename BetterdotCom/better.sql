CREATE DATABASE IF NOT EXISTS betterment;

USE betterment;

-- CREATE TABLE IF NOT EXISTS companies (name varchar(32), country varchar(50), PRIMARY KEY(name));
--
-- CREATE TABLE IF NOT EXISTS trades (id INT, seller varchar(32), buyer varchar(32), value INT, PRIMARY KEY (id), FOREIGN KEY (seller) REFERENCES companies (name), FOREIGN KEY (buyer) REFERENCES companies (name));
--
-- INSERT INTO companies VALUES ('Alice s.p.', 'Wonderland');
-- INSERT INTO companies VALUES ('Y-zap', 'Wonderland');
-- INSERT INTO companies VALUES ('Absolute', 'Mathlands');
-- INSERT INTO companies VALUES ('Arcus t.g.', 'Mathlands');
-- INSERT INTO companies VALUES ('Lil Mermaid', 'Underwater Kingdom');
-- INSERT INTO companies VALUES ('None at all', 'Nothingland');
--
-- INSERT INTO trades VALUES (20121107, 'Lil Mermaid', 'Alice s.p.', 10);
-- INSERT INTO trades VALUES (20123112, 'Arcus t.g.', 'Y-zap', 30);
-- INSERT INTO trades VALUES (20120125, 'Alice s.p.', 'Arcus t.g.', 100);
-- INSERT INTO trades VALUES (20120216, 'Lil Mermaid', 'Absolute', 30);
-- INSERT INTO trades VALUES (20120217, 'Lil Mermaid', 'Absolute', 50);


SELECT nm.country,
       IFNULL(SUM(TdS.value),0) AS Export,
       IFNULL(SUM(TdB.value),0) AS Import
FROM companies nm
    LEFT JOIN trades TdS
        ON TdS.seller = nm.name
    LEFT JOIN trades TdB
        ON TdB.buyer = nm.name
GROUP BY nm.country;

select n.country as Country,
        SUM(IFNULL(t.value,0)) as Export,
        SUM(IFNULL(t1.value,0)) as Import
from companies n
    left join  trades t
        on n.name = t.seller
    left join  trades t1
        on n.name = t1.buyer
group by n.country;



-- SELECT a.country, export, import FROM (SELECT country, IFNULL(SUM(VALUE), 0) AS export
--                                        FROM companies LEFT JOIN trades ON name = seller GROUP BY country) AS a
--                                  LEFT JOIN
--                                       (SELECT country, IFNULL(SUM(VALUE), 0) AS import
--                                        FROM companies LEFT JOIN trades ON name = buyer GROUP BY country) AS b
--                                  ON a.country = b.country;
