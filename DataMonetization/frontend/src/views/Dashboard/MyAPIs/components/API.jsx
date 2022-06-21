import React from "react";
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
} from "@chakra-ui/react";

import {ChevronLeftIcon} from "@chakra-ui/icons"

import { AddIcon} from '@chakra-ui/icons'
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";
  
import APIStatistics from "./APIStatistics";
import TabView from "./TabView";

import useFetcher from "fetch";
import {api as apiUrl, frontend as frontendUrl} from "baseUrl";

import NewPackageModal from "./NewPackageModal";
import NewResourceModal from "./NewResourceModal";

export default function API({id, select}) {
  const [url, setUrl] = React.useState(`${apiUrl}/client-api/${id}`);
  const [itemToAdd, setItemToAdd] = React.useState();
  const [openModal, setOpenModal] = React.useState();

  const {data: api, loading, error, } = useFetcher({url});
  
  const textColor = useColorModeValue("gray.700", "white");

  const createNew = () => {
    setOpenModal(itemToAdd);
  }

  return (
    <>
    <NewPackageModal 
      open={openModal === "package"} 
      onClose={() => setOpenModal()} 
      onFinish={() => {}}
      apiId={id}
    />
    <NewResourceModal 
      open={openModal === "resource"} 
      onClose={() => setOpenModal()} 
      onFinish={() => {}}
      apiId={id}
    />
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
        <Flex>
          <Text fontSize='xl' color={textColor} fontWeight='bold'>
            {loading ? "Loading..." : (api && (api.title || api.name))}
          </Text>
          <Spacer />
          <Text fontSize='xl' color={textColor}>
            {itemToAdd && 
            <Button 
              leftIcon={<AddIcon />}
              colorScheme='blue' 
              variant="outline"
              onClick={createNew}
              size="sm"
            >
              Add API {
                itemToAdd === "package" ? "Package" :
                itemToAdd === "dataset" ? "Dataset" :
                "Resource"
              }
            </Button>}
          </Text>
        </Flex>
      </CardHeader>
      <CardBody>
        {loading ? "Loading..." : <TabView api={api} setItemToAdd={setItemToAdd}/>}
      </CardBody>
    </Card>
    </>
  );
}