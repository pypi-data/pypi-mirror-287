import boto3

class SES_SNS_Check:
    def verify_ses_identity(self,email, aws_access_key_id, aws_secret_access_key):
        ses_client = boto3.client('ses',region_name='us-east-1',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
        response = ses_client.list_identities(IdentityType='EmailAddress')
        identities = response['Identities']
        
        if email in identities:
            verification_attributes = ses_client.get_identity_verification_attributes(Identities=[email])
            status = verification_attributes['VerificationAttributes'].get(email, {}).get('VerificationStatus', 'Not Verified')
            if status == 'Success':
                return 'verified'
            else:
                return 'not_verfied'
        else:
            ses_client.verify_email_identity(EmailAddress=email)
            return 'added'
    
    def subscribe_to_sns(self,email,SNS_TOPIC_ARN,aws_access_key_id, aws_secret_access_key):
        sns_client = boto3.client('sns', region_name='us-east-1')
        response = sns_client.list_subscriptions_by_topic(TopicArn=SNS_TOPIC_ARN)
        subscriptions = response['Subscriptions']
        for subscription in subscriptions:
            if subscription['Endpoint'] == email:
                if subscription['SubscriptionArn'] != 'PendingConfirmation':
                    return "verified"
                else:
                    return"not_verfied"
        response = sns_client.subscribe(TopicArn=SNS_TOPIC_ARN,Protocol='email',Endpoint=email)
        return "added"
    def sns_check_subscribers(self,topics,aws_access_key_id, aws_secret_access_key):
        status_func= True
        try:
            sns_client = boto3.client('sns', region_name='us-east-1')
            topics_with_subscribers = []
            for topic in topics:
                subscribers_response = sns_client.list_subscriptions_by_topic(TopicArn=topic)
                subscribers = subscribers_response.get('Subscriptions', [])
                subscriber_details = []
                for sub in subscribers:
                    if "PendingConfirmation" not in sub['SubscriptionArn']:
                        status = 'Confirmed'
                    else:
                        status = 'Pending Confirmation'
                    subscriber_details.append({'Endpoint': sub['Endpoint'],'Status': status})
                topics_with_subscribers.append({'TopicName': topic.split(':')[-1],'Subscribers': subscriber_details})
                
        except Exception as e:
            print(f"An error occurred: {e}")
            status = False
            return topics_with_subscribers,status_func
        return topics_with_subscribers,status_func