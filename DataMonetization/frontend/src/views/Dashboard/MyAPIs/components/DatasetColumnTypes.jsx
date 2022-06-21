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
} from '@chakra-ui/react'

import {frontend, api} from "baseUrl";

const columnTypes = {
  "Integer": "i",
  "Boolean": "b", 
  "Unsigned Integer": "u", 
  "Float": "f", 
  "Complex Float": "c", 
  "Timedelta": "m", 
  "Datetime": "M", 
  "Object": "O", 
  "String": "S", 
  "Unicode String": "U", 
  "fixed chunk of memory for other type ( void )": "V"
};

export default function DatasetColumnTypes({dataset, apiId, resourceId, fetch}) {
  const [saving, setSaving] = React.useState(false);
  const [columns, setColumns] = React.useState({});

  const toast = useToast();

  React.useEffect(() => {
    setColumns(c => {
      let stuff  = {};
      Object.keys(dataset.column_types).forEach(item => {
        if (!Object.keys(columnTypes).includes(dataset.column_types[item])) {
          stuff[item] = null;
        } else {
          stuff[item] = dataset.column_types[item];
        }
      })
      return stuff;
    });
  }, [dataset]);

  const setType = (column, type) => {
  	setColumns(s => ({
  	  ...s,
      [column]: type
  	}))
  }

  const save = () => {
  	setSaving(true);
    let actualColumns = {};

    Object.keys(columns).forEach(item => {
      if (columns[item]) {
        actualColumns[item] = columns[item];
      }
    })

  	const data = {
  		column_types: actualColumns
  	};

    axios.post(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/column-types`, data).then(({data}) => {
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

  return (
  	<div style={{ backgroundColor: "#eee", padding: "30px 0" }}>
  	  <div 
	  	style={{
	  	  width: "80%",
	  	  border: "1px solid #ddd",
	  	  padding: "10px",
	  	  margin: "0 auto",
	  	  backgroundColor: "#fff"
  		}}
      >
        <div>
          <Table>
            <Tr>
              <Th>Column</Th>
              <Th>Type</Th>
            </Tr>
            {
              Object.keys(columns).map(item => (
                <Tr>
                  <Td style={{ margin: 0, padding: 0}}>{item}</Td>
                  <Td style={{ margin: 0, padding: 0}}>
                    <Select 
                      placeholder='Select type' 
                      selectedValue={columns[item]} 
                      style={{ color: "#000" }} 
                      size="md" 
                      onChange={(e) => setType(item, e.target.value)}
                    >
                      {
                        Object.keys(columnTypes).map(colType => (
                          <option value={columnTypes[colType]}>{colType}</option>
                          ))
                      }
                    </Select>
                  </Td>
                </Tr>
              ))
            }  
          </Table>
        </div>
  	  </div>
  	  <div style={{ padding: "30px 0 0 20px" }}>
  	    <Button onClick={save} colorScheme="blue" isLoading={saving}>
  	  	  Save changes
  	    </Button>
  	  </div>
  	</div>
  	);
}