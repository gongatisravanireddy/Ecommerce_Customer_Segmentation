import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load RFM Table
rfm = pd.read_csv("output/RFM_Table.csv")

# Features for clustering
X = rfm[["Recency", "Frequency", "Monetary"]]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

# Create Cluster column
rfm["Cluster"] = kmeans.fit_predict(X_scaled)

# Save clustered data
rfm.to_csv("output/Clustered_Customers.csv", index=False)

print("K-Means Clustering Completed Successfully!")
print("\nCluster Counts:")
print(rfm["Cluster"].value_counts())

print("\nFirst 10 Customers:")
print(rfm.head(10))