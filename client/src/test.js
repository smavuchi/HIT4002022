import React, { Component } from 'react';
import './App.css';
import { BrowserRouter, Route, Switch, withRouter } from 'react-router-dom';
import Greeter from './artifacts/Greeter.json';
import Patient from './artifacts/Patient.json';
import { DrizzleProvider } from 'drizzle-react';
import { LoadingContainer, AccountData, ContractData, ContractForm } from 'drizzle-react-components';
import Navbar from './components/navbar';

const drizzleOptions = {
  contracts: [
    Greeter,
    Patient
  ]
}

class App extends Component {

  render() {
    return (
      <DrizzleProvider options={drizzleOptions}>
        <LoadingContainer>
          <div>
            <h5>Your account:</h5>
            <AccountData accountIndex={0} units={"ether"} precision={2} />
            <br/>
            <h5>Current greeting:</h5>
            <ContractData contract="Greeter" method="get" />
            <br/>
            <h5>Custom data</h5>
            <ContractData
            contract="Greeter"
            method="get"
            // toUtf8
            render={data => (
              <>
                Your greeting is: <b>{data}</b>
              </>
            )}
            />
            <br/>
            <h5>Set greeting:</h5>
            <ContractForm contract="Greeter" method="set" labels={['data1', 'data2']} />
            <br/>
            <h5>Patient data:</h5>
            {/* <ContractData contract="Patient" method="getPatientData" methodArgs={[1]}/> */}
            <br/>
            <h5>Register patient:</h5>
            <ContractForm contract="Patient" method="registerPatient" labels={['Firstname', 'Lastname', 'Identifier', 'Identifier Number', 'Sex', 'Birthdate', 'Current queue', 'Registration date']} />
            <br/>
            <h5>Customized Form</h5>
            <ContractForm
        contract="Patient"
        method="registerPatient"
        render={({ inputs, inputTypes, state, handleInputChange, handleSubmit }) => (
          <form onSubmit={handleSubmit}>
            {inputs.map((input, index) => (
              <div style={{padding: '2px'}}>
              <input
                style={{ fontSize: '15px', color: 'blue'}}
                key={input.name}
                type={inputTypes[index]}
                name={input.name}
                value={state[input.name]}
                placeholder={input.name}
                onChange={handleInputChange}
              />
              </div>

            ))}
            <button
              key="submit"
              type="button"
              onClick={handleSubmit}
              style={{ fontSize: '15px', color: 'white', backgroundColor: 'blue' }}
            >
              Register Patient
            </button>
          </form>
        )}
      />
                    <br/>
            <h5>Custom data</h5>
            <ContractData
        contract="Patient"
        method="patients"
        methodArgs={[1]}
        render={displayData => (
          <h5>Firstname {displayData.firstname}</h5>
        )}
      />
          </div>
        </LoadingContainer>

      </DrizzleProvider>
    );
  }
}

export default App;
