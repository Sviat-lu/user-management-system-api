CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    note VARCHAR(255)
);

COPY "user" (id, name, email, phone, note)
FROM '/docker-entrypoint-initdb.d/userdata.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('user_id_seq', (SELECT MAX(id) FROM "user"));
