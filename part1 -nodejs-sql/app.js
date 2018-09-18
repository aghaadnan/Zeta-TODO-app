var express =require('express');
var http =require('http');
var router = require('./router.js');
var port=process.env.PORT||3050;
var app=express();

app.use(function(req,res,next){
    console.log(req.url);
    next();
});
app.use(router);
 http.createServer(app).listen(port);