import {
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Box
} from '@chakra-ui/react'

import DatasetColumns from "./DatasetColumns";
import DatasetIdColumns from "./DatasetIdColumns";
import DatasetColumnTypes from "./DatasetColumnTypes";
import DatasetInconsistentData from "./DatasetInconsistentData";
import DatasetMissingValues from "./DatasetMissingValues";
import DatasetDuplicateRows from "./DatasetDuplicateRows";

export default function DatasetCleaning({dataset, apiId, resourceId, fetch}) {
  return (
  	<>
  	<Accordion allowToggle>
	  <AccordionItem>
	    <h2>
	      <AccordionButton _expanded={{ bg: '#06f', color: '#fff' }}>
	        <Box flex='1' textAlign='left'>
	          Set Columns
	        </Box>
	        <AccordionIcon />
	      </AccordionButton>
	    </h2>
	    <AccordionPanel pb={4}>
	      <DatasetColumns dataset={dataset} apiId={apiId} resourceId={resourceId} fetch={fetch}/>
	    </AccordionPanel>
	  </AccordionItem>
	  <AccordionItem>
	    <h2>
	      <AccordionButton _expanded={{ bg: '#06f', color: '#fff' }}>
	        <Box flex='1' textAlign='left'>
	          Set ID Columns
	        </Box>
	        <AccordionIcon />
	      </AccordionButton>
	    </h2>
	    <AccordionPanel pb={4}>
	      <DatasetIdColumns dataset={dataset} apiId={apiId} resourceId={resourceId} fetch={fetch}/>
	    </AccordionPanel>
	  </AccordionItem>
	  <AccordionItem>
	    <h2>
	      <AccordionButton _expanded={{ bg: '#06f', color: '#fff' }}>
	        <Box flex='1' textAlign='left'>
	          Set Column Types
	        </Box>
	        <AccordionIcon />
	      </AccordionButton>
	    </h2>
	    <AccordionPanel pb={4}>
	      <DatasetColumnTypes dataset={dataset} apiId={apiId} resourceId={resourceId} fetch={fetch}/>
	    </AccordionPanel>
	  </AccordionItem>
	  <AccordionItem>
	    <h2>
	      <AccordionButton _expanded={{ bg: '#06f', color: '#fff' }}>
	        <Box flex='1' textAlign='left'>
	          Resolve Inconsistent Data
	        </Box>
	        <AccordionIcon />
	      </AccordionButton>
	    </h2>
	    <AccordionPanel pb={4}>
	      <DatasetInconsistentData dataset={dataset} apiId={apiId} resourceId={resourceId} fetch={fetch}/>
	    </AccordionPanel>
	  </AccordionItem>
	  <AccordionItem>
	    <h2>
	      <AccordionButton _expanded={{ bg: '#06f', color: '#fff' }}>
	        <Box flex='1' textAlign='left'>
	          Resolve Missing Values
	        </Box>
	        <AccordionIcon />
	      </AccordionButton>
	    </h2>
	    <AccordionPanel pb={4}>
	      <DatasetMissingValues dataset={dataset} apiId={apiId} resourceId={resourceId} fetch={fetch}/>
	    </AccordionPanel>
	  </AccordionItem>
	  <AccordionItem>
	    <h2>
	      <AccordionButton _expanded={{ bg: '#06f', color: '#fff' }}>
	        <Box flex='1' textAlign='left'>
	          Resolve Duplicate Rows
	        </Box>
	        <AccordionIcon />
	      </AccordionButton>
	    </h2>
	    <AccordionPanel pb={4}>
	      <DatasetDuplicateRows dataset={dataset} apiId={apiId} resourceId={resourceId} fetch={fetch}/>
	    </AccordionPanel>
	  </AccordionItem>
	</Accordion>
  	</>
	);
}