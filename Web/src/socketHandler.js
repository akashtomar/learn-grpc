/**
 * code to handle all the socket events
 */
const myEmitter = require('./myEmitter');



module.exports = function(socket){
    myEmitter.on('someServerEvent', (msg)=>{
        console.log('inside emit on', msg); 
        socket.emit('otherEvent', msg);
    });
    
    socket.on('randomEvent', (msg)=>{
        myEmitter.emit('someServerEvent', msg);
        //console.log(msg);     
    });
    

}