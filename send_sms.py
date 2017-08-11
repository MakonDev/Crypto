# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

def send_text_notification(text):
    
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC14f6a87d32523ceff0791befdba5ffb4", "c70b7810ed9cc6399714ca511118825d")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to="+16034893501",from_="+16037183064",body=text)
    
    return

#send_text_notification("Test")