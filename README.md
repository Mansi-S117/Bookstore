# 📚 Bookstore

**Bookstore** is an e-commerce web application built with Django that allows users to browse, purchase, and manage books online. It includes secure payment integration using Stripe and supports email notifications for order confirmations and other actions.

---

## 🚀 Getting Started

Follow the steps below to set up the project on your local machine.

---


1. Take clone of the project 
    ``` bash
   git clone  https://github.com/Mansi-S117/Bookstore.git
    cd Bookstore
    ```
2. Create and activate virtual environment
   ```bash 
     python -m venv env
     .\env\Scripts\activate   #for windows
    source env/bin/activate   # for linux
   ```
3. Install the requirements
   ``` bash 
     pip install -r requirements.txt
   ```
4. Make a .env file and add the following credentials for email and stripe
   ``` bash
     EMAIL_HOST_USER 
     EMAIL_HOST_PASSWORD 
     DEFAULT_FROM_EMAIL
     STRIPE_PUBLIC_KEY 
     STRIPE_SECRET_KEY
   ```
5. Apply migrations
   ``` bash
     python manage.py migrate
   ```
6. Run the project
   ``` bash
     python manage.py runserver
   ```
   
**This is the landing page for bookstore**


![home page 1](https://github.com/user-attachments/assets/5df9dda6-e704-4c73-a3a7-a0192b984b21)

**The user can register themselves as buyer or seller roles**


![Register](https://github.com/user-attachments/assets/294f0c4d-8732-4179-a761-58606e25ba15)


**The books are displayed according to the categories**


![home page 2](https://github.com/user-attachments/assets/bb525833-dcaa-40c8-8ad5-afa22c2d9d1d)

**The buyer can add the books to the cart**


![cart](https://github.com/user-attachments/assets/1957aefe-50e5-4e89-ae5d-0a3c4972442c)


**For payment method we have integrated stripe**


![payment](https://github.com/user-attachments/assets/8aa66020-4267-44da-9533-35a59c42db8c)

**The buyer can also keep track of the orders they place**


![buyer dashboard](https://github.com/user-attachments/assets/c620faae-c31e-4857-8fe3-5874ea0ca07b)

**The seller can add one or more books from their dashboard**


![Add Book](https://github.com/user-attachments/assets/4d12684a-e47f-4d60-9149-3b8b49cc560d)


![seller books](https://github.com/user-attachments/assets/1bf74455-6de6-4cae-ad7b-495df1d61bae)

**The seller gets the information about the number of orders they recieved for their books**


![recieved orders](https://github.com/user-attachments/assets/2f495aaf-7e6f-47c3-a0af-8183c2e62bff)






