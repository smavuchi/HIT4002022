// Chakra imports
import {
  Button,
  Box,
  Table,
  Tbody,
  Text,
  Th,
  Thead,
  Tr,
  Flex,
  Spacer,
  useColorModeValue,
  useToast,
  Input,
  InputGroup,
  InputLeftAddon,
  InputRightElement
} from "@chakra-ui/react";


import JsonFormatter from 'react-json-formatter'

import axios from "axios";
import React from "react";

import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";

import {api as apiUrl, frontend as frontendUrl} from "baseUrl";

export default function API({id, select, fetch}) {
  const [loading, setLoading] = React.useState(false);
  const [url, setUrl] = React.useState();
  const [response, setResponse] = React.useState();

  const textColor = useColorModeValue("gray.700", "white");
  const toast = useToast();

  const send = () => {
    setResponse();
    let completeUrl = "http://localhost:5000/api/v1/query/" + url
    setLoading(true);
    
    axios({
      url: completeUrl,
      headers: {
        "Accept": "application/json"
      },
    }).then(({data}) => {
      setLoading(false);
      setResponse(data);
    }).catch(e => {
      setLoading(false);
    })
  }

  const jsonStyle = {
    propertyStyle: { color: 'red' },
    stringStyle: { color: 'green' },
    numberStyle: { color: 'blue' }
  }

  React.useEffect(() => {
    console.log(response);
  }, [response]);

  return (
  	<>
  	<Card overflowX={{ sm: "scroll", xl: "hidden" }}>
      <CardHeader p='6px 0px 22px 0px'>
	    <Text fontSize='xl' color={textColor} fontWeight='normal' style={{ display: "inline", float: "left" }}>
	      Console
	    </Text>
      </CardHeader>
      <CardBody>
        <div style={{ width: "100%"}}>
          <div style={{ width: "100%", display: "block"}}>
            <Text>Url</Text>
            <InputGroup>
              <InputLeftAddon children='http://localhost:5000/api/v1/query/' />
              <Input
                placeholder="eg. metals-api/metal?limit=2"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
              />

              <InputRightElement width='4.5rem'>
                <Button h='1.75rem' size='sm' onClick={send} isLoading={loading}>
                  Send
                </Button>
              </InputRightElement>
            </InputGroup>
          </div>
          {response && <div style={{ width: "100%", display: "block", background: "#fff"}}>
            <br/>
            Response
            <div>
              {<JsonFormatter json={JSON.stringify(response)} tabWith='4' jsonStyle={jsonStyle}/>}
            </div>
          </div>
          }
        </div>
      </CardBody>
     </Card>
  	</>
  	)
}