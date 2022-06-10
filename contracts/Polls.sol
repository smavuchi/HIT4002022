pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Polls {
    uint public pollsCount = 0;

    struct PollsData{
        uint id;
        string title;
        string date;
        string candidates;
    }

    mapping(uint => PollsData) public polls;
    PollsData[] public pollsArray;

    function addPoll(
        string memory _title, 
        string memory _date, 
        string memory _candidates
    ) public {
        pollsCount ++;
        polls[pollsCount] = PollsData(
            pollsCount, 
            _title, 
            _date, 
            _candidates
        );
    }

    function getCount() public view returns (uint) {
        return pollsCount;
    }

    function allPolls() public returns (PollsData[] memory) {
        for(uint i = 0; i < pollsCount; i ++){
            pollsArray.push(polls[i]);
        }
        return pollsArray;
    }

}