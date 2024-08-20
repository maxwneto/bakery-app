
# Bakery Inventory Management System

This project is a Bakery Inventory Management System built using Python. It is designed to manage products, categories, inventory levels, and sales for a bakery. The system follows the MVC (Model-View-Controller) architecture, ensuring a clear separation of concerns and facilitating maintainability.

## Features

- **Manage Products**: Add, update, and remove products in the inventory.
- **Category Management**: Manage product categories.
- **Inventory Tracking**: Track product quantities in the inventory.
- **Sales Management**: Record and track sales transactions.
- **File-based Persistence**: Data is stored in text files (`estoque.txt`, `categoria.txt`, `vendas.txt`), allowing for simple file-based storage.

## Project Structure

The project is organized into the following modules:

- **Model**: Defines the data structures and business logic.
- **View**: Handles the user interface (console-based in this case).
- **Controller**: Manages the logic to handle user input and updates the models.
- **DAO (Data Access Object)**: Handles data storage and retrieval from text files.

## Requirements

- Python 3.x

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/maxwneto/bakery-app.git
   cd bakery-app
   ```

2. Ensure that Python 3.x is installed on your system.

3. Run the program:

   ```bash
   python main.py
   ```

## Usage

### Adding a Product

To add a product to the inventory:

1. Run the program.
2. Select the option to add a new product.
3. Enter the product details including name, price, category, and quantity.

### Updating a Product

To update an existing product:

1. Run the program.
2. Select the option to update a product.
3. Enter the product's current name and provide the new details.

### Removing a Product

To remove a product from the inventory:

1. Run the program.
2. Select the option to remove a product.
3. Enter the name of the product you wish to remove.

### Managing Categories

You can add, update, and remove categories using similar steps to those for managing products.

### Recording a Sale

To record a sale:

1. Run the program.
2. Select the option to record a sale.
3. Enter the product name, quantity sold, and customer details.

## File Structure

- **`estoque.txt`**: Stores the product inventory with product details and quantities.
- **`categoria.txt`**: Stores the list of product categories.
- **`vendas.txt`**: Stores records of sales transactions.

## Example

### Adding Products to Inventory (estoque.txt)

```plaintext
Maçã|2.50|Frutas|10
Pão Francês|1.00|Padaria|50
Leite|3.50|Bebidas|20
```

### Adding Categories (categoria.txt)

```plaintext
Frutas
Padaria
Bebidas
Carnes
```

### Recording Sales (vendas.txt)

```plaintext
Maçã|2.50|Frutas|3|Joyce|Max|20/08/24
Leite|3.50|Bebidas|1|Joyce|Max|20/08/24
Pão Francês|1.00|Padaria|5|Joyce|Ana|20/08/24
```

## Contribution

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or feedback, please reach out to:

- Email: [maxwneto@gmail.com](mailto:maxwneto@gmail.com)
- GitHub: [maxwneto](https://github.com/maxwneto)
