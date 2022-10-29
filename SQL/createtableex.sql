Drop Table cardecision;

CREATE TABLE cardecision (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carid INT,
    buying varchar(255),
    maint varchar(255),
    doors varchar(255),
    persons varchar(255),
    lug_boot varchar(255),
    carsafety varchar(255),
    decision varchar(255)
); 

CREATE  UNIQUE INDEX carid ON cardecision(id);