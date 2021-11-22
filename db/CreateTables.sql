CREATE TABLE IF NOT EXISTS future
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          name VARCHAR(60) NOT NULL,
                          prize      VARCHAR(15) NOT NULL,
                          future     VARCHAR(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `future` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `future` VALUES (1,'George Barnacle','£65',"Will lose it investing on a 'Big Chungus' NFT");
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;