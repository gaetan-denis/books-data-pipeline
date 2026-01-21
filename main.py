import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("books.csv")

# Filter books published after 1950
books_post_1950 = df[df['year'] >= 1950]

# Display the filtered books
print(books_post_1950)

# Save filtered books to a new CSV
books_post_1950.to_csv("books_after_1950.csv", index=False)

# Create a simple bar chart
plt.figure(figsize=(8,5))
plt.bar(books_post_1950['title'], books_post_1950['year'], color='skyblue')
plt.xlabel("Book Title")
plt.ylabel("Publication Year")
plt.title("Books Published After 1950")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("books_after_1950.png")
plt.show()
