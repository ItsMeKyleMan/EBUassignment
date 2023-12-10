import pandas as pd
import matplotlib.pyplot as plt

# Sample data representing Amazon product prices and ratings
amazon_products = {
    "Price": [50, 60, 70, 80, 90],
    "Rating": [3.5, 4.2, 3.8, 4.5, 3.9]
}

# Creating a Pandas DataFrame to hold the Amazon product data
amazon_df = pd.DataFrame(amazon_products)

# Extracting prices and ratings for plotting
product_prices = amazon_df['Price']
product_ratings = amazon_df['Rating']

# Creating a scatter plot to visualize the relationship between price and rating
plt.figure(figsize=(8, 6))
plt.scatter(product_prices, product_ratings, alpha=0.5)
plt.title('Relationship between Price and Rating of Amazon Products')
plt.xlabel('Price ($)')
plt.ylabel('Rating')
plt.grid(True)
plt.show()
