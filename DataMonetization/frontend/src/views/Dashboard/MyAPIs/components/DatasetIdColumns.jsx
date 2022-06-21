import "./style.css";
import React from "react";
import axios from "axios";

import { Button, useToast } from "@chakra-ui/react";
import {frontend, api} from "baseUrl";

export default function DatasetIdColumns({dataset, apiId, resourceId, fetch}) {
  const [saving, setSaving] = React.useState(false);
  const [columns, setColumns] = React.useState({
  	keep: [],
  	discard: []
  });

  const toast = useToast();

  React.useEffect(() => {
  	setColumns(s => ({
  		keep: dataset.id_columns,
  		discard: Object.keys(dataset.column_types).filter(x => !dataset.id_columns.includes(x))
  	}))
  }, [dataset]);

  const keep = (item) => {
  	setColumns(s => ({
  	  discard: s.discard.filter(x => x != item),
  	  keep: [...s.keep, item]
  	}))
  }
  
  const discard = (item) => {
  	setColumns(s => ({
  	  keep: s.keep.filter(x => x != item),
  	  discard: [...s.discard, item]
  	}))
  }

  const save = () => {
  	setSaving(true);
  	const data = {
  		columns: columns.keep
  	};

    axios.post(`${api}/client-api/${apiId}/resources/${resourceId}/dataset/resolve/id-columns`, data).then(({data}) => {
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
	  	  display: "grid",
	  	  gridTemplateColumns: "1fr 1fr",
	  	  backgroundColor: "#fff"
  		}}
      >
      	<div>
      	  <p style={{ fontWeight: "bold", padding: "10px", border: "1px solid #ddd", marginBottom: "10px" }}>Non-ID columns</p>
      	  {
      	  	columns.discard.sort().map(item => (
      	  	  <div style={{ padding: "5px 10px", borderBottom: "1px solid #ddd" }} onClick={() => keep(item)} className="dataset-column-item" title="Click to keep instead">
      	  	  	{item}
      	  	  </div>
      	  	))
      	  }
      	  <div>{columns.discard.length === 0 && "No columns selected"}</div>
      	</div>
      	<div>
      	  <p style={{ fontWeight: "bold", padding: "10px", border: "1px solid #ddd", marginBottom: "10px" }}>ID Columns</p>
      	  {
      	  	columns.keep.sort().map(item => (
      	  	  <div style={{ padding: "5px 10px", borderBottom: "1px solid #ddd" }} onClick={() => discard(item)} className="dataset-column-item" title="Click to discard instead">
      	  	  	{item}
      	  	  </div>
      	  	))
      	  }
      	  <div>{columns.keep.length === 0 && "No columns selected"}</div>
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