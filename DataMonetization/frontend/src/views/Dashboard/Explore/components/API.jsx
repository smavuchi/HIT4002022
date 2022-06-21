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
  useToast
} from "@chakra-ui/react";

import {ChevronLeftIcon} from "@chakra-ui/icons"

import axios from "axios";
import React from "react";

import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";

import useFetcher from "fetch";

import {api as apiUrl, frontend as frontendUrl} from "baseUrl";
import APIBody from "./APIBody";

export default function API({id, select, fetch}) {
  const [url, setUrl] = React.useState(`${apiUrl}/client-api/${id}`);
  const {data: api, loading, error} = useFetcher({url});
  
  const textColor = useColorModeValue("gray.700", "white");
  const toast = useToast();

  return (
  	<>
    <div style={{ paddingBottom: "10px" }}>
      <Button 
        size="sm"
        onClick={() => select()}
        leftIcon={<ChevronLeftIcon/>}
      >
        Back
      </Button>
    </div>
  	<Card overflowX={{ sm: "scroll", xl: "hidden" }}>
      <CardHeader p='6px 0px 22px 0px'>
	    <Text fontSize='xl' color={textColor} fontWeight='normal' style={{ display: "inline", float: "left" }}>
	      {api && (api.title || api.name)}
	    </Text>
	    {api && <Text style={{ display: "inline", float: "right" }} color="gray.500" size="sm">{api.owner_email}</Text>}
      </CardHeader>
      <CardBody>
      	{loading && "Loading ..."}
      	{(!loading) && (!api) && "No response"}
      	{api && <APIBody api={api}/>}
      </CardBody>
     </Card>
  	</>
  	)
}