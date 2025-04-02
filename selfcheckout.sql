-- Use the correct schema
CREATE DATABASE IF NOT EXISTS selfcheckout;
USE selfcheckout;

-- Drop tables if they exist (in reverse dependency order)
DROP TABLE IF EXISTS discrepancies;
DROP TABLE IF EXISTS receipt_items;
DROP TABLE IF EXISTS detections;
DROP TABLE IF EXISTS transactions;

-- Recreate tables

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50) UNIQUE NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    image_path VARCHAR(255)
);

CREATE TABLE detections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50),
    label VARCHAR(100),
    confidence FLOAT,
    x_min INT,
    y_min INT,
    x_max INT,
    y_max INT,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
        ON DELETE CASCADE
);

CREATE TABLE receipt_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50),
    label VARCHAR(100),
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
        ON DELETE CASCADE
);

CREATE TABLE discrepancies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50),
    issue TEXT,
    resolved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
        ON DELETE CASCADE
);
