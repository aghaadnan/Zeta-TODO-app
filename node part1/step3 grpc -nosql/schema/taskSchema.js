var mongoose = require('mongoose');
var taskschema=mongoose.Schema({
    title:String,
    discription:String,
    done:{type:Boolean,default:false}
},{
    versionKey:false
});
module.exports=mongoose.model("task",taskschema)