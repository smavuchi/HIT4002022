import "./style.css";
import React from "react";
import axios from "axios";

import { Button, useToast, Select } from "@chakra-ui/react";
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
  Input,

  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Box,

  FormControl,
  FormLabel,
  FormErrorMessage,
  FormHelperText,
} from '@chakra-ui/react'

import {frontend, api} from "baseUrl";

export default function DatasetMissingValues({dataset, apiId, resourceId, fetch}) {
  const [saving, setSaving] = React.useState(false);
  const [defaultValues, setDefaultValues] = React.useState({
    numeric: 0,
    nonnumeric: "__MISSING__"
  });

  const [rowMinMax, setRowMinMax] = React.useState({min: Object.keys(dataset.column_types).length, max: 100});
  const [colMinMax, setColMinMax] = React.useState({min: 100, max: 100});

  const toast = useToast();

  const save = (url, data) => {
    setSaving(true);

    axios.post(url, data).then(({data}) => {
      setSaving(false);
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
      setSaving(false);
    })
  }

  const insertFrequentValues = () => save(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/missing-data/insert-frequent-values`, {});
  const insertMedians = () => save(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/missing-data/insert-medians`, {});
  const insertDefaults = () => save(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/missing-data/insert-defaults`, defaultValues);
  const dropColumns = () => save(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/missing-data/drop-columns`, {
    min_percent: colMinMax.min
  });
  const dropRows = () => save(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/missing-data/drop-rows`, rowMinMax);

  return (
	  <div style={{ padding: "20px 0 0 20px" }}>
      <Accordion allowToggle>
        <AccordionItem>
          <h2>
            <AccordionButton _expanded={{ bg: '#eee' }}>
              <Box flex='1' textAlign='left'>
                Drop Columns
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <FormControl>
              <FormLabel htmlFor='colMin'>Minimum percentage</FormLabel>
              <Input 
                id='colMin' 
                type='number' 
                value={colMinMax.min}
                min={"0"}
                max={"100"}
                onChange={(e) => {
                  e.persist();
                  setColMinMax(s => ({...s, min: e.target.value}));
                }
              }/>
              <FormHelperText>Columns with percentage missing values greater than this will be dropped</FormHelperText>
            </FormControl>
            <br/>
            <Button onClick={dropColumns} isLoading={saving}>Drop Columns</Button>
          </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
          <h2>
            <AccordionButton _expanded={{ bg: '#eee' }}>
              <Box flex='1' textAlign='left'>
                Drop Rows
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <FormControl>
              <FormLabel htmlFor='colMin'>Minimum</FormLabel>
              <Input 
                id='colMin' 
                type='number' 
                value={rowMinMax.min}
                min={"0"}
                max={"100"}
                onChange={(e) => {
                  e.persist();
                  setRowMinMax(s => ({...s, min: e.target.value}));
                }
              }/>
              <FormHelperText>Rows with the number of missing values greater than this will be dropped</FormHelperText>
            </FormControl>
            <br/>
            <Button onClick={dropRows} isLoading={saving}>Drop Rows</Button>
          </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
          <h2>
            <AccordionButton _expanded={{ bg: '#eee' }}>
              <Box flex='1' textAlign='left'>
                Insert Defaults
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <FormControl>
              <FormLabel htmlFor='numeric'>Numeric</FormLabel>
              <Input 
                id='numeric' 
                type='number' 
                value={defaultValues.numeric}
                onChange={(e) => {
                  e.persist()
                  setDefaultValues(s => ({
                    ...s,
                    numeric: e.target.value
                  }))
                }
              }/>
              <FormHelperText>Default value for numeric fields</FormHelperText>
            </FormControl>
            <br/>
            <FormControl>
              <FormLabel htmlFor='nonnumeric'>Nonnumeric</FormLabel>
              <Input 
                id='nonnumeric' 
                type='text' 
                value={defaultValues.nonnumeric}
                onChange={(e) => {
                  e.persist()
                  setDefaultValues(s => ({
                    ...s,
                    nonnumeric: e.target.value
                  }))
                }
              }/>
              <FormHelperText>Default value for nonnumeric fields</FormHelperText>
            </FormControl>

            <br/>
            <Button onClick={insertDefaults} isLoading={saving}>Insert</Button>
          </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
          <h2>
            <AccordionButton _expanded={{ bg: '#eee' }}>
              <Box flex='1' textAlign='left'>
                Insert Medians
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <Button onClick={insertMedians} isLoading={saving}>Insert</Button>
          </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
          <h2>
            <AccordionButton _expanded={{ bg: '#eee' }}>
              <Box flex='1' textAlign='left'>
                Insert Frequent Values
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <Button onClick={insertFrequentValues} isLoading={saving}>Insert</Button>
          </AccordionPanel>
        </AccordionItem>
      </Accordion>
	  </div>
  	);
}