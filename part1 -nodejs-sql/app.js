var express =require('express');
var http =require('http');
var path =require('path');
var router = require('./router.js');
var parser =require('body-parser');
var port=process.env.PORT||3050;
var app=express();

app.use(function(req,res,next){
    console.log(req.url);
    next();
});
app.use(express.static(path.resolve(__dirname)));
app.use(parser.urlencoded({extended:false}));
app.use(router);
 http.createServer(app).listen(port);