pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Votes {
    uint public votesCount = 0;

    struct VotesData{
        uint id;
        string poll_id;
        string voter_id;
        string candidate;
    }

    mapping(uint => VotesData) public votes;
    VotesData[] public votesArray;

    function addVote(
        string memory _poll_id,
        string memory _voter_id,
        string memory _candidate
    ) public {
        votesCount ++;
        votes[votesCount] = VotesData(
            votesCount, 
            _poll_id, 
            _voter_id,
            _candidate
        );
    }

    function getCount() public view returns (uint) {
        return votesCount;
    }

    function allVotes() public returns (VotesData[] memory) {
        for(uint i = 0; i < votesCount; i ++){
            votesArray.push(votes[i]);
        }
        return votesArray;
    }

}