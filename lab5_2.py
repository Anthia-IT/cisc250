#Section 2: Classes

#Task 1

#1.1 Create a class called Product

class Product:
    '''This class represents a product'''

    #1.2 Create the constructor/initializer method

    def __init__(self, name, price, stock=0):
        '''Creates the product details'''

        self.name = name
        self.price = price
        self.stock = stock


    #1.3 Create a method called display_details()

    def display_details(self):
        '''Displays the product details'''

        print("\nProduct Details")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock}")


    #1.4 Create a method called update_stock

    def update_stock(self, quantity):
        '''Updates the stock amount'''

        if self.stock + quantity >= 0:

            self.stock = self.stock + quantity

            print(f"Stock was updated by {quantity}")

        else:

            print("Stock cannot go below zero.")



#Task 2

#2.1 Create a child class called DigitalProduct

class DigitalProduct(Product):
    '''This class represents a digital product'''

    #2.2 Create the constructor/initializer method

    def __init__(self, name, price, download_link):
        '''Creates the digital product details'''

        super().__init__(name, price, 9999)

        self.download_link = download_link


    #2.3 Override the display_details method

    def display_details(self):
        '''Displays the digital product details'''

        print("\nDigital Product Details")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Download Link: {self.download_link}")



#Task 3

#3.1 Create two objects

product1 = Product("Notebook", 5.99, 10)

digital_product1 = DigitalProduct("Python E-book", 15.99, "www.downloadpythonbook.com")


#3.3 Display the product details before stock updates

product1.display_details()


#3.2 Update the stock by a positive number

product1.update_stock(5)

#3.3 Display after update

product1.display_details()


#3.2 Update the stock by a negative number above zero

product1.update_stock(-3)

#3.3 Display after update

product1.display_details()


#3.2 Update the stock by a negative number below zero

product1.update_stock(-20)

#3.3 Display after update

product1.display_details()


#3.4 Display the digital product details

digital_product1.display_details() 