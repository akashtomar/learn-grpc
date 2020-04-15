/**
 * code to handle all the socket events
 */


module.exports = function(socket){
    socket.on('randomEvent', (msg)=>{
        console.log(msg);     
    });
    socket.emit('otherEvent', socket.id);

}