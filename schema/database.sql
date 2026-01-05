CREATE DATABASE IF NOT EXISTS inventory_ops;
USE inventory_ops;

-- Products available for distribution
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL
);

-- Current inventory levels
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Delivery drivers
CREATE TABLE drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Delivery records
CREATE TABLE deliveries (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT NOT NULL,
    delivery_date DATE NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);

-- Items delivered per delivery
CREATE TABLE delivery_items (
    delivery_item_id INT AUTO_INCREMENT PRIMARY KEY,
    delivery_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (delivery_id) REFERENCES deliveries(delivery_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Driver-related expenses
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    expense_date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);
