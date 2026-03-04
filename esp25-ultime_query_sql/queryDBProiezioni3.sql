CREATE TABLE CINEMA (idc TEXT, nome TEXT, num_posti INTEGER, indirizzo TEXT)

INSERT INTO CINEMA VALUES ("C4", "Genga", 200, "v. delle albicocche 17 milano")

SELECT f.titolo
FROM film f join proiezioni p on f.idf = p.film
WHERE f.genere = 'Thriller' and (f.naz = 'USA' or f.naz = 'UK') and p.ora_inizio > 20:00

SELECT sum(c.num_posti)
FROM cinema c

SELECT cont(*)
FROM cinema c join proiezioni p on c.idc = p.cinema
WHERE p.data > '15/05/2024' and p.data < '22/05/2024'
GROUP BY c.idc

SELECT f.titolo, f.genere
FROM cinema c join proiezioni p on c.idc = p.cinema join film f on f.idf = p.film
WHERE c.nome = 'Cristallo' and f.regista like '%Tim%'

SELECT f.titolo
FROM film f join proiezioni p on f.idf = p.film
WHERE f.durata < 90
GROUP BY f.genere
ORDER BY f.titolo asc
