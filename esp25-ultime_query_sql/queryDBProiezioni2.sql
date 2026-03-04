CREATE TABLE FILM (idf TEXT, titolo TEXT, naz TEXT, genere TEXT, regista TEXT, durata INTEGER)

INSERT INTO FILM VALUES ("F4", "Natale a Rio", "Italia", "Comico", "Neri Parenti", 114)

SELECT f.titolo
FROM film f join proiezioni p on f.idf = p.film
WHERE f.naz = 'USA' and (f.genere = 'Thriller' or f.genere = 'Horror') and p.data = '15/05/2024'

SELECT f.titolo, cont(*)
FROM film f join proiezioni p on f.idf = p.film
GROUP BY f.idf 

SELECT c.nome, sum(f.durata)
FROM cinema c join proiezioni p on c.idc = p.cinema join film f on f.idf = p.film
GROUP BY c.idc
ORDER BY sum(f.durata) asc
