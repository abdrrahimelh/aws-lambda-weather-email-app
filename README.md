# aws-lambda-weather-email-app
The first step is to configure your SES verify two emails one for sending and the other for receiving , if you are not in the sandbox one email is enough.
The second step is to create a lambda function (python >3.6)
Then navigate to your IAM > Policies > Create policy > paste the json and create the policy. Then navigate again to policies select the policy that you just created > Actions > Attach > Select your lambda function.
Go back to your lambda section and add a layer for our library ("dload") upload the python zip from the repository (select compatible runtimes python 3.6 and greater).
Go to your lambda function past the code and  don't forget to edit the city the sender and receiver and also the region.
Click on add layer above the code and add the layer that you've uploaded.
Test your function.
You can set a schedule trigger in CloudWatch so the function can be triggered in a time of the day .
