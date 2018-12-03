var chai  = require('chai');
var grpc = require('grpc');
var chai = require('chai');
var expect = chai.expect;
var tasksProto =  grpc.load('./proto/task.proto');
var client =new tasksProto.TODOService('0.0.0.0:50051', grpc.credentials.createInsecure());


it('should insert task',function(done){
    var task ={title:"Some task has to be done ",discription:"task to be performed at 6'o clock"};
 client.insert(task,function(err,result){
    expect(err).to.be.null;
    done();
 });
});
var id ;
it("should return all registered tasks",function(done){
    client.tasks({},function(err,result){
        
        expect(err).to.be.null;
      //  id = result[result.length-1].id;
        done();
 }
);
     
});

