import React, { Component } from 'react';
import './App.css';
import { BrowserRouter, Route, Switch, withRouter } from 'react-router-dom';
import Polls from './artifacts/Polls.json';
import Users from './artifacts/Users.json';
import Voters from './artifacts/Voters.json';
import Votes from './artifacts/Votes.json';
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Navbar from './components/navbar';
import Signup from './components/signup';
import Signin from './components/signin';
import RegisterToVote from './components/register_to_vote'
import NewPoll from './components/new_poll'
import Polls_ from './components/polls'
import Vote from './components/vote'
import VoterProfiles from './components/voter_profiles'

const drizzleOptions = {
  contracts: [
    Polls,
    Users,
    Voters,
    Votes
  ]
}

class App extends Component {

  render() {
    return (
      <DrizzleProvider options={drizzleOptions}>
        <LoadingContainer>
          <div className="App">
            <Navbar/>
            <BrowserRouter>
                <Switch>
                    <Route path='/' exact={true} component={Signin}/>
                    <Route path='/signup' exact={true} component={Signup}/>
                    <Route path='/register-to-vote' exact={true} component={RegisterToVote}/>
                    <Route path='/new-poll' exact={true} component={NewPoll}/>
                    <Route path='/polls' exact={true} component={Polls_}/>
                    <Route path='/vote/:poll_id' exact={true} component={Vote}/>
                    <Route path='/voter-profiles' exact={true} component={VoterProfiles}/>
                </Switch>
            </BrowserRouter>               
        </div>
        </LoadingContainer>
      </DrizzleProvider>
    );
  }
}

export default App;
