/**
 * code to handle all the socket events
 */
const myEmitter = require('./myEmitter');
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');
const PROTO_PATH = path.join(__dirname, '../proto/TaskMsg.proto');
const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

let createFile = grpc.loadPackageDefinition(packageDefinition).createfile;



module.exports = function(socket){
    /*myEmitter.on('someServerEvent', (msg)=>{
        console.log('inside emit on', msg); 
        
    });*/
    
    socket.on('createFile', (msg)=>{
        //myEmitter.emit('someServerEvent', msg);
        let client = new createFile.FileCreater('localhost:50051',
                                       grpc.credentials.createInsecure());

        client.CreateFile({fileName: "testFile", content: "test content"}, (err, response)=>{
            if(err){console.log(err);}
            else{console.log(response.message);
            socket.emit('ackFile', response.message);}
        });
        //console.log(msg);
    });
    

}