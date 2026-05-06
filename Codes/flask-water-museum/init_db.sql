-- 创建数据库
CREATE DATABASE IF NOT EXISTS jiangxi_water_culture
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE jiangxi_water_culture;

-- 创建水系数据表
CREATE TABLE IF NOT EXISTS water_systems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL COMMENT '水系名称',
    water_level FLOAT COMMENT '实时水位(米)',
    culture_intro TEXT COMMENT '富有温度的文化简介',
    image_path VARCHAR(200) COMMENT '本地图片路径'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入江西五大水系核心数据（每行均含名称、水位、文化简介、图片路径）
INSERT INTO water_systems (name, water_level, culture_intro, image_path) VALUES
('赣江', 15.63,
 '赣江，江西的母亲河，滔滔江水穿省而过，滋养了千年豫章文明，每一朵浪花都激荡着红色热土的记忆。',
 'images/ganjiang.jpg'),
('抚河', 12.81,
 '抚河，宛如一条碧带蜿蜒在赣东大地，它灌溉出临川才子之乡的文脉，低吟着汤显祖的戏曲余韵。',
 'images/fuhe.jpg'),
('信江', 18.24,
 '信江，自怀玉山奔腾而来，流经上饶这片红色故土，清澈的江水映照着方志敏烈士的赤诚初心。',
 'images/xinjiang.png'),
('饶河', 10.57,
 '饶河，汇聚昌江与乐安江之秀美，它是景德镇千年窑火的源泉，陶瓷文化随波流传。',
 'images/raohe.jpg'),
('修水', 14.02,
 '修水，漫江碧透，滋养了秋收起义的星火，每一滴水都承载着革命老区的坚韧与荣光。',
 'images/xiushui.jpeg');