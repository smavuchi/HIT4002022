import React from "react";
import { Button, useToast } from "@chakra-ui/react";
import axios from "axios";
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,

  Input,
  Box,
} from '@chakra-ui/react'

import {frontend, api} from "baseUrl";

export default function Preview({dataset, resourceId, apiId}) {
  const [offset, setOffset] = React.useState(0);
  const [limit, setLimit] = React.useState(4);
  const [data, setData] = React.useState([]);
  const [loading, setLoading] = React.useState(false);

  const toast = useToast();

  const fetch = () => {
  	setLoading(true);
    axios.get(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/data` + `?limit=${limit}&offset=${offset}`).then(({data}) => {
      setLoading(false);
      if (data.status != 200 && data.status != 201) {
        toast({
          title: 'API dataset not fetched',
          description: data.message,
          duration: 3000,
          error: true,
          success: false,
          isClosable: true,
        })
        return;
      }
      else {
        setData(JSON.parse(data.data));
      }
    }).catch(e => {
      toast({
        title: 'Error fetching API dataset data',
        description: "network problems. Please retry",
        duration: 3000,
        error: true,
        success: false,
        isClosable: true,
      })
      setLoading(false);
    })
  }

  React.useEffect(() => {
  	fetch();
  }, []);

  return (
    <>
    <Box> 
    From
      <Input
        type="number"
        width="100px"
        style={{
        	margin: "0 10px"
        }}
        onChange={(e) => setOffset(e.target.value)}
        value={offset}
      />
    Get records
      <Input
        type="number"
        width="100px"
        style={{
        	margin: "0 10px"
        }}
        onChange={(e) => setLimit(e.target.value)}
        value={limit}
      />
      <Button onClick={fetch} style={{ float: "right"}} colorScheme="blue">
      	Fetch
      </Button>
    </Box>
    <Box style={{ marginTop: "40px"}}>
      <Table>
      	<Thead>
      	<Tr>
      	  {Object.keys(dataset.column_types).map(item => (
      	  	<Th>{item}</Th>
      		))
      	  }
      	</Tr>
      	</Thead>
      	{(!loading) && 
	      	<Tbody>
	      	{
	      	  data.map((item, i) => (
	      	  	<Tr key={i}>
	      	  	 {
	      	  	 	Object.keys(dataset.column_types).map((column, index) => (
	      	  	 		<Td key={index}>{item[column]}</Td>
	      	  	 	))
	      	  	 }
	      	  	</Tr>
	      	  ))
	      	}
	      	</Tbody>
      	}
      </Table>
    </Box>
    {(loading || data.length === 0) && <Box style={{ textAlign: "center", padding: "100px 0"}}>
	    {
	    	loading && "Loading..."
	    }
	  	{
	  		(data.length === 0 && (!loading)) && "No records found"
	  	}
	    </Box>
	}
    </>
    )
}