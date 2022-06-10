pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Voters {
    uint public votersCount = 0;

    struct VotersData{
        uint id;
        string firstname;
        string lastname;
        string id_number;
        string phonenumber;
        string home_address;
        string image;
        string user_id;
    }

    mapping(uint => VotersData) public voters;
    VotersData[] public votersArray;

    function addVoter(
        string memory _firstname, 
        string memory _lastname, 
        string memory _id_number,
        string memory _phonenumber,
        string memory _home_address,
        string memory _image,
        string memory _user_id
    ) public {
        votersCount ++;
        voters[votersCount] = VotersData(
            votersCount, 
            _firstname, 
            _lastname, 
            _id_number, 
            _phonenumber,
            _home_address,
            _image,
            _user_id
        );
    }

    function getCount() public view returns (uint) {
        return votersCount;
    }

    function allVoters() public returns (VotersData[] memory) {
        for(uint i = 0; i < votersCount; i ++){
            votersArray.push(voters[i]);
        }
        return votersArray;
    }

}