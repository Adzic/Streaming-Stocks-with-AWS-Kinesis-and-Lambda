
import boto3
import os
import subprocess
import sys
import json


subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')


import yfinance as yf

def lambda_handler(event, context):
    
    
    fh = boto3.client("firehose", "us-east-2")
    
    
    sdate = '2020-05-14'
    edate = '2020-05-15'
    granuality = '1m'
    stocks = ['fb', 'shop', 'bynd', 'nflx', 'pins', 'sq', 'ttd', 'okta', 'snap', 'ddog']
    
    
    for stock in range(len(stocks)):
        records = yf.download(stocks[stock], start = sdate, end = edate, interval = granuality)
        data = []
        
        
        for i in range(len(records)):
            output = {"High":records['High'][i],"Low":records['Low'][i],"Timestamp":records.index[i].strftime('%m/%d/%Y %X'),"Name":stocks[stock]}
            
            
            as_jsonstr = json.dumps(output)
    
            
            fh.put_record(
                DeliveryStreamName="finance-stream-tm", 
                Record = {'Data': as_jsonstr.encode('utf-8')})
            data.append(output)
            
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }