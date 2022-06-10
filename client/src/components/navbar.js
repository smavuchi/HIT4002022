import React, { Component, useReducer } from 'react';
import {Collapse,Navbar,NavbarToggler,NavbarBrand,Nav,NavItem,NavLink,UncontrolledDropdown,
 Button, Input, Row, Col, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Form, Container, Label, InputGroup} from "reactstrap";
import Logo from '../images/logo.png';
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';

  class NavBar extends Component{

    constructor(props) { 
      super(props);
      this.toggle = this.toggle.bind(this);
      this.state = {
        dropdownOpen: false,
        userid: localStorage.getItem('decentralizedVoting')
      }; 

      this.dtoggle = () => {
        this.setState(prevState => ({
          dropdownOpen: !prevState.dropdownOpen
        }));
      }

      this.onMouseEnter = () => {
        this.setState({dropdownOpen: true});
      };
    
      this.onMouseLeave = () => {
        this.setState({dropdownOpen: false});
      };

      this.Signout = () => {
        localStorage.removeItem('decentralizedVoting');
        let port = (window.location.port ? ':' + window.location.port : '');
        window.location.href = '//' + window.location.hostname + port + '/';
      };

      this.validateSignIn = () => {
        var userid =  this.state.userid
        if(userid == null){
          return<Nav className="ml-auto" navbar>
            <NavItem>
            <NavLink></NavLink>
            </NavItem>
            <NavItem>
              <Button href={"/"} style={{backgroundColor: 'inherit', border: '1px solid #1faced', color: 'inherit'}}>Signin</Button>
            </NavItem>
            <NavItem>
            <NavLink></NavLink>
            </NavItem>
            <NavItem>
              <Button href="/signup" style={{backgroundColor: 'inherit', border: '1px solid #1faced', color: 'inherit'}}>Signup</Button>
            </NavItem>
          </Nav>
        }else{
          return<Nav className="ml-auto" navbar>
            <NavItem href={"/register-to-vote"} style={{marginRight: 20}}>
              Register To Vote
            </NavItem>
            <NavItem href={"/polls"} style={{marginRight: 20}}>
              Polls
            </NavItem>
            <NavItem href={"/new-poll"} style={{marginRight: 20}}>
              New Poll
            </NavItem>
            <NavItem>
              <ContractData
              contract="Users"
              method="users"
              methodArgs={[userid]}
              render={data => (
                <Dropdown className="d-inline-block" onMouseOver={this.onMouseEnter} onMouseLeave={this.onMouseLeave} isOpen={this.state.dropdownOpen} toggle={this.dtoggle}>
                <DropdownToggle  style={{backgroundColor:  'inherit', border: 'none'}}>
                  <span style={{fontSize: '10px', color: '#1faced'}}>You are signedin as <span style={{fontSize: '13px', fontWeight: 'bold', color: '#1faced'}}>{data.firstname} {data.lastname}</span></span>
                </DropdownToggle>
                <DropdownMenu>
                <DropdownItem  onClick={this.Signout}>
                  <NavLink style={{color: '#1faced'}} >
                     Signout
                  </NavLink>
                </DropdownItem>
                </DropdownMenu>
                </Dropdown>
              )}
            />
            </NavItem>
          </Nav>
        }
      }

    }

    componentDidMount() {

  }


    toggle() {
      this.setState({
        isOpen: !this.state.isOpen
      });
    }
    dtoggle() {
      this.setState(prevState => ({
        dropdownOpen: !prevState.dropdownOpen
      }));
    }
    onMouseEnter() {
      this.setState({dropdownOpen: true});
    }
  
    onMouseLeave() {
      this.setState({dropdownOpen: false});
    }

    render() {
      const { open } = this.state;
      return (
          <Navbar color="light" light expand="md"  style={{boxShadow: '0 8px 16px 0 grey', marginBottom: '10px'}}>
            <NavbarBrand href="/" style={{width: '20%'}}><img src={Logo} style={{width: '25%', float: 'left'}}/>
            <h5 style={{color: '#212529', paddingTop: '15px'}}>Decentralized Voting</h5>
          </NavbarBrand>
            <NavbarToggler onClick={this.toggle} />
            <Collapse isOpen={this.state.isOpen} navbar>
              <this.validateSignIn/>           
            </Collapse>
          </Navbar>
      );
    }

  };
  
  export default NavBar;