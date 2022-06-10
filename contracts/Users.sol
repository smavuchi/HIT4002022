pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Users {
    uint public usersCount = 0;

    struct UsersData{
        uint id;
        string firstname;
        string lastname;
        string email;
        string password;
    }

    mapping(uint => UsersData) public users;
    UsersData[] public usersArray;

    function addUser(
        string memory _firstname, 
        string memory _lastname, 
        string memory _email,
        string memory _password
    ) public {
        usersCount ++;
        users[usersCount] = UsersData(
            usersCount, 
            _firstname, 
            _lastname, 
            _email, 
            _password
        );
    }

    function getCount() public view returns (uint) {
        return usersCount;
    }

    function allUsers() public returns (UsersData[] memory) {
        for(uint i = 0; i < usersCount; i ++){
            usersArray.push(users[i]);
        }
        return usersArray;
    }

}