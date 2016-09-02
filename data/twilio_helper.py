import twilio
from twilio.rest import TwilioRestClient
import twilio_credentials

def send_alert(restaurant, phone_num):
    client = TwilioRestClient(
        twilio_credentials.ACCOUNT_SID, 
        twilio_credentials.AUTH_TOKEN)

    message_body = "Alert from PlateCheck: SF Dept of Public Health "\
                   "gave your favorite restaurant, {}, a poor rating "\
                   "at a recent health inspection. See platecheck.info "\
                   "for more information.".format(restaurant)

    message = client.messages.create(
        body=message_body,
        to=phone_num,
        from_="2012583467")
