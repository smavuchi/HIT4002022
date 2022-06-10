import React, { Component } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
    Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Form, FormGroup, Container, Label, InputGroup, InputGroupAddon, InputGroupText} from "reactstrap";
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Voters from '../artifacts/Voters.json';
import Votes from '../artifacts/Votes.json'
import Polls from '../artifacts/Polls.json'
import Modal from 'react-responsive-modal';
import { SSL_OP_NO_TLSv1_1 } from 'constants';
import {FaUserAlt, FaUsers, FaPhone, FaKey, FaUserLock, FaMailBulk} from 'react-icons/fa';

const drizzleOptions = {
    contracts: [
      Voters,
      Votes,
      Polls
    ]
}

class RegisterToVote extends Component{

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

        this.BackToPolls = () => {
            let port = (window.location.port ? ':' + window.location.port : '');
            window.location.href = '//' + window.location.hostname + port + '/polls';
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

        var current_poll = this.state.polls[this.props.match.params.poll_id]
        var candidates_as_string = current_poll.candidates
        var candidates_as_list = candidates_as_string.split(',')

        var candidates_map = candidates_as_list.map((item, index) => {
            return<div style={{borderRadius: '20px', border: '1px solid #1faced', margin: '5px'}}>
                <br/>
                <Row style={{textAlign: 'left'}}>
                    <Col style={{color: '#1faced', fontWeight: 'bold'}}>
                        <Container>
                            <br/>
                            Candidate Name:
                            <br/>
                        </Container>
                    </Col>
                    <Col>
                        <Container>
                            <br/>
                            {item}
                            <br/>
                            <ContractForm
                                contract="Votes"
                                method="addVote"
                                render={({ inputs, inputTypes, state, handleInputChange, handleSubmit }) => (
                                    <form onSubmit={handleSubmit}>
                                        <Input
                                            style={{visibility: 'hidden'}}
                                            key='_poll_id'
                                            type={inputTypes[0]}
                                            name='_poll_id'
                                            value={current_poll.id}
                                            onChange={handleInputChange}
                                        />
                                        <Input
                                            style={{visibility: 'hidden'}}
                                            key='_voter_id'
                                            type={inputTypes[1]}
                                            name='_voter_id'
                                            value={localStorage.getItem('decentralizedVoting')}
                                            onChange={handleInputChange}
                                        />
                                        <Input
                                            style={{visibility: 'hidden'}}
                                            key='_candidate'
                                            type={inputTypes[2]}
                                            name='_candidate'
                                            value={item}
                                            onChange={handleInputChange}
                                        />
                                        <Button
                                            key="submit"
                                            type="button"
                                            onClick={() => handleSubmit, this.BackToPolls()}
                                            style={{backgroundColor: 'inherit', border: '1px solid #1faced', borderRadius: '20px', marginTop: '-120px', color: 'inherit'}}
                                        >
                                            Vote for candidate
                                        </Button>
                                    </form>
                                )}
                            />
                            <br/>
                        </Container>
                    </Col>
                </Row>
                <br/>
            </div>
        })

        return(
            <Container>
                <br/><br/>
                <h5 style={{borderBottom: '1px solid #1faced'}}>
                    Vote on {current_poll.title}
                </h5>
                <br/><br/>
                <div style={{textAlign: 'left'}}>
                    <span style={{fontWeight: 'bold'}}>Candidates:</span> {candidates_as_string}
                </div>
                <br/>
                {candidates_map}
                <this.getPollsCount/>
                <this.getVotesCount/>
                <this.getVotersCount/>
            </Container>
        )
    }

};
export default  RegisterToVote;