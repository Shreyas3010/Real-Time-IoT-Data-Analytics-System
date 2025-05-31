# Real-Time-IoT-Data-Analytics-System

Transform Your Phone into a Hub of Insights with IoT Sensor Tracking and Real-Time Data Streaming with AWS!

This repository provides a comprehensive guide and setup for streaming real-time data from IoT sensors, logging it using industry-standard practices, and analyzing the data using Parquet format. The setup includes components like an Android/iOS app for sending real-life and real-time data.

## AWS Services Used
Lambda, API Gateway,S3 , DyanmoDB, Glue Catalog, Athena, Kinesis Streams and Firehose
## Steps to follow
1. Sensor Logger Application
    i.Install Sensor Logger App in your Android/IOS
      Android-- https://play.google.com/store/apps/details?id=com.kelvin.sensorapp&hl=en_CA&gl=US \
      IOS-- https://apps.apple.com/us/app/sensor-logger/id1531582925 \
    ii. Follow the Steps in the photo given below\
      Step 1. Enable for Ambient Sensor for this particular project(feel free to customize)\
      Step 2. Go to Settings and Refer to the image below to enable HTTP push, and set the URL the one you will get while deploying the API\
     <img width="667" alt="Device_Setting" src="https://github.com/Shivam-Mishra1417/AWS-RealTime-data-analytics/assets/100092728/a4dd604f-5833-4438-ad46-1551e323ca0e">\
    iii. This Application will send the data in JSON format to API Gateway
      ```bash
      	{'light_illumination': 40.82624816894531, 'capture_time': 1712020418971037400}
      ```
2. Create a RestAPi using API Gateway\
  i. Create a REST API \
  ii. Create a resource named data, and enable cors and lambda integration. 
  iii. After creating deploy the API and save the URL in the app (refer to 1. Sensor Logger Application)

3. Create a lambda function with Python as the environment and upload the code.\ 
  i.Increase the default execution of lambda from 3sec to as per your needs (3-5 minutes). (Use Kafka in Ec2 instance for continuous delivery)\
  ii. Create an IAM ROLE to allow permissions to lambda to have full access to Kinesis Streams to write\
  iii. Deploy the Lambda\
  Refer - LamdaFunction

4. Kinesis Data Streams\
  i.Create a Stream with Provisioned Mode and Shard Capacity as 1 (you can change as per your needs but make sure you follow proper sharding in lambda function)

5. S3 Buckets\
  i.Create 2 Buckets for Parquet Format and JSON Format (Single Bucket with Different Prefix can also be used)

6. Glue Catalog\
  Determining the Structure of your data (JSON) is necessary, if you wish to add more parameters in JSON by enabling multiple sensors. Make changes accordingly to Lambda and Catalog
  i. Go to Athena\
  ii. Make a default database.\
  iii. Enter the Query (For this example I am only using an ambient light sensor)
    ```bash
    create external table default.tablename
    (light_illumination float,
    capture_time float)
    stored as parquet
    Location 's3://parquetbucketname/'
    TBLPROPERTIES ("parquet.compression"="SNAPPY")
    ```
7. Go to Firehose\
  i.Create a delivery stream\
  ii. Select source as Kinesis\
  iii. In source settings choose your kinesis stream which you have created\
  iv. Select Destination as S3 Bucket\
  v.Enable record format conversion and format as Parquet Apache\
  vi. Select the Glue Region where you created your glue and select the database and table\
  vii. Select destination as your s3 bucket and change the bucket size to 64MB as we are using parquet format is very lightweight, and the buffer interval to 60Sec\
  viii. Enable Backup Setting and select your backup JSON bucket\
  ix. Configure the backup bucket you created and set a prefix for your choice. (You can choose the same bucket as well)

## RoadBlock Faced and Solved
1. Lambda function working
2. Receiving data in Streams
3. Select the sensor according to your needs and make sure you have the correct JSON format and corresponding representation across lambda and data catalog query schema.

##Screenshot
Architecture Diagram : ![image](https://github.com/Shivam-Mishra1417/AWS-RealTime-data-analytics/assets/100092728/ece54d50-d05d-4927-a914-4fb82d23d270)
