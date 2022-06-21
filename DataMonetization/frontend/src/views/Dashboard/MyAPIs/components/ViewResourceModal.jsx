import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Button,
  Input,
  Text,
  FormControl,
  FormLabel,
  FormErrorMessage,
  FormHelperText,
  Textarea,
  Spacer,
  InputGroup,
  InputLeftAddon
} from '@chakra-ui/react'

import React from "react";
import axios from "axios";
import { useToast } from '@chakra-ui/react'

import {frontend, api} from "baseUrl";
import useFetcher from "fetch";

export default function ViewAPIResourceModal({open, setOpen, onFinish, apiId, resourceId, ...props}) {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState();
  
  const [name, setName] = React.useState();
  const [urlName, setUrlName] = React.useState();
  const [description, setDescription] = React.useState();

  const [url, setUrl] = React.useState(`${api}/client-api/${apiId}/resources/${resourceId}`);
  const {data: apiResource, loading: resourceLoading, error: errorLoadingResource, response} = useFetcher({url});

  const toast = useToast()

  const onClose = () => {
    props.onClose();
  }

  const onUpdate = () => {
    setLoading(true);
    setError();

    axios.post(`${api}/client-api/${apiId}/resources/${resourceId}/update`, { name, urlName, description }).then(({data}) => {
      setLoading(false);
      if (data.status != 200 && data.status != 201) {
        setError(data.message);
        return;
      }
      else {
        onFinish();
        toast({
          title: 'API resource updated',
          description: "We've updated your API resource for you.",
          duration: 3000,
          isClosable: true,
        })
        onClose();
      }
    }).catch(e => {
      setLoading(false);
      setError("network problems. Please retry")
    })
  }

  React.useEffect(() => {
    if (!apiResource) {
      return;
    }
    setName(apiResource.name);
    setUrlName(apiResource.url_name);
    setDescription(apiResource.description);
  }, [apiResource])

  return (
    <>
      <Modal onClose={onClose} isOpen={open} isCentered>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>View API Resource</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {error && <><Text style={{ color: "red"}}>{error}</Text><br/></>}

            <FormControl isRequired>
              <FormLabel htmlFor='api-resource-name'>Name</FormLabel>
              <Input 
                id='api-resource-name' 
                type='text' 
                placeholder="eg. metals" 
                value={name} 
                onChange={(e) => setName(e.target.value)}/>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-resource-url-name'>Url Name</FormLabel>
              <Input 
                id='api-resource-url-name' 
                type='text' 
                placeholder="" 
                value={urlName} 
                onChange={(e) => setUrlName(e.target.value)}/>
              <FormHelperText>A url-friendly name that is short and precise</FormHelperText>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-resource-description'>Description</FormLabel>
               <Textarea
                id="api-resource-description"
                placeholder='Enter description text...'
                size='sm'
                value={description} 
                onChange={(e) => setDescription(e.target.value)}/>
            </FormControl>
            <br/>
          </ModalBody>
          <ModalFooter>
            <Button onClick={onUpdate} colorScheme="blue" isLoading={loading == true}>Update</Button>
            <Spacer/>
            <Button onClick={onClose}>Close</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}