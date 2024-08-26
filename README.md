

# LaModa ATTIREVOGUE App

## Overview

The eShopping App is a web-based platform for online shopping, built with Python and Django. It provides features such as user management, product catalogs, shopping carts, and order processing. This README will guide you through the setup, usage, and contribution to the project. LaModa is a term derived from Spanish and Italian, where it directly translates to "The Fashion" in English. This Python-Django full-stack web development project showcases a sleek, responsive interface built with HTML and CSS, catering to a diverse audience. The platform offers a wide range of clothing, accessories, and fashion essentials for men, women, and kids, making it a one-stop shop for all fashion needs.

## Features

- User registration and login
- Product catalog with search and filter options
- Shopping cart management
- Checkout and payment processing
- Order history and tracking
- Admin dashboard for product and order management

## Prerequisites

- Python 3.x
- Django 4.x or later
- A database engine (e.g., SQLite, PostgreSQL)

##  Key Features:

1. User-Friendly Interface:

  - A clean, intuitive design ensures easy navigation, allowing users to browse categories and products effortlessly.

2. Diverse Product Range:

  - Men’s Collection:Includes a variety of clothing options like casual wear, formal attire, sportswear, and accessories such as belts, watches, and wallets.

  - Women’s Collection:Features a broad selection of dresses, tops, bottoms, ethnic wear, and accessories like handbags, jewelry, and scarves.

  - Kids’ Collection:Offers trendy and comfortable clothing for boys and girls, along with a range of accessories tailored for children.

  

3. Personalized Shopping Experience:

  - Registered users can create accounts to manage orders, save  items, and receive personalized recommendations.

  - Secure payment gateway integration ensures safe and convenient transactions.



4. Admin Panel:

  - The Django admin interface allows site administrators to manage products, categories, user accounts, and orders.



Technical Stack:

- Backend:Python with Django framework, ensuring robust and scalable architecture.

- Frontend:HTML, CSS, and JavaScript for a visually appealing and responsive user interface.

- Database:MySQL/dbSQLite for managing user data, product information, and orders.

 Target Audience:

- Men, Women, and Kids:Fashion enthusiasts looking for the latest trends and quality products.In LaModa | AttireVogue, the eCommerce website includes Frontend Pages:



1. login.html:

  - User authentication page for signing in with credentials.



2. register.html:

  - Page for new users to create an account with input fields for necessary information.



3. single_product.html:

  - Detailed view of a single product with images, descriptions, pricing, and purchase options.



4. product_filtered.html:

  - Displays products based on selected filters like category, price range, brand, etc.



5. cart.html:

  - Shows items added to the shopping cart, with options to update quantities or remove products.



6. checkout.html:

  - The final step in the purchase process, where users enter shipping details, choose payment methods, and review their order before finalizing.



7. payment.html:

  - Page for processing payment through various methods (credit card, PayPal, etc.).



8. contact.html:

  - A contact page with a form for users to submit inquiries or feedback, including company contact details.



9. our_products.html:

  - Possibly an overview page showing a list of products, such as a "Our Products" section, showcasing featured or all available products.



Backend Pages:



1. add_category.html:

  - Form for administrators to add new product categories to the site.



2. add_product.html:

  - Form for adding new products, including fields for product name, description, price, images, and category assignment.



3. display_category.html:

  - Displays a list of all categories, allowing administrators to view and manage them.



4. display_product.html:

  - Lists all products, with options to view, edit, or delete each product.



5. edit_category.html:

  - Allows administrators to edit the details of an existing product category.



6. edit_product.html:

  - Enables editing of existing product details, including updating descriptions, prices, and images.


## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/eshopping-app.git
   cd eshopping-app
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   The app will be available at `http://127.0.0.1:8000/`.

## Usage

- **Homepage**: View featured products and categories.
- **Product Pages**: Browse product details and add items to the cart.
- **Cart**: View and modify items in your cart.
- **Checkout**: Proceed with payment and complete your purchase.
- **Order History**: View past orders and their statuses.

## Admin Interface

- **Access**: Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.
- **Manage Products**: Add, update, or delete products.
- **Manage Orders**: View and process customer orders.

## Configuration

You can adjust settings in the `settings.py` file for database configurations, email settings, and other environment-specific parameters.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Create a pull request.



---
