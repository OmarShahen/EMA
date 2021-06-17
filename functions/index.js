const functions = require("firebase-functions");
const app = require('express')();
const mailer = require('nodemailer');
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));


app.get('/', (request, response)=>{

    return response.send("Is it working");
});

app.post('/ema-mail', (request, response)=>{
    
    const transporter = mailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'emawebsitemail908@gmail.com',
            pass: 'abdelhamed77'
        }
    });
    //mabdelhamed151@gmail.com, chairman@ema-egypt.com,
    const mailOptions = {
        from: 'emawebsitemail908@gmail.com',
        to: 'omarredaelsayedmohamed@gmail.com',
        subject: 'Message From The Site',
        html: `
        <strong>Visitor Name: </strong>${request.body.user_name}<br>
        <strong>Visitor Mail: </strong>${request.body.user_email}<br>
        <strong>Visitor Phone: </strong>${request.body.user_phone}<br>
        <strong>Visitor Message: </strong>${request.body.user_message}`
    }

    transporter.sendMail(mailOptions, (error, info)=>{
        if(error)
            console.log(error.message);
        else
            return response.send("تم ارسال الرسالة بنجاح");
    });
    
});





 exports.app = functions.https.onRequest(app);
