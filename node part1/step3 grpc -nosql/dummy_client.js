var grpc = require('grpc');
var chai = require('chai');
var expect = chai.expect;
var tasksProto =  grpc.load('./proto/task.proto');
var client =new tasksProto.TODOService('0.0.0.0:50051', grpc.credentials.createInsecure());

    client.tasks({},function(err,result){
      console.log(result);
        
     });
 

 client.task({id:'5bb122c5ef63c206b060e5cb'},function(err,result){
     if(err) console.log("Get error"+err);
     else
    console.log("reuslt for :"+ result.title);
 });
 client.update({id:'5bb122c5ef63c206b060e5cb',title:"This is modified title",
discription:"this is 2nd modified discription"},function(err,result){
     if(err) console.log("Error for update "+ err);
     
 });

 var task ={title:"This is inserted title",discription:"this is inserted discription"};
 client.insert(task,function(err,result){
     if(err) console.log(err);
 });

 client.delete({id:'5bb122c5ef63c206b060e5cb'},function(err,result){
    if(err) console.log("Delete error"+ err);
});