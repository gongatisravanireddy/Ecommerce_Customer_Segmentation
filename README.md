\# E-Commerce Customer Segmentation \& Sales Performance Dashboard



\## Project Overview



This project analyzes e-commerce sales data and customer purchasing behavior using \*\*Power BI\*\* and \*\*Python\*\*.



The project combines data cleaning, Revenue analysis, RFM analysis, customer segmentation using K-Means clustering, and an interactive Power BI dashboard to generate useful business insights.



\## Business Problem



E-commerce businesses generate large amounts of customer and sales data. It can be difficult to identify valuable customers, understand purchasing behavior, and determine which products and countries contribute most to sales.



This project aims to:



\- Analyze overall sales performance

\- Understand customer purchasing behavior

\- Segment customers based on their RFM values

\- Identify top-performing products and countries

\- Provide business insights for better decision-making



\## Dataset



The project uses the \*\*Online Retail Dataset\*\* containing e-commerce transaction information.



Important columns include:



\- InvoiceNo

\- StockCode

\- Description

\- Quantity

\- InvoiceDate

\- UnitPrice

\- CustomerID

\- Country



The original dataset contains transaction-level sales records.



\## Data Cleaning



Data cleaning was performed using \*\*Power BI / Power Query\*\*.



The cleaning process included:



\- Handling missing Customer IDs

\- Removing duplicate records

\- Removing invalid quantity values

\- Checking UnitPrice values

\- Correcting data types

\- Converting InvoiceDate into the required date format

\- Checking the consistency of transaction data



\## Revenue Calculation



Revenue was calculated in Power BI using:



\*\*Revenue = Quantity × UnitPrice\*\*



This calculated revenue was used for sales analysis and dashboard visualizations.



\## RFM Analysis



Customer behavior was analyzed using \*\*RFM Analysis\*\*.



\### Recency



Recency represents how recently a customer made a purchase.



\### Frequency



Frequency represents the number of purchases/orders made by a customer.



\### Monetary



Monetary represents the total amount spent by a customer.



The RFM table was created in Power BI and exported as:



`RFM\_Table.csv`



\## Customer Segmentation using K-Means



Customer segmentation was performed using \*\*Python\*\*.



The RFM values were used as input features:



\- Recency

\- Frequency

\- Monetary



The data was standardized using `StandardScaler`.



Then \*\*K-Means Clustering\*\* was applied with 4 clusters.



The clustered customer data was saved as:



`Clustered\_Customers.csv`



\### Python Technologies



\- Python

\- Pandas

\- Scikit-learn

\- StandardScaler

\- K-Means Clustering



\## Power BI Dashboard



The final interactive dashboard was developed using \*\*Microsoft Power BI\*\*.



\### Key Performance Indicators



The dashboard includes:



\- Total Revenue

\- Total Orders

\- Total Customers

\- Average Revenue



\### Dashboard Visualizations



The dashboard contains:



\- Monthly Sales Trend

\- Country-wise Sales

\- Top 10 Products

\- Customer Segmentation

\- Customer Cluster Analysis

\- Interactive Country Filter



\## Project Workflow



```text

Online Retail Dataset

&#x20;       ↓

Power BI / Power Query

Data Cleaning

&#x20;       ↓

Revenue Calculation

&#x20;       ↓

RFM Analysis

&#x20;       ↓

RFM Table

&#x20;       ↓

Python

StandardScaler + K-Means

&#x20;       ↓

Customer Clusters

&#x20;       ↓

Power BI Dashboard

&#x20;       ↓

Business Insights

