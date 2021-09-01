import boto3
from botocore.exceptions import ClientError
import dload


def lambda_handler(event, context):
    # Replace SENDER and RECIEPIENT. If your account 
    # is still in the sandbox, this address must be verified.
    SENDER = sender email
    data= dload.json("https://api.openweathermap.org/data/2.5/weather?q="+your_city+"&units=metric&appid=10233baa27900bde1363821e57d39603")

    RECIPIENT = reciepient email
    temperature=data["main"]["feels_like"]
    description=data["weather"][0]["description"]
    icon=data["weather"][0]["icon"]

    
    # If necessary, replace eu-west-3 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "eu-west-3"
    
    # The subject line for the email.
    SUBJECT = "Today's weather in "+ your_city
    
    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("The temperature is "+str(temperature)+"\r\n"
                 "Today is "+description
                )
                
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Today is """ +description+"""</h1>
      <p>The temperature is """+str(temperature)+""" °C</p>
      <p style="text-align:center;">
      <img src="http://openweathermap.org/img/wn/"""+icon+"""@2x.png" alt="weather" width="100" height="100"</img>
      </p>
    </body>
    </html>
                """            
    
    # The character encoding for the email.
    CHARSET = "UTF-8"
    
    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)
    
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
       
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
