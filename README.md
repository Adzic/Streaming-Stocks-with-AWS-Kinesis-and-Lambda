# Streaming Stocks With AWS Kinesis&Lambda

This project is work on how to provision Lambda functions in order to capture real time or historical data. Our goal is to get financial data form yfinance and store it in s3 bucket. Creating these lambda functions allow us to keep collecting data from a source and store it for future queries and analysis. We will also use AWS Glue and AWS Athena. <br />

First, we will use data-collector lambda dunction and then kinesis firehose to transforme data that is downloaded and store it into s3. For final result that can be seen as result.scv we used SQL queries. Below are DataColletor Lambda configuration page and Kinesis Data Firehose Delivery stream monitoring.


![Image](https://github.com/Adzic/Streaming-Stocks-with-AWS-Kinesis-and-Lambda/blob/master/Stock%20Collector.png)
![Image](https://github.com/Adzic/Streaming-Stocks-with-AWS-Kinesis-and-Lambda/blob/master/Kinesis%20Stock%20Stream.png)
