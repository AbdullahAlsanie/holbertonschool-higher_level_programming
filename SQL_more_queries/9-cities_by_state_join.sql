--  lists all cities contained in the database hbtn_0d_us
SELECT c.id, c.name, s.name FROM cities c, states s
WHERE c.state_id = s.id
GROUP BY c.id ASC;
