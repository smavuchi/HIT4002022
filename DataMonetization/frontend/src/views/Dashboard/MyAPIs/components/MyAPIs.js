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

// Custom components
import { AddIcon} from '@chakra-ui/icons'
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";
import APIsTableRow from "components/Tables/APIsTableRow";
import React from "react";
import NewAPIModal from "./NewAPIModal";

import axios from "axios";

import {api as apiUrl, frontend as frontendUrl} from "baseUrl";

const MyAPIs = ({ title, captions, data, fetchAPIs, select }) => {
  const fetch = fetchAPIs;

  const [newAPIModalIsOpen, setNewAPIModalIsOpen] = React.useState(false);
  const textColor = useColorModeValue("gray.700", "white");

  const [_delete, setDelete] = React.useState();
  const [deletionConfirmed, setDeletionConfirmed] = React.useState(false);

  const [deleting, setDeleting] = React.useState();
  const [deletingError, setDeletingError] = React.useState();
  const [publishing, setPublishing] = React.useState();

  const toast = useToast();

  const publishAPI = (apiId) => {
    setPublishing(true);

    axios.post(`${apiUrl}/client-api/${apiId}/publish`, {}).then(({data}) => {
      setPublishing(false);
      if (data.status != 200 && data.status != 201) {
        toast({
          title: 'API publication FAILED!',
          description: data.message,
          duration: 3000,
          status: "error",
          isClosable: true,
        })
        return;
      }
      else {
        toast({
          title: 'API published',
          description: "We've published that API for you.",
          duration: 3000,
          isClosable: true,
        })
        fetch();
      }
    }).catch(e => {
      toast({
        title: 'API publication FAILED!',
        description: "network problems, please retry",
        duration: 3000,
        status: "error",
        isClosable: true,
      })
      setPublishing(false);
    })
  };

  const deleteAPI = (apiId) => {
    setDeleting(true);
    setDeletingError();

    axios.delete(`${apiUrl}/client-api/${apiId}`).then(({data}) => {
      setDeleting(false);
      if (data.status != 200 && data.status != 201) {
        toast({
          title: 'API deletion FAILED!',
          description: data.message,
          duration: 3000,
          status: "error",
          isClosable: true,
        })
        return;
      }
      else {
        toast({
          title: 'API deleted',
          description: "We've deleted that API for you.",
          duration: 3000,
          isClosable: true,
        })
        fetchAPIs();
      }
    }).catch(e => {
      toast({
        title: 'API deletion FAILED!',
        description: "network problems, please retry",
        duration: 3000,
        status: "error",
        isClosable: true,
      })
      setDeleting(false);
    })
  }

  return (
    <>
    <NewAPIModal open={newAPIModalIsOpen} setOpen={setNewAPIModalIsOpen} onFinish={fetchAPIs}/>
    <Card overflowX={{ sm: "scroll", xl: "hidden" }}>
      <CardHeader p='6px 0px 22px 0px'>
        <Flex>
          <Text fontSize='xl' color={textColor} fontWeight='bold'>
            {title}
          </Text>
          <Spacer />
          <Text fontSize='xl' color={textColor} fontWeight='bold'>
            <Button 
              leftIcon={<AddIcon />}
              colorScheme='blue' 
              variant="outline"
              onClick={() => setNewAPIModalIsOpen(true)}
              size="sm"
            >Create New API</Button>
          </Text>
        </Flex>
      </CardHeader>
      <CardBody>
        <Table variant='simple' color={textColor}>
          <Thead>
            <Tr my='.8rem' pl='0px' color='gray.400'>
              {captions.map((caption, idx) => {
                return (
                  <Th color='gray.500' key={idx} ps={idx === 0 ? "0px" : null}>
                    {caption}
                  </Th>
                );
              })}
            </Tr>
          </Thead>
          <Tbody>
            {data.map((row, index) => {
              return (
                <APIsTableRow
                  select={select}
                  _delete={deleteAPI}
                  publish={publishAPI}
                  id={row.id}
                  key={index}
                  name={row.name}
                  title={row.title}
                  status={row.status}
                  date={row.created}
                />
              );
            })}
          </Tbody>
        </Table>
      </CardBody>
    </Card>
    </>
  );
};

export default MyAPIs;
