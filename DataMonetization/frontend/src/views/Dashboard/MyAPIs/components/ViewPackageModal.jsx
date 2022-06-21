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

export default function ViewAPIPackageModal({open, setOpen, onFinish, apiId, packageId, ...props}) {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState();
  
  const [name, setName] = React.useState();
  const [pricing, setPricing] = React.useState(0);
  const [requests, setRequests] = React.useState(10);
  const [description, setDescription] = React.useState();

  const [url, setUrl] = React.useState(`${api}/client-api/${apiId}/packages/${packageId}`);
  const {data: apiPackage, loading: packageLoading, error: errorLoadingPackage, response} = useFetcher({url});

  const toast = useToast()

  const onClose = () => {
    props.onClose();
  }

  const onUpdate = () => {
    setLoading(true);
    setError();

    axios.post(`${api}/client-api/${apiId}/packages/${packageId}/update`, { name, pricing, description, requests }).then(({data}) => {
      setLoading(false);
      if (data.status != 200 && data.status != 201) {
        setError(data.message);
        return;
      }
      else {
        onFinish();
        toast({
          title: 'API package updated',
          description: "We've updated your API package for you.",
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
    if (!apiPackage) {
      return;
    }
    setName(apiPackage.name);
    setRequests(apiPackage.requests);
    setPricing(apiPackage.pricing);
    setDescription(apiPackage.description);
  }, [apiPackage])

  return (
    <>
      <Modal onClose={onClose} isOpen={open} isCentered>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>View API Package</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {error && <><Text style={{ color: "red"}}>{error}</Text><br/></>}

            <FormControl isRequired>
              <FormLabel htmlFor='api-package-name'>Name</FormLabel>
              <Input 
                id='api-package-name' 
                type='text' 
                placeholder="eg. starter, enterprise" 
                value={name} 
                onChange={(e) => setName(e.target.value)}/>
              <FormHelperText>A url-friendly name that is short and precise</FormHelperText>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-package-description'>Description</FormLabel>
               <Textarea
                id="api-package-description"
                placeholder='Enter description text...'
                size='sm'
                value={description} 
                onChange={(e) => setDescription(e.target.value)}/>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-package-requests'>Requests</FormLabel>
              <Input 
                id='api-package-requests' 
                type='number' 
                placeholder="eg: 10"
                value={requests} 
                onChange={(e) => setRequests(e.target.value)}/>
              <FormHelperText>Maximum number of requests subscribers can make</FormHelperText>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='api-package-price'>Pricing</FormLabel>

              <InputGroup>
                <InputLeftAddon children='USD $' />
                <Input 
                  id='api-package-price' 
                  type='number' 
                  placeholder="eg: 10"
                  value={pricing} 
                  onChange={(e) => setPricing(e.target.value)}/>
              </InputGroup>
            </FormControl>
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