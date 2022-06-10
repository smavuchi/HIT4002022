import React, { Component } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
    Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Form, FormGroup, Container, Label, InputGroup, InputGroupAddon, InputGroupText} from "reactstrap";
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Voters from '../artifacts/Voters.json'
import Modal from 'react-responsive-modal';
import { SSL_OP_NO_TLSv1_1 } from 'constants';
import {FaUserAlt, FaUsers, FaPhone, FaKey, FaUserLock, FaMailBulk} from 'react-icons/fa';

const drizzleOptions = {
    contracts: [
      Voters
    ]
}

class VoterProfiles extends Component{

    constructor(props) {
        super(props);
        this.state = { 
            voters: [],
            voters_count: localStorage.getItem('voters_count')
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
    };

    componentDidMount(){
        if(localStorage.getItem('decentralizedVoting')==null){
            let port = (window.location.port ? ':' + window.location.port : '');
            window.location.href = '//' + window.location.hostname + port + '/';
        };
    };

    render() {

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

        var voters_map = this.state.voters.map((item, index) => {
            return<div style={{borderRadius: '20px', border: '1px solid #1faced', margin: '5px'}}>
                <br/>
                <Row style={{textAlign: 'left'}}>
                    <Col style={{color: '#1faced'}}>
                        <Container>
                            Firstname:
                            <br/>
                            Lastname:
                            <br/>
                            National ID Number:
                            <br/>
                            Phonenumber:
                            <br/>
                            Home Address:
                        </Container>
                    </Col>
                    <Col>
                        <Container>
                            {item.firstname}
                            <br/>
                            {item.lastname}
                            <br/>
                            {item.id_number}
                            <br/>
                            {item.phonenumber}
                            <br/>
                            {item._home_address}
                        </Container>
                    </Col>
                    <Col>
                        <Container>
                            <img src={item.image} style={{width: 'auto', maxWidth: '100%', height: 'auto', maxHeight: '200px', borderRadius: '20px'}} />
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
                    Voter Profiles
                </h5>
                <br/><br/>
                {voters_map}
                <this.getVotersCount/>
            </Container>
        )
    }

};
export default  VoterProfiles;