var express= require('express');
var  Sequelize = require('sequelize');
var router = express.Router();

var db = new Sequelize("postgres://postgres:hanzala12@localhost:5432/Tasks");



var tasks=db.define("Tasks",{
    title:{type:Sequelize.STRING},
    discription:{type:Sequelize.STRING}
});


tasks.sync();

router.get('/todo/api/v1.0/tasks',function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
tasks.findAll().then(function(result){
    if(result){
        
        result.forEach(function(data){
            res.write("Id : "+ data.id +" title : "+ data.title +" discription: "+data.discription+"<br>");
        });
    }
    res.end();
});

});


router.get('/todo/api/v1.0/tasks/:taskid',function(req,res){
    var id = req.params.taskid;
    tasks.findById(id).then(function(result){
        
        if(result){
        res.write("Id :"+ id);
        res .write("  title:"+ result.title);
        res .write("  discription:     "+ result.discription);
        res.end();}
        else{
            res.send("No data found");
        }
    });
});

router.post('/todo/api/v1.0/tasks',function(req,res){
    var title=req.body.object.title;
    var discription= req.body.discription;
    tasks.create({title:title,discription:discription});
    res.send("Titile : "+ title +"    Description :"+ discription);
    res.end("Request to tasks with Post method arrives");
});

router.put('/todo/api/v1.0/tasks/:taskid',function(req,res){

res.end("request comes to update task of id : "+ req.params.taskid);

});


router.delete("/todo/api/v1.0/tasks/:taskid",function(req,res){
    res.end("Deleting id: "+ req.params.taskid);
});
module.exports=router;