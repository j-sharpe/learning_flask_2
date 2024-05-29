DROP TABLE IF EXISTS temps;

CREATE TABLE temps (
    celsius INT,
    fahrenheit INT,
    PRIMARY KEY(celsius, fahrenheit)
);