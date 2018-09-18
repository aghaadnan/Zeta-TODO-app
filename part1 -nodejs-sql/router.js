var express= require('express');

var router = express.Router();

router.get('/todo/api/v1.0/tasks',function(req,res){
res.end("Request to tasks with get method arrives");
});
router.get('/todo/api/v1.0/tasks/:taskid',function(req,res){
    var id = req.params.taskid;
    res.end("Task for id: "+ id +" arrives ");
});
router.post('/todo/api/v1.0/tasks',function(req,res){
    res.end("Request to tasks with Post method arrives");
});
router.put('/todo/api/v1.0/tasks/:taskid',function(req,res){
res.end("request comes to update task of id : "+ req.params.taskid);
});
router.delete("/todo/api/v1.0/tasks/:taskid",function(req,res){
    res.end("Deleting id: "+ req.params.taskid);
});
module.exports=router;