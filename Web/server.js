require('dotenv').config();
const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
app.set('view engine', 'ejs');
app.use(express.static('public'));

app.get('/', (req, res)=>{
    res.render('index');
});


io.on('connection', (socket) => {
    console.log(socket.id);
    console.log('a user connected');
    require('./src/socketHandler')(socket);
    socket.on('disconnect', ()=>{
        console.log('a user disconnected');
    });
});


http.listen(3000,()=>{
    console.log('lights @', 3000);
});

