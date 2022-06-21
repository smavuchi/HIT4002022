// Chakra imports
import { Flex } from "@chakra-ui/react";
import React from "react";
import MyAPIs from "./components/Authors";
import { tablesTableData } from "variables/general";

import axios from "axios";

function Tables() {
  const [apis, setApis] = React.useState([]);
  
  React.useEffect(() => {

  }, []);

  return (
    <Flex direction='column' pt={{ base: "120px", md: "75px" }}>
      <MyAPIs
        title={"No name"}
        captions={["Name", "Title", "Published", "Created"]}
        data={tablesTableData}
      />
    </Flex>
  );
}

export default Tables;
