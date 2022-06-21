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
import APIPackagesTableRow from "components/Tables/APIPackagesTableRow";
import React from "react";
// import NewAPIModal from "./NewAPIModal";

import useFetcher from "fetch";
import {api as apiUrl, frontend as frontendUrl} from "baseUrl";
import axios from "axios"
import ConfirmDialog from "components/ConfirmDialog";
import ViewPackageModal from "./ViewPackageModal";

export default function APIPackages({ apiId }){
  const toast = useToast()

  const [edit, setEdit] = React.useState();
  const [_delete, setDelete] = React.useState();
  const [deletionConfirmed, setDeletionConfirmed] = React.useState(false);
  const [url, setUrl] = React.useState(apiUrl + "/client-api/" + apiId + "/packages");
  
  const {data, loading, error, fetch} = useFetcher({url, repeatAfter: 3});
  const textColor = useColorModeValue("gray.700", "white");

  const [deleting, setDeleting] = React.useState();
  const [deletingError, setDeletingError] = React.useState();

  React.useEffect(() => {
    if (deletionConfirmed) {      
      setDeleting(true);
      setDeletingError();

      axios.delete(`${apiUrl}/client-api/${apiId}/packages/${deletionConfirmed}`).then(({data}) => {
        setDeleting(false);
        if (data.status != 200 && data.status != 201) {
          toast({
            title: 'API package deletion FAILED!',
            description: data.message,
            duration: 3000,
            status: "error",
            isClosable: true,
          })
          return;
        }
        else {
          toast({
            title: 'API package deleted',
            description: "We've deleted that API package for you.",
            duration: 3000,
            isClosable: true,
          })
          fetch();
        }
      }).catch(e => {
        toast({
          title: 'API package deletion FAILED!',
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
      {edit && <ViewPackageModal 
        open={edit !=  null} 
        onClose={() => setEdit()} 
        onFinish={fetch}
        apiId={apiId}
        packageId={edit}
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
          <Tr my='.8rem' pl='0px' color='gray.400'>
            {["Name", "Max no. of requests", "Pricing", "Created"].map((caption, idx) => {
              return (
                <Th color='gray.500' key={idx} ps={idx === 0 ? "0px" : null}>
                  {caption}
                </Th>
              );
            })}
          </Tr>
        </Thead>
        <Tbody>
          {data && data.map((row, index) => {
            return (
              <APIPackagesTableRow
                select={setEdit}
                _delete={setDelete}
                id={row.id}
                key={index}
                name={row.name}
                requests={row.requests}
                date={row.created_at}
                pricing={row.pricing}
              />
            );
          })}
        </Tbody>
      </Table>
      <Text style={{ padding: "100px 0"}} fontSize="sm" align="center">
        {data && data.length === 0 && "No packages. Add one by clicking on the 'add API package' button"}
      </Text>
    </>
  );
};
