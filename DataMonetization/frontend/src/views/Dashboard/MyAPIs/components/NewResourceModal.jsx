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

export default function NewAPIPackageModal({open, setOpen, onFinish, apiId, ...props}) {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState();
  
  const [name, setName] = React.useState();
  const [urlName, setUrlName] = React.useState();
  const [description, setDescription] = React.useState();

  const toast = useToast()

  const onClose = () => {
    props.onClose();
  }

  const onCreate = () => {
    setLoading(true);
    setError();

    axios.post(`${api}/client-api/${apiId}/resources`, { name, urlName, description }).then(({data}) => {
      setLoading(false);
      if (data.status != 200 && data.status != 201) {
        setError(data.message);
        return;
      }
      else {
        onFinish();
        toast({
          title: 'API resource created',
          description: "We've created your API resource for you.",
          duration: 3000,
          isClosable: true,
        })
        setName(); setUrlName(); setDescription();
        onClose();
      }
    }).catch(e => {
      setLoading(false);
      setError("network problems. Please retry")
    })
  }

  return (
    <>
      <Modal onClose={onClose} isOpen={open} isCentered>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>New API Resource</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {error && <><Text style={{ color: "red"}}>{error}</Text><br/></>}
            <FormControl isRequired>
              <FormLabel htmlFor='api-resource-name'>Name</FormLabel>
              <Input 
                id='api-resource-name' 
                type='text' 
                placeholder="eg. metal" 
                value={name} 
                onChange={(e) => setName(e.target.value)}/>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-resource-url-name'>URL Name</FormLabel>
              <Input 
                id='api-resource-url-name' 
                type='text' 
                placeholder="eg. metals" 
                value={urlName} 
                onChange={(e) => setUrlName(e.target.value)}/>
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
            <Button onClick={onCreate} colorScheme="blue" isLoading={loading == true}>Create</Button>
            <Spacer/>
            <Button onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}