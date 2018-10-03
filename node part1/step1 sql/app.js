var express =require('express');
var http =require('http');
var path =require('path');

var router = require('./router.js');
var parser =require('body-parser');
var port=process.env.PORT||3050;
var app=express();

app.use(function(req,res,next){
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    console.log(req.url);
    next();
});

app.use(express.static(path.resolve(__dirname)));
app.use(parser.urlencoded({extended:false}));
app.use(parser.json());
app.use(router);
app.use(function(req,res){
    res.status(404).send('No data found');
});
 http.createServer(app).listen(port);
 module.exports=app;