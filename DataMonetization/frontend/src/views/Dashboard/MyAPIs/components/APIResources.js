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
import APIResourcesTableRow from "components/Tables/APIResourcesTableRow";
import React from "react";

import useFetcher from "fetch";
import {api as apiUrl, frontend as frontendUrl} from "baseUrl";
import axios from "axios"
import ConfirmDialog from "components/ConfirmDialog";
import ViewResourceModal from "./ViewResourceModal";
import ViewDatasetModal from "./APIDatasetModal";

export default function APIResources({ apiId }){
  const toast = useToast()

  const [openDataset, setOpenDataset] = React.useState();
  const [edit, setEdit] = React.useState();
  const [_delete, setDelete] = React.useState();
  const [deletionConfirmed, setDeletionConfirmed] = React.useState(false);
  const [url, setUrl] = React.useState(apiUrl + "/client-api/" + apiId + "/resources");
  
  const {data, loading, error, fetch} = useFetcher({url, repeatAfter: 3});
  const textColor = useColorModeValue("gray.700", "white");

  const [deleting, setDeleting] = React.useState();
  const [deletingError, setDeletingError] = React.useState();
  const [publishing, setPublishing] = React.useState();

  const publish = (resourceId) => {
    setPublishing(true);

    axios.post(`${apiUrl}/client-api/${apiId}/resources/${resourceId}/publish`, {}).then(({data}) => {
      setPublishing(false);
      if (data.status != 200 && data.status != 201) {
        toast({
          title: 'API resource publication FAILED!',
          description: data.message,
          duration: 3000,
          status: "error",
          isClosable: true,
        })
        return;
      }
      else {
        toast({
          title: 'API resource published',
          description: "We've published that API resource for you.",
          duration: 3000,
          isClosable: true,
        })
        fetch();
      }
    }).catch(e => {
      toast({
        title: 'API resource publication FAILED!',
        description: "network problems, please retry",
        duration: 3000,
        status: "error",
        isClosable: true,
      })
      setPublishing(false);
    })
  };

  React.useEffect(() => {
    if (deletionConfirmed) {      
      setDeleting(true);
      setDeletingError();

      axios.delete(`${apiUrl}/client-api/${apiId}/resources/${deletionConfirmed}`).then(({data}) => {
        setDeleting(false);
        if (data.status != 200 && data.status != 201) {
          toast({
            title: 'API resource deletion FAILED!',
            description: data.message,
            duration: 3000,
            status: "error",
            isClosable: true,
          })
          return;
        }
        else {
          toast({
            title: 'API resource deleted',
            description: "We've deleted that API resource for you.",
            duration: 3000,
            isClosable: true,
          })
          fetch();
        }
      }).catch(e => {
        console.log(e)
        toast({
          title: 'API resource deletion FAILED!',
          description: "network problems, please retry",
          duration: 3000,
          status: "error",
          isClosable: true,
        })
        setDeleting(false);
      })

      setDeletionConfirmed(false);
    }
  }, [deletionConfirmed])

  return (
    <>
      {edit && <ViewResourceModal 
        open={edit !=  null} 
        onClose={() => setEdit()} 
        onFinish={fetch}
        apiId={apiId}
        resourceId={edit}
      />}
      {openDataset && <ViewDatasetModal 
        open={true} 
        onClose={() => setOpenDataset()} 
        onFinish={() => {}}
        apiId={apiId}
        resourceId={openDataset}
      />}
      <ConfirmDialog 
        title="Confirm deletion"
        text="Are you sure?"
        isOpen={_delete}
        deletion
        onClose={(answer) => {
          setDeletionConfirmed(answer ? _delete : false);
          setDelete()
        }}
      />
      {deleting && <Text style={{ color: "red" }}>deleting...</Text> }
      <Table variant='simple' color={textColor}>
        <Thead>
          <Tr my='.8rem' color='gray.400' textAlign="left" >
            {["Name", "Url Name", "Actions", "Status", "Created"].map((caption, idx) => {
              return (
                <Th color='gray.500' key={idx} ps={idx === 0 ? "0px" : null} textAlign="left">
                  {caption}
                </Th>
              );
            })}
          </Tr>
        </Thead>
        <Tbody>
          {data && data.map((row, index) => {
            return (
              <APIResourcesTableRow
                select={setEdit}
                _delete={setDelete}
                setOpenDataset={setOpenDataset}
                publish={publish}
                id={row.id}
                key={index}
                name={row.name}
                urlName={row.url_name}
                actions={row.actions}
                status={row.published ? "Published" : "Not published"}
                date={row.created_at}
                pricing={row.pricing}
              />
            );
          })}
        </Tbody>
      </Table>
      <Text style={{ padding: "100px 0"}} fontSize="sm" align="center">
        {data && data.length === 0 && "No resources. Add one by clicking on the 'add API resource' button"}
      </Text>
    </>
  );
};
