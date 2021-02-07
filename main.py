from twilio.rest import Client 
 
account_sid = 'ACe9c5be427f466b31033be9ab596d1978' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello Pyresearch',      
                              to='whatsapp:+92' 
                          ) 
 
print(message.sid)