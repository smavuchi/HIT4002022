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

export default function DatasetInconsistentData({dataset, apiId, resourceId, fetch}) {
  const [saving, setSaving] = React.useState(false);
  const toast = useToast();

  const save = () => {
  	setSaving(true);

    axios.post(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/inconsistent-data`, {}).then(({data}) => {
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
	  <div style={{ padding: "20px 0 0 20px" }}>
      <p>Click the button bellow to fix capitalization and whitespace issues within the dataset</p>
      <br/>
	    <Button onClick={save}  isLoading={saving}>
	  	  Resolve Inconsistencies
	    </Button>
	  </div>
  	);
}