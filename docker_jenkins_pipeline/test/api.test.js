const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../src/server'); // Adjust the path to your server.js file
const expect = chai.expect;

chai.use(chaiHttp);

describe('API Tests', function() {
  it('should return Hello from Dockerized Node.js app!', function(done) {
    chai.request(app)
      .get('/')
      .end(function(err, res) {
        expect(res).to.have.status(200);
        expect(res.text).to.equal('Hello from Dockerized Node.js app!');
        done();
      });
  });

  it('should return Hello, API!', function(done) {
    chai.request(app)
      .get('/api')
      .end(function(err, res) {
        expect(res).to.have.status(200);
        expect(res.body).to.be.an('object');
        expect(res.body.message).to.equal('Hello, API!');
        done();
      });
  });
});

