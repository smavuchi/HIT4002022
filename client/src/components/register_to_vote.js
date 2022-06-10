import React, { Component } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
    Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Form, FormGroup, Container, Label, InputGroup, InputGroupAddon, InputGroupText} from "reactstrap";
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Voters from '../artifacts/Voters.json';
import Modal from 'react-responsive-modal';
import { SSL_OP_NO_TLSv1_1 } from 'constants';
import {FaUserAlt, FaUsers, FaPhone, FaKey, FaUserLock, FaMailBulk} from 'react-icons/fa';
import axios from 'axios';
import {Backend_Url} from './backend_url'

const drizzleOptions = {
    contracts: [
      Voters
    ]
}

class RegisterToVote extends Component{

    constructor(props) {
        super(props);
        this.state = { 
            image: null,
            image_path: ''
        };

        this.UploadFile = (e) => {
          this.setState({image: e.target.files[0]})

            var data = new FormData() 
            data.append('image', e.target.files[0])
            
            axios.post(Backend_Url + 'saveImage', data)
            .then((res) => {
                let result = res.data
                this.setState({image_path: result})
                alert('Image saved successfully.')
            }).catch((error) => {
                alert('Something went wrong, check your connection and try uploading the image again.')
            })

        }
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
                <h5 style={{borderBottom: '1px solid #1faced'}}>Register To Vote</h5>
                <ContractForm
                    contract="Voters"
                    method="addVoter"
                    render={({ inputs, inputTypes, state, handleInputChange, handleSubmit }) => (
                        <form onSubmit={handleSubmit}> <br/> <br/>
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
                                    <Label>ID Number</Label>
                                    <InputGroup>
                                    {/* <InputGroupAddon addonType="prepend"><FaUserLock style={{margin:'10px'}}/></InputGroupAddon> */}
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_id_number'
                                        type={inputTypes[2]}
                                        name='_id_number'
                                        value={state['_id_number']}
                                        placeholder='National ID Number'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/>
                                </Col>
                                <Col>
                                    <Label>Phonenumber</Label>
                                    <InputGroup>
                                    {/* <InputGroupAddon addonType="prepend"><FaKey style={{margin:'10px'}}/></InputGroupAddon> */}
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_phonenumber'
                                        type={inputTypes[3]}
                                        name='_phonenumber'
                                        value={state['_phonenumber']}
                                        placeholder='Phonenumber'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                            </Row>
                            <Row>
                                <Col>
                                    <Label>Home address</Label>
                                    <InputGroup>
                                    {/* <InputGroupAddon addonType="prepend"><FaMailBulk style={{margin:'10px'}}/></InputGroupAddon> */}
                                    <Input
                                        style={{ marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_home_address'
                                        type={inputTypes[4]}
                                        name='_home_address'
                                        value={state['_home_address']}
                                        placeholder='Home Address'
                                        onChange={handleInputChange}
                                    />
                                    </InputGroup><br/> 
                                </Col>
                                <Col>
                                    <Label>Image Upload</Label>
                                    <InputGroup>
                                    {/* <InputGroupAddon addonType="prepend"><FaPhone style={{margin:'10px'}}/></InputGroupAddon> */}
                                    <Input
                                        style={{visibility: 'hidden', marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_image'
                                        type={inputTypes[5]}
                                        name='_image'
                                        value={this.state.image_path}
                                        onChange={handleInputChange}
                                    />
                                    <Input
                                        style={{visibility: 'hidden', marginBottom: '15px', border: 'none', borderBottom: '1px solid #1faced'}}
                                        key='_user_id'
                                        type={inputTypes[6]}
                                        name='_user_id'
                                        value={localStorage.getItem('decentralizedVoting')}
                                        onChange={handleInputChange}
                                    />
                                    <Input type='file' onChange={this.UploadFile}
                                    style={{border: 'none', marginTop: '-88px'}}/>
                                    </InputGroup><br/> 
                                </Col>
                            </Row>
                            <Button
                                key="submit"
                                type="button"
                                onClick={handleSubmit}
                                style={{backgroundColor: 'inherit', border: '1px solid #1faced', color: 'inherit', marginBottom: '15px'}}
                            >
                                Register To Vote
                            </Button>
                        </form>
                    )}
                />
            </Container>
        )
    }

};
export default  RegisterToVote;