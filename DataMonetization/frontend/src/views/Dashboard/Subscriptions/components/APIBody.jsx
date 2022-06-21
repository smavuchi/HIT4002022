import React from "react";
import {
	Text,
	Box,
  	Badge,
  	Table,
  	Tr,
  	Th,
  	Td,
  	Tbody,
  	Thead,
  	Button,
  	useToast
} from "@chakra-ui/react";

import axios from "axios";

import useFetcher from "fetch";
import {api as apiUrl, frontend as frontendUrl} from "baseUrl";

export default function APIBody({api}) {
  const [url, setUrl] = React.useState(`${apiUrl}/client-api/${api.id}/packages`);
  const {data: packages, loading, error, fetch} = useFetcher({url});
  const [subscribing, setSubscribing] = React.useState(false);
  const toast = useToast();

  const subscribe = (packageId)  => {
    setSubscribing(true);
    axios.post(`${apiUrl}/client-api/${api.id}/packages/${packageId}/subscriptions`, {}).then(({data}) => {
      setSubscribing(false);
      if (data.status != 200 && data.status != 201) {
        toast({
          title: 'Subscription failed',
          description: data.message,
          duration: 3000,
          error: true,
          success: false,
          isClosable: true,
        })
        return;
      }
      else {
        toast({
          title: 'Subscription added',
          description: "We have added an API subscription to the given package",
          duration: 3000,
          isClosable: true,
        })
        fetch();
      }
    }).catch(e => {
      toast({
        title: 'Subscription failed',
        description: "network problems. Please retry",
        duration: 3000,
        error: true,
        success: false,
        isClosable: true,
      })
      setSubscribing(false);
    })
  }

  return (
  	<div style={{ width: "100%" }}>
  		<Text color="gray.400">{api.description || "No description provided"}</Text>
  		<Box style={{ marginTop: "30px" }}>
	  		<Text fontWeight="bold">
	  			Packages
	  		</Text>
  		</Box>
  		{
  			(!loading) && packages && packages.length === 0 &&
	  		<Box style={{ padding: "100px 0", display: "block", width: "100%", textAlign: "center"}}>
	  			{ <Text>No packages available</Text> }
	  		</Box>
  		}

  		{
  			loading &&
	  		<Box style={{ padding: "100px 0", display: "block", width: "100%", textAlign: "center"}}>
	  			{ <Text>Loading...</Text> }
	  		</Box>
  		}
  		<Box style={{ marginTop: "10px"}}>
  			<Table>
  			{(!loading) && packages && packages.length > 0 &&
  				<Thead>
  					<Tr>
  						<Th>Name</Th>
  						<Th>Description</Th>
  						<Th>Requests</Th>
  						<Th>Pricing</Th>
  						<Th>Your Status</Th>
  						<Th>Action</Th>
  					</Tr>
  				</Thead>}
  			{ (!loading) && packages && packages.map(p => (
  				<Tr>
  					<Td>{p.name}</Td>
  					<Td>{p.description}</Td>
  					<Td>{p.requests}</Td>
  					<Td>$ {p.pricing}</Td>
  					<Td>
				        <Badge
				          bg={p.subscribed ? "blue.400" : "gray.300"}
				          color={p.subscribed ? "#fff" : "#000"}
				          p="3px 10px"
				          borderRadius="8px"
				          size="sm"
				        >
				          {p.subscribed ? "subscribed" : "not subscribed"}
				        </Badge>
  					</Td>
  					<Td>
  						<Button size="sm" variant="outline" fontWeight="normal" disabled={p.subscribed} onClick={(e) => subscribe(p.id)}>
  							{p.subscribed ? "unsubscribe" : "subscribe"}
  						</Button>
  					</Td>
  				</Tr>
  				))}
  			</Table>
  		</Box>
  	</div>
    )
}