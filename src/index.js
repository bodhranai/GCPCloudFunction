const functions = require('@google-cloud/functions-framework');
const TWILIO_AUTH_TOKEN =  'TWILIO_AUTH_TOKEN';
const TWILIO_PHONE =  'TWILIO_PHONE';
const TWILIO_SID =  'TWILIO_SID';
const client  = require("twilio")(TWILIO_SID,TWILIO_AUTH_TOKEN);

functions.http('helloHttp', async (req, res) => {
    
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Allow-Headers', '*');
    res.set('Access-Control-Allow-Methods', 'GET,POST');
     res.status(200).send('OK');
    
 const recipient = req.query.recipient || req.body.recipient,
     body = req.query.body || req.body.body;
   const message = await client.messages.create({
     body,
     from: TWILIO_PHONE,
     to: recipient
   })
   res.send(`Sent message ${message.sid}!`);
  
  
});
