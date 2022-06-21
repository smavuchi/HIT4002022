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
  InputLeftAddon,
} from '@chakra-ui/react'
import { Tabs, TabList, TabPanels, Tab, TabPanel } from '@chakra-ui/react'

import React from "react";
import axios from "axios";
import { useToast } from '@chakra-ui/react'

import {frontend, api} from "baseUrl";
import useFetcher from "fetch";
import DatasetIssues from "./DatasetIssues";
import DatasetCleaning from "./DatasetCleaning";
import DatasetPreview from "./DatasetPreview"

export default function ViewAPIDatasetModal({open, setOpen, onFinish, apiId, resourceId, ...props}) {
  const [activeTab, setActiveTab] = React.useState("dataset");

  const [url, setUrl] = React.useState(`${api}/client-api/${apiId}/resources/${resourceId}/dataset`);
  const {data, loading, error, fetch} = useFetcher({url});
  const {data: datasetIssues, fetch: fetchDatasetIssues} = useFetcher({url: url + "/info/issues"});

  const [title, setTitle] = React.useState();
  const [file, setFile] = React.useState();
  const [issues, setIssues] = React.useState();
  
  const [addingDataset, setAddingDataset] = React.useState();

  const toast = useToast()

  const onClose = () => {
    props.onClose();
  }

  const onAddDataset = () => {
    setAddingDataset(true);

    let data = new FormData();
    data.append("title", title)
    data.append("dataset", file)

    axios.post(`${api}/client-api/${apiId}/resources/${resourceId}/dataset`, data).then(({data}) => {
      setAddingDataset(false);
      if (data.status != 200 && data.status != 201) {
        toast({
          title: 'API dataset not updated',
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
          title: 'API dataset updated',
          description: "We've updated your API dataset for you.",
          duration: 3000,
          isClosable: true,
        })
        fetch();
      }
    }).catch(e => {
      toast({
        title: 'API dataset not updated',
        description: "network problems. Please retry",
        duration: 3000,
        error: true,
        success: false,
        isClosable: true,
      })
      setAddingDataset(false);
    })
  }

  React.useEffect(() => {
    if (data) {
      fetchDatasetIssues()
      setTitle(data.title)
    }
  }, [data])

  return (
    <>
      <Modal onClose={onClose} isOpen={open} isCentered size="full" scrollBehavior="inside">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>API Dataset</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {error && <><Text style={{ color: "red"}}>{error}</Text><br/></>}
            <div style={{ height: "200px"}}>
              <Tabs variant="enclosed" size="sm" width="100%">
                <TabList>
                  <Tab onClick={() => setActiveTab("dataset")}>Dataset</Tab>
                  <Tab onClick={() => setActiveTab("preview")}>Preview</Tab>
                  <Tab onClick={() => setActiveTab("types")}>Column Types</Tab>
                  <Tab onClick={() => setActiveTab("descriptions")}>Column Descriptions</Tab>
                  <Tab onClick={() => setActiveTab("kurtosis")}>Kurtosis per Column</Tab>
                  <Tab onClick={() => setActiveTab("missing")}>Missing values by Column</Tab>
                  <Tab onClick={() => setActiveTab("issues")}>Issues</Tab>
                  <Tab onClick={() => setActiveTab("clean")}>Clean</Tab>
                </TabList>

                <TabPanels>
                  <TabPanel>
                    <FormControl isRequired>
                      <FormLabel htmlFor='api-dataset-title'  size="sm">Title</FormLabel>
                      <Input 
                        id='api-dataset-title' 
                        type='text'
                        size="sm" 
                        placeholder="eg. metals" 
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}/>
                    </FormControl>
                    <br/>  
                    <FormControl isRequired>
                      <FormLabel htmlFor='api-dataset-file'  size="sm">File</FormLabel>
                      <Input 
                        id='api-dataset-file' 
                        type='file' 
                        placeholder="eg. metals"
                        size="sm"
                        onChange={(e) => setFile(e.target.files[0])}/>
                    </FormControl>
                    <br/>          
                    <Button onClick={onAddDataset} colorScheme="blue" isLoading={addingDataset} size="sm" fontWeight="regular">Update Dataset</Button>
                  </TabPanel>
                  <TabPanel>
                    {data && activeTab === "preview" && <DatasetPreview dataset={data} resourceId={resourceId} apiId={apiId}/>}
                    {(!data) && "Upload a dataset first"}
                  </TabPanel>
                  <TabPanel>
                    {data && activeTab === "types" && Object.keys(data.column_types).map((name, index) => (
                      <div>
                        <Text> <Text style={{ color: "blue", display: "inline"}} fontWeight="bold">{index + 1}</Text>. {name}: <Text style={{ color: "red", display: "inline"}} fontWeight="bold">{data.column_types[name]}</Text></Text>
                      </div>
                      ))}
                    {(!data) && "Upload a dataset first"}
                  </TabPanel>
                  <TabPanel>
                    {data && activeTab === "descriptions" && Object.keys(data.columns_description).map((name, index) => (
                      <div>
                        <Text> 
                          <Text style={{ color: "blue", display: "inline"}} fontWeight="bold">{index + 1}. {name}</Text>: <Text style={{ color: "black", display: "inline"}} fontWeight="normal">
                            {"{"}
                            {Object.keys(data.columns_description[name]).map(key => (
                              <>
                              <Text fontWeight="bold" style={{ display: "inline" }}>{key}</Text> : {" "}
                              <Text fontWeight="normal" style={{ display: "inline" }}>{data.columns_description[name][key]}</Text>, {" "}
                              </>
                              ))}
                            {"}"}
                          </Text>
                        </Text>
                      </div>
                      ))}
                    {(!data) && "Upload a dataset first"}
                  </TabPanel>
                  <TabPanel>
                    {data && activeTab === "kurtosis" && Object.keys(data.kurt_per_column).map((name, index) => (
                      <div>
                        <Text> <Text style={{ color: "blue", display: "inline"}} fontWeight="bold">{index + 1}</Text>. {name}: <Text style={{ color: "red", display: "inline"}} fontWeight="bold">{data.kurt_per_column[name]}</Text></Text>
                      </div>
                      ))}
                    {(!data) && "Upload a dataset first"}
                  </TabPanel>
                  <TabPanel>
                    {data && activeTab === "missing" && Object.keys(data.percentage_missing_values_by_column).map((name, index) => (
                      <div>
                        <Text> <Text style={{ color: "blue", display: "inline"}} fontWeight="bold">{index + 1}</Text>. {name}: <Text style={{ color: "red", display: "inline"}} fontWeight="bold">{data.percentage_missing_values_by_column[name]*100}%</Text></Text>
                      </div>
                      ))}
                    {(!data) && "Upload a dataset first"}
                  </TabPanel>
                  <TabPanel>
                    <DatasetIssues data={datasetIssues}/>
                  </TabPanel>
                  <TabPanel>
                    {data && activeTab === "clean" && <DatasetCleaning dataset={data} apiId={apiId} resourceId={resourceId} fetch={fetch}/>}
                  </TabPanel>
                </TabPanels>
              </Tabs>
            </div>

          </ModalBody>
          <ModalFooter>
            <Spacer/>
            <Button onClick={onClose}>Close</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}