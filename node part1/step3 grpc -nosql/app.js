

var express = require('express');
var mongoose = require('mongoose');
var grpc = require('grpc');
var  myTask= require('./schema/taskSchema');

var server = new grpc.Server();

mongoose.connect("mongodb://localhost:27017/task",function(err){
    if(!err) console.log("Database created");
    
});

var model = new myTask({title:"This is something",discription:"this is another thing",done:false});
//model.save();

var tasksProto = grpc.load('./proto/task.proto');

server.addService(tasksProto.TODOService.service,{
  tasks : function(call,callback){
    myTask.find().then(function(data){
        var tasks=[];
        data.forEach(function(task){
var  task = {id:task.id,done:false,title:task.title,discription:task.discription};
tasks.push(task);
        });
        
        callback(null,tasks);
    }) ; 
    
  },
  task :function(call,callback){
 var id = call.request.id;
 console.log(id);
 
 myTask.findById(id).then(function(task){
    
if(task){
var  mytask = {id:task.id,done:task.done,title:task.title,discription:task.discription};
    callback(null,mytask);}
    else 
    callback(new Error('Invalid id'),null);
 });
  },


  update: function(call,callback){
    var id = call.request.id;
    var title = call.request.title;
    var discription = call.request.discription;
    var done = call.request.done;
    if(!title||!discription){ 
      callback(new Error("Invalid title or/and discription"),{});
    return;
    }
      myTask.findById(id).then(function(result){
if(!result){
  callback(new Error("Invalid id"),{});
  return;
} 
result.title=title;
result.discription=discription;
result.done=done;
result.save();
      callback(null,{});
})
         
  },
  insert: function(call,callback){
    
    var title = call.request.title;
    var discription = call.request.discription;
    var done = call.request.done;
    if(!title||!discription){ 
      callback(new Error("Invalid title or/and discription"),{});
    return;
    }

    task = {title:title,discription:discription,done:done};
  new myTask(task).save();
  callback(null,{});
  },

  delete:function(call,callback){
    var id = call.request.id;
    myTask.findById(id).then(function(task){
      if(!task) {callback(new Error("Invalid id "),{});return;}
       task.remove();
       callback(null,{});
    });
  }

});

server.bind('0.0.0.0:50051',
  grpc.ServerCredentials.createInsecure());
  server.start();
