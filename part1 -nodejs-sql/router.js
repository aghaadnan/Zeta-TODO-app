var express= require('express');
var  Sequelize = require('sequelize');
var router = express.Router();

var db = new Sequelize("postgres://postgres:hanzala12@localhost:5432/Tasks");



var tasks=db.define("Tasks",{
    title:{type:Sequelize.STRING},
    discription:{type:Sequelize.STRING},
    done:{type:Sequelize.BOOLEAN,defaultValue:false}
});


tasks.sync();

router.get('/todo/api/v1.0/tasks',function(req,res){
    
tasks.findAll().then(function(result){
    if(result){
        
         res.status(200).send(result);
    }
    
});

});


router.get('/todo/api/v1.0/tasks/:taskid',function(req,res){
    var id = req.params.taskid;
    tasks.findById(id).then(function(result){
        
        if(result){
        res.status(200).send(result);}
        else{
            res.status(400).send("No data found");
        }
    });
});

//adding record of task in database
router.post('/todo/api/v1.0/tasks',function(req,res){
    var title=req.body.title;
    var discription= req.body.discription;
    
    tasks.create({title:title,discription:discription});
    res.send("Titile : "+ title +"    Description :"+ discription);
    res.end("Request to tasks with Post method arrives");
});

//updating tasks against id
router.put('/todo/api/v1.0/tasks/:taskid',function(req,res){
var id = req.params.taskid;
var title = req.body.title;
var discription= req.body.discription;
var done = req.body.done;
console.log(req.body.title);
tasks.findById(id).then(function(project){
    project.updateAttributes({
        title:title,
        discription:discription,
        done:done
    });
});


});

//deleting taks against given id
router.delete("/todo/api/v1.0/tasks/:taskid",function(req,res){
    console.log("Delete request arrives");
    var id = req.params.taskid;
    tasks.findById(id).then(function(project){
        if(project){
        project.destroy();
        res.status(200).send({sucess:true});
        }
        else{
            res.status(404).send({success:false});
        }
    })
});
module.exports=router;