import React, { Component } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
    Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Form, FormGroup, Container, Label, InputGroup, InputGroupAddon, InputGroupText} from "reactstrap";
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Polls from '../artifacts/Polls.json';
import Modal from 'react-responsive-modal';
import { SSL_OP_NO_TLSv1_1 } from 'constants';
import {FaUserAlt, FaUsers, FaPhone, FaKey, FaUserLock, FaMailBulk} from 'react-icons/fa';

const drizzleOptions = {
    contracts: [
      Polls
    ]
}

class NewPoll extends Component{

    constructor(props) {
        super(props);
        this.state = { 
            
        };
    };

    componentDidMount(){
        if(localStorage.getItem('decentralizedVoting')==null){
            let port = (window.location.port ? ':' + window.location.port : '');
            window.location.href = '//' + window.location.hostname + port + '/';
        };
    };

    render() {

        return(
            <Container>
                <br/><br/>
                <h5 style={{borderBottom: '1px solid #1faced'}}>Create a new poll</h5>
                <ContractForm
                    contract="Polls"
                    method="addPoll"
                    render={({ inputs, inputTypes, state, handleInputChange, handleSubmit }) => (
                        <form onSubmit={handleSubmit}> <br/> <br/>
                            <Row>
                                <Col>
                                    <Label>Poll title</Label>
                                    <InputGroup>
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_title'
                                        type={inputTypes[0]}
                                        name='_title'
                                        value={state['_title']}
                                        placeholder='Enter Title Here'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                                <Col>
                                    <Label>Poll Date</Label>
                                    <InputGroup>
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_date'
                                        type={inputTypes[1]}
                                        name='_date'
                                        value={state['_date']}
                                        placeholder='Enter Date Here'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                            </Row>
                            <Row>
                                <Col>
                                    <Label>Names of Candidates</Label>
                                    <InputGroup>
                                    {/* <InputGroupAddon addonType="prepend"><FaUserLock style={{margin:'10px'}}/></InputGroupAddon> */}
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_candidates'
                                        type={inputTypes[2]}
                                        name='_candidates'
                                        value={state['_candidates']}
                                        placeholder='Seperate by commas e.g Candidate1, Candidate2 ...'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/>
                                </Col>
                            </Row>
                            <Button
                                key="submit"
                                type="button"
                                onClick={handleSubmit}
                                style={{backgroundColor: 'inherit', border: '1px solid #1faced', color: 'inherit', marginBottom: '15px'}}
                            >
                                Add Poll
                            </Button>
                        </form>
                    )}
                />
            </Container>
        )
    }

};
export default  NewPoll;