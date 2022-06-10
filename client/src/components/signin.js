import React, { Component } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
    Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Form, FormGroup, Container, Label, InputGroup} from "reactstrap";
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Users from '../artifacts/Users.json';
import Modal from 'react-responsive-modal';
import { SSL_OP_NO_TLSv1_1 } from 'constants';
import Image from '../images/image_1.png'

const drizzleOptions = {
    contracts: [
      Users
    ]
}

class Signin extends Component{

    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '', 
            users_count: localStorage.getItem('users_count'),
            allUsers: []
        };

        this.HandleChange = (e) =>{
            this.setState({[e.target.name]: e.target.value});
        };

        this.getUsersCount = () => {
            return<ContractData
                contract="Users"
                method="getCount"
                render={data => (
                <h5 style={{visibility: 'hidden'}}>Total number of users is: {data}{localStorage.setItem('users_count', data)}</h5>
                )}
            />
        };

        this.Signin = (e) => {
            e.preventDefault()
            const email = this.state.email
            const password = this.state.password

            var allUsers = this.state.allUsers
            var user = allUsers.filter(user => user.email === email && user.password === password)

            console.log('user', user)
            if(user.length == 0){
                alert('Signin failed, please check your details and try again.')

            }else{
                localStorage.setItem('decentralizedVoting', user[0].id)
                alert('Signin successful.')
                let port = (window.location.port ? ':' + window.location.port : '');
                window.location.href = '//' + window.location.hostname + port + '/';

            }
        };
    };

    componentDidMount(){
        if(localStorage.getItem('decentralizedVoting')!=null){
            let port = (window.location.port ? ':' + window.location.port : '');
            window.location.href = '//' + window.location.hostname + port + '/polls';
        };
    };

    render() {
        var userIndexes = [];
        var userCount = this.state.users_count;
        for(var i=1; i<=userCount; i++){
        userIndexes[i] = i;
        };
        var allUsers = []
        var userData = userIndexes.map((user, index) => {
            return<ContractData
            contract="Users"
            method="users"
            methodArgs={[user]}
            render={data => {
                allUsers[user-1]={
                    id: user,
                    email: data.email,
                    password: data.password
                };
                this.state['allUsers']=allUsers;
                return<div>

                </div>
            }}
        />
        });
        return(
            <Container>
                <br/><br/>
                <Row>
                    <Col>
                        <img src={Image} style={{width: '100%', marginTop: '0px', marginRight: '20px'}}/>
                    </Col>
                    <Col>
                    <br/>
                    <Form onSubmit={this.Signin} >
                    <h4  style={{borderBottom: '1px solid #1faced'}}>Signin</h4> 
                        <br/><br/>
                        <Label for="email"><h6>Email</h6></Label>
                        <InputGroup>
                            <Input  style={{border: 'none', borderBottom: '1px solid #1faced'}} placeholder="Enter your email here" type="text" name="email" id="email" 
                                value={this.state.email} onChange={this.HandleChange} />
                        </InputGroup><br/> <br/> 
                        <Label for="password"><h6>Password</h6></Label>
                        <InputGroup>
                            <Input  style={{border: 'none', borderBottom: '1px solid #1faced', color: '#BFDCE7', backgroundColor: 'inherit'}} placeholder="Enter password here" type="password" name="password" id="password" 
                                value={this.state.password} onChange={this.HandleChange} />
                        </InputGroup><br/><br/>
                        <Button type="submit" style={{backgroundColor: 'inherit', color: 'inherit', border: '1px solid #1faced'}}>Signin</Button>{' '}
                        <Button color="secondary" href="/" style={{backgroundColor: 'inherit', color: 'inherit', border: '1px solid #1faced'}}>Cancel</Button>
                    </Form>
                    </Col>
                </Row>
                <this.getUsersCount/>
                <div style={{maxHeight: '5px'}}>
                    {userData}
                </div>
            </Container>
        )
    }

};
export default  Signin;