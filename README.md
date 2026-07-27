# SQL for Business Revenue Analysis

## 🔎 Overview
Contoso is a fictional global electronics retailer with stores across multiple countries, thousands of customers, and a catalog of products sold in different currencies. This project digs into ~100K rows of transactional data to answer the questions which are specified in below section.

Download the database here [Contoso_100k](https://github.com/lukebarousse/Int_SQL_Data_Analytics_Course/releases/download/v.0.0.0/contoso_100k.sql)

## 🛠️ Tools I Use
1️⃣ PostgreSQL ➜ Core programming language to query the database and answer the questions <br>
2️⃣ pgAdmin ➜ Act as PostgreSQL database <br>
3️⃣ Visual Studio Code ➜ Writing the README.md and integration with GitHub <br>
4️⃣ DBeaver ➜ Database admin tool which I mostly use to write the queries on <br>
5️⃣ GitHub ➜ Project's version control and host <br>
6️⃣ Python (Pandas) ➜ Create bar / chart / graph visualization <br>
7️⃣ Google Colab ➜ Environment to run Python in

## 💼 Business Questions
1️⃣ Who are the most valuable customers? <br>
2️⃣ How does each customer group generate revenue each year? Recent purchase or long-lasting purchase <br>
3️⃣ Who don't purchase recently? Why?

## 📊 Analysis Approach

### 1. Customer Segmentation
Group customers to 3 categories: High value (Above 75% percentile of total revenue), Mid value (Between 25% and 75% percentile), and low value (below 25% percentile)

**💻 Query**: [1_customer_segmentation.sql](/project_sql/1_customer_segmentation.sql)

**🖼️ Visualization**
|      Customer Value     | Customer Count | Total Lifetime Value ($) | Average Lifetime Value ($) |
| ----------------------- | -------------- | ------------------------ | -------------------------- |
| 1 - Low Value Customer  |      12372     |       4,341,809.53       |            350.94          |
| 2 - Mid Value Customer  |      24743     |       66,636,451.79      |            2693.14         |
| 3 - High Value Customer |      12372     |       135,429,277.27     |            10946.43        |

<img src="images/1_Percentage_CustomerSegmentation_by_TotalLTV.png"
width = 80%>

**🗝️ Key Findings**
- High-value segment (12372 customers ≈ 25% total customers) drives approximately 66% of the total revenue
- Mid-value segment (24743 customers ≈ 50% total customers) generates approximately 32% of the total revenue and holds the highest headcount
- Low-value segment (12372 customers ≈ 25% total customers) drives only 2% of the total revenue

**💡 Business Insights**
- High-Value Customers → **Revenue Engine** <br>
➢ A single customer contribute almost $11,000 to the total revenue, losing one customer prove to be a huge loss. <br>
➢ Prioritize retention over acquisition. <br>
➢ Provide premium perks only available to this segment (early access to new products/features).<br>
➢ Gather information about what makes this customer segment spend this massive cost to absorb more of these customers type

- Mid-Value Customers → **Highest Headcount** <br>
➢ Prioritize deepening relationship. <br>
➢ Provide tiered achievement or tiered benefits (e.g. spend $100 more to unlock reward X). <br>

- Low-Value Customers → **Minimum Contributor** <br>
➢ Keep this segment engaged only by using automated ads or automated engagement. It is best not to spend too much manual effort or personal touch or resource into this segment

### 2. 

**💻 Query**

**🖼️ Visualization**

**🗝️ Key Findings**

**💡 Business Insights**

### 3.

**💻 Query**

**🖼️ Visualization**

**🗝️ Key Findings**

**💡 Business Insights**