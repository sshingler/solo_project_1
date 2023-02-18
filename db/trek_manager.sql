DROP TABLE IF EXISTS treks;
DROP TABLE IF EXISTS destinations; 

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    destination_name VARCHAR(255),
    country VARCHAR(255),
    continent VARCHAR(255)
); 

CREATE TABLE treks (
    id SERIAL PRIMARY KEY,
    trek_name VARCHAR(255),
    trek_distance FLOAT, 
    trek_days FLOAT,
    trek_headline VARCHAR(255),
    trek_completed BOOLEAN,
    trek_notes TEXT,
    destination_id INT NOT NULL REFERENCES destinations(id)
);

