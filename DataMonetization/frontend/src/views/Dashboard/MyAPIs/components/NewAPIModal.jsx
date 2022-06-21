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
  Spacer
} from '@chakra-ui/react'

import React from "react";
import axios from "axios";
import { useToast } from '@chakra-ui/react'

import {frontend, api} from "baseUrl";

export default function NewAPIModal({open, setOpen, onFinish}) {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState();
  
  const [name, setName] = React.useState();
  const [title, setTitle] = React.useState();
  const [description, setDescription] = React.useState();

  const toast = useToast()

  const onClose = () => {
    setOpen(false);
  }

  const onCreate = () => {
    setLoading(true);
    setError();

    axios.post(`${api}/client-api`, { name, title, description }).then(({data}) => {
      setLoading(false);
      if (data.status != 200 && data.status != 201) {
        setError(data.message);
        return;
      }
      else {
        onFinish();
        toast({
          title: 'API created',
          description: "We've created your API for you.",
          duration: 3000,
          isClosable: true,
        })
        setName(); setTitle(); setDescription()
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
          <ModalHeader>New API</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {error && <><Text style={{ color: "red"}}>{error}</Text><br/></>}

            <FormControl isRequired>
              <FormLabel htmlFor='api-name'>Name</FormLabel>
              <Input 
                id='api-name' 
                type='text' 
                placeholder="eg: metals-api" 
                value={name} 
                onChange={(e) => setName(e.target.value)}/>
              <FormHelperText>A url-friendly name that is short and precise</FormHelperText>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-title'>Title</FormLabel>
              <Input 
                id='api-title' 
                type='text' 
                placeholder="eg: Real-time metal prices API"
                value={title} 
                onChange={(e) => setTitle(e.target.value)}/>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-description'>Description</FormLabel>
               <Textarea
                id="api-description"
                placeholder='Enter description text...'
                size='sm'
                value={description} 
                onChange={(e) => setDescription(e.target.value)}/>
            </FormControl>
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