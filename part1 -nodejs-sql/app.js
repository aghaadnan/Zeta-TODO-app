var express =require('express');
var http =require('http');
var port=process.env.PORT||3050;
var app=express();

app.use(function(req,res,next){
    console.log(req.url);
    next();
});
app.use(function(req,res){
    res.send('Hello world');
    res.end();
});
 http.createServer(app).listen(port);