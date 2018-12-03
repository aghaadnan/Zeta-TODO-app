

var assert = require('assert');
var chai = require('chai');
 var expect = chai.expect;
var chaiHttp = require('chai-http');
var router = require('./router');
var server = require('./app');
var id;
var data={title:"I have to do some work",discription:"Work has to be done at 6 pm",done:true};
var modified={title:"this is modified title",discription:"this is modified discription",done:false}
chai.use(chaiHttp);

var router = server.use(router);

it("should post desired data",function(done){
  chai.request(router).post('/todo/api/v1.0/tasks').send(data).end(
    function(err,res){
      
      expect(res.body.sucess).to.be.true;
      
      done();
    }
  );
});

    it('it should GET all tasks', function (done)  {
      chai.request(router)
          .get('/todo/api/v1.0/tasks')
          .end( function(err, res) {
            
            expect(res.body.sucess).to.be.true;
                expect(res.body.result).to.be.an('array');
             var result=res.body.result;
             id=result[result.length-1].id;

done();
          });
        });

        it("should modify desired data",function(done){
          chai.request(router).put('/todo/api/v1.0/tasks/'+id).send(modified).end(
            function(err,res){
             
              expect(res.body.sucess).to.be.true;
              
              done();
            }
          );
        });

        it('it should GET a task', function (done)  {
          chai.request(router)
              .get('/todo/api/v1.0/tasks/'+id)
              .end( function(err, res) {
                
                expect(res.body.sucess).to.be.true;
                    
                 
    
    done();
              });
            });
            
            it('it should Delete a task', function (done)  {
              chai.request(router)
                  .del('/todo/api/v1.0/tasks/'+id)
                  .end( function(err, res) {
                    
                    expect(res.body.sucess).to.be.true;
                        
                     
        
        done();
                  });
                });

        

      



