CREATE TABLE IF NOT EXISTS characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    class VARCHAR(50),
    level INT,
    achievements INT
);

INSERT INTO characters (name, class, level, achievements) VALUES
('VeraShadow', 'Pandawa', 60, 200),
('FiraClaw', 'Huppermage', 50, 160),
('MokaBlaze', 'Eniripsa', 60, 150),
('XyloDust', 'Ecaflip', 55, 135),
('RikoGale', 'Xelor', 50, 120),
('RoboGale', 'Feca', 45, 110),
('LunaFang', 'Sacrieur', 38, 95),
('TikiShade', 'Iop', 40, 85),
('ZaraMoon', 'Roublard', 48, 80),
('VicoStorm', 'Cra', 30, 45),
('TikiClaw', 'Osamodas', 25, 30);
