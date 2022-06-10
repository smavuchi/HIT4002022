import React, { Component } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
    Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Form, FormGroup, Container, Label, InputGroup, InputGroupAddon, InputGroupText} from "reactstrap";
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Users from '../artifacts/Users.json';
import Modal from 'react-responsive-modal';
import { SSL_OP_NO_TLSv1_1 } from 'constants';
import {FaUserAlt, FaUsers, FaPhone, FaKey, FaUserLock, FaMailBulk} from 'react-icons/fa';

const drizzleOptions = {
    contracts: [
      Users
    ]
}

class Signup extends Component{

    constructor(props) {
        super(props);
        this.state = { 
        
        };
    };

    componentDidMount(){
        if(localStorage.getItem('decentralizedVoting')!=null){
            let port = (window.location.port ? ':' + window.location.port : '');
            window.location.href = '//' + window.location.hostname + port + '/polls';
        };
    };

    render() {

        return(
            <Container>
                <br/><br/>
                <h5 style={{borderBottom: '1px solid #1faced'}}>Sign Up</h5>
                <ContractForm
                    contract="Users"
                    method="addUser"
                    render={({ inputs, inputTypes, state, handleInputChange, handleSubmit }) => (
                        <form onSubmit={handleSubmit}> <br/> <br/> <br/>
                            <Row>
                                <Col>
                                    <Label>Firstname</Label>
                                    <InputGroup>
                                    <InputGroupAddon addonType="prepend"><FaUserAlt style={{margin:'10px'}}/></InputGroupAddon>
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_firstname'
                                        type={inputTypes[0]}
                                        name='_firstname'
                                        value={state['_firstname']}
                                        placeholder='Enter Firstname Here'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                                <Col>
                                    <Label>Lastname</Label>
                                    <InputGroup>
                                    <InputGroupAddon addonType="prepend"><FaUsers style={{margin:'10px'}}/></InputGroupAddon>
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_lastname'
                                        type={inputTypes[1]}
                                        name='_lastname'
                                        value={state['_lastname']}
                                        placeholder='Enter Lastname Here'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                            </Row>
                            <Row>
                                <Col>
                                    <Label>Email</Label>
                                    <InputGroup>
                                    <InputGroupAddon addonType="prepend"><FaMailBulk style={{margin:'10px'}}/></InputGroupAddon>
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_email'
                                        type={inputTypes[4]}
                                        name='_email'
                                        value={state['_email']}
                                        placeholder='Enter Email Here'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                                <Col>
                                    <Label>Password</Label>
                                    <InputGroup>
                                    <InputGroupAddon addonType="prepend"><FaKey style={{margin:'10px'}}/></InputGroupAddon>
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_password'
                                        // type={inputTypes[3]}
                                        type='password'
                                        name='_password'
                                        value={state['_password']}
                                        placeholder='Enter Password Here'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                            </Row>
                            <br/><br/>
                            <Button
                                key="submit"
                                type="button"
                                onClick={handleSubmit}
                                style={{backgroundColor: 'inherit', border: '1px solid #1faced', color: 'inherit', marginBottom: '15px'}}
                            >
                                Signup
                            </Button>
                        </form>
                    )}
                />
            </Container>
        )
    }

};
export default  Signup;