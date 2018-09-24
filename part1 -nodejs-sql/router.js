var express= require('express');
var  Sequelize = require('sequelize');
var router = express.Router();

var db = new Sequelize("postgres://iwfykmna:c4k4f0PYKKFF8JRnTPBbdkGhH3dtY-R8@elmer.db.elephantsql.com:5432/iwfykmna");



var tasks=db.define("Tasks",{
    title:{type:Sequelize.STRING},
    discription:{type:Sequelize.STRING},
    done:{type:Sequelize.BOOLEAN,defaultValue:false}
});


tasks.sync();

router.get('/todo/api/v1.0/tasks',function(req,res){
    
tasks.findAll().then(function(result){
    if(result){
        
        res.status(200).send({sucess:true,result:result});
    }else{
        res.status(404).send({sucess:false,message:"No data found"});
    }
    
});

});


router.get('/todo/api/v1.0/tasks/:taskid',function(req,res){
    var id = req.params.taskid;
    tasks.findById(id).then(function(result){
        
        if(result){
        res.status(200).send({sucess:true,result:result});}
        else{
            res.status(404).send({sucess:false,message:"No data found"});
        }
    });
});

//adding record of task in database
router.post('/todo/api/v1.0/tasks',function(req,res){
    var title=req.body.title;
    var discription= req.body.discription;
    


  if(title && discription){
    tasks.create({title:title,discription:discription});
    res.status(200).send({sucess:true,message:'Successfully created'});
}
else if(!title){
    res.status(404).send({sucess:false,message:'Invalid title'});
}
else if(!discription){
    res.status(404).send({sucess:false,message:'Invalid discription'});
}

    
    
});

//updating tasks against id
router.put('/todo/api/v1.0/tasks/:taskid',function(req,res){
var id = req.params.taskid;
var title = req.body.title;
var discription= req.body.discription;

var done = req.body.done;

tasks.findById(id).then(function(project){
    if(project){


    if(title && discription){

    project.updateAttributes({
        title:title,
        discription:discription,
        done:done
});
          res.status(200).send({sucess:true,message:'Successfully updated'});
            
            }
        else if(!title)
         res.status(404).send({sucess:false,message:'Invalid title'});
         else if(!discription)  
         res.status(404).send({sucess:false,message:'Invalid DISCRIPTION'});


        }
   else{
                res.status(404).send({sucess:false,message:'Invalid id'});
            }
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
