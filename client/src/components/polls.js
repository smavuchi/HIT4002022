import React, { Component } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
    Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Form, FormGroup, Container, Label, InputGroup, InputGroupAddon, InputGroupText} from "reactstrap";
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Polls from '../artifacts/Polls.json'
import Votes from '../artifacts/Votes.json'
import Voters from '../artifacts/Voters.json'
import Modal from 'react-responsive-modal';
import { SSL_OP_NO_TLSv1_1 } from 'constants';
import {FaUserAlt, FaUsers, FaPhone, FaKey, FaUserLock, FaMailBulk} from 'react-icons/fa';

const drizzleOptions = {
    contracts: [
      Polls,
      Votes,
      Voters
    ]
}

class PastPolls extends Component{

    constructor(props) {
        super(props);
        this.state = { 
            polls: [],
            polls_count: localStorage.getItem('polls_count'),
            votes: [],
            votes_count: localStorage.getItem('votes_count'),
            voters: [],
            voters_count: localStorage.getItem('voters_count')
        };

        this.getPollsCount = () => {
            return<ContractData
                contract="Polls"
                method="getCount"
                render={data => (
                    <h5 style={{visibility: 'hidden'}}>{data}{localStorage.setItem('polls_count', data)}</h5>
                )}
            />
        };

        this.getVotesCount = () => {
            return<ContractData
                contract="Votes"
                method="getCount"
                render={data => (
                    <h5 style={{visibility: 'hidden'}}>{data}{localStorage.setItem('votes_count', data)}</h5>
                )}
            />
        };

        this.getVotersCount = () => {
            return<ContractData
                contract="Voters"
                method="getCount"
                render={data => (
                    <h5 style={{visibility: 'hidden'}}>{data}{localStorage.setItem('voters_count', data)}</h5>
                )}
            />
        };

        this.Vote = (poll_id) => {

            var voters_match = this.state.voters.filter(vot => vot.user_id == localStorage.getItem('decentralizedVoting'))
            if (voters_match.length > 0) {
                let port = (window.location.port ? ':' + window.location.port : '');
                window.location.href = '//' + window.location.hostname + port + '/vote/' + poll_id;
            }else{
                alert('You are not a registered voter. Please register to vote first.')
            }
        }
    };

    componentDidMount(){
        if(localStorage.getItem('decentralizedVoting')==null){
            let port = (window.location.port ? ':' + window.location.port : '');
            window.location.href = '//' + window.location.hostname + port + '/';
        };
    };

    render() {

        var pollsArray = [];
        var pollsCount = this.state.polls_count;
        for(var i=1; i<=pollsCount; i++){
          pollsArray[i-1] = i;
        };

        var polls = []
        const pollsMap = pollsArray.map((info, index) => {
            return<ContractData
                contract="Polls"
                method="polls"
                methodArgs={[info]}
                render={ data => {
                polls[info-1]={
                    id: data.id,
                    title: data.title,
                    date: data.date,
                    candidates: data.candidates
                };
                this.state['polls']=polls;
                return<div>
                </div>
                }}
            />
        });

        //

        var votesArray = [];
        var votesCount = this.state.votes_count;
        for(var i=1; i<=votesCount; i++){
          votesArray[i-1] = i;
        };

        var votes = []
        const votesMap = votesArray.map((info, index) => {
            return<ContractData
                contract="Votes"
                method="votes"
                methodArgs={[info]}
                render={ data => {
                votes[info-1]={
                    id: data.id,
                    poll_id: data.poll_id,
                    voter_id: data.voter_id,
                    candidate: data.candidate
                };
                this.state['votes']=votes;
                return<div>
                </div>
                }}
            />
        });

        //

        var votersArray = [];
        var votersCount = this.state.voters_count;
        for(var i=1; i<=votersCount; i++){
          votersArray[i-1] = i;
        };

        var voters = []
        const votersMap = votersArray.map((info, index) => {
            return<ContractData
                contract="Voters"
                method="voters"
                methodArgs={[info]}
                render={ data => {
                voters[info-1]={
                    id: data.id,
                    firstname: data.firstname,
                    lastname: data.lastname,
                    id_number: data.id_number,
                    phonenumber: data.phonenumber,
                    home_address: data.home_address,
                    image: data.image
                };
                this.state['voters']=voters;
                return<div>
                </div>
                }}
            />
        });

        var polls_with_current_user_votes = this.state.votes.filter(poll => poll.voter_id == localStorage.getItem('decentralizedVoting'))

        var polls_map = this.state.polls.map((item, index) => {

            if (polls_with_current_user_votes.filter(it => it.id == item.id).length > 0){
                var voted = true
            }else{
                var voted = false
            }

            var votes_for_current_poll = this.state.votes.filter(po => po.id == item.id)
            var number_of_votes = votes_for_current_poll.length

            var candidate_votes = {}
            votes_for_current_poll.map((vt, id) => {
                candidate_votes[vt.candidate] = votes_for_current_poll.filter(vte => vte.candidate == vt.candidate).length
            })
            var candidate_votes_string = ''
            for (const key in candidate_votes) {
                candidate_votes_string = candidate_votes_string + ', ' + key.toString() + ': ' + candidate_votes[key].toString()
            }

            return<div style={{borderRadius: '20px', border: '1px solid #1faced', margin: '5px'}}>
                <br/>
                <Row style={{textAlign: 'left'}}>
                    <Col style={{color: '#1faced'}}>
                        <Container>
                            Title:
                            <br/>
                            Date:
                            <br/>
                            Candidates:
                            <br/>
                            Number of votes:
                            <br/>
                            Candidates vote count:
                        </Container>
                    </Col>
                    <Col>
                        <Container>
                            {item.title}
                            <br/>
                            {item.date}
                            <br/>
                            {item.candidates}
                            <br/>
                            {number_of_votes} votes
                            <br/>
                            {candidate_votes_string}
                            <br/>
                            {
                                voted == true
                                ? <Button
                                    disabled={true}
                                    style={{backgroundColor: 'inherit', border: '1px solid #1faced', color: 'inherit'}}
                                >
                                    You've already voted on this poll
                                </Button>
                                : <Button
                                    onClick={() => this.Vote(item.id)}
                                    style={{backgroundColor: 'inherit', border: '1px solid #1faced', color: 'inherit'}}
                                >
                                    Place Vote
                                </Button>
                            }
                        </Container>
                    </Col>
                </Row>
                <br/>
            </div>
        })

        return(
            <Container>
                <br/>
                <h5 style={{borderBottom: '1px solid #1faced'}}>
                    Vote
                </h5>
                <br/><br/>
                {polls_map}
                <this.getPollsCount/>
                <this.getVotesCount/>
                <this.getVotersCount/>
            </Container>
        )
    }

};
export default  PastPolls;