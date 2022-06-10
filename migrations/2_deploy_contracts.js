const Polls = artifacts.require("Polls");
const Users = artifacts.require("Users");
const Voters = artifacts.require("Voters");
const Votes = artifacts.require("Votes");

module.exports = function(deployer) {
  deployer.deploy(Polls);
  deployer.deploy(Users);
  deployer.deploy(Voters);
  deployer.deploy(Votes);
};
