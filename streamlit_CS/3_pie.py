import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('streamlit_CS/data/pie_demo.csv')

# Extract data
labels = df['Category']
sizes = df['Value']

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Fruit Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
plt.tight_layout()
plt.show()
