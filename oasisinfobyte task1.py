#🔷 PART 1 — Libraries Import

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
# Load the dataset 🔷 PART 2— Data Load & Clean

df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/datasets/retail_sales_dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

df.drop_duplicates(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Month_Name'] = df['Date'].dt.strftime('%b')

print("\nData Cleaned Successfully!")
#🔷 PART 3 — Descriptive Statistics
print("Basic Statistics:")
print(df.describe())

print("\nMean Total Amount:", df['Total Amount'].mean().round(2))
print("Median Total Amount:", df['Total Amount'].median())
print("Mode Total Amount:", df['Total Amount'].mode()[0])
print("Std Dev:", df['Total Amount'].std().round(2))

print("\nTotal Revenue:", df['Total Amount'].sum())

print("\nGender-wise Avg Spend:")
print(df.groupby('Gender')['Total Amount'].mean().round(2))

#🔷 PART 4 — Time Series Analysis
monthly = df.groupby(['Year','Month'])['Total Amount'].sum().reset_index()
monthly = monthly.sort_values(['Year','Month'])

print("Monthly Revenue:")
print(monthly)

plt.figure(figsize=(10,5))
plt.plot(monthly.index, monthly['Total Amount'], marker='o', color='steelblue')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_trend.png')
plt.show()

#🔷 PART 5 — Customer & Product Analysis
print("Revenue by Category:")
cat = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
print(cat)

plt.figure(figsize=(8,5))
cat.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('category_revenue.png')
plt.show()

print("\nGender Count:")
print(df['Gender'].value_counts())

plt.figure(figsize=(5,5))
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%',
colors=['#66b3ff','#ff9999'])
plt.title('Gender Distribution')
plt.tight_layout()
plt.savefig('gender_pie.png')
plt.show()

#🔷 PART 6 — Heatmap
pivot = df.pivot_table(index='Month_Name',
                       columns='Product Category',
                       values='Total Amount',
                       aggfunc='sum')

plt.figure(figsize=(10,6))
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Monthly Revenue Heatmap by Category')
plt.tight_layout()
plt.savefig('heatmap.png')
plt.show()

#🔷 PART 7 — Recommendations
best_cat = df.groupby('Product Category')['Total Amount'].sum().idxmax()
worst_cat = df.groupby('Product Category')['Total Amount'].sum().idxmin()

print("RECOMMENDATIONS:")
print(f"1. Best Category: {best_cat} - iska stock badao")
print(f"2. Worst Category: {worst_cat} - discount offer karo")
print("3. Peak month mein zyada marketing karo")
print("4. Top customers ko loyalty rewards do")
print("5. Low sales days mein flash sale karo")

