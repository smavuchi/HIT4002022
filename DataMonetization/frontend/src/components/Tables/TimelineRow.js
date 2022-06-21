import { Box, Flex, Icon, Text, useColorModeValue } from "@chakra-ui/react";
import IconBox from "components/Icons/IconBox";
import React from "react";
import { Avatar } from "@chakra-ui/react";

function TimelineRow(props) {
  const { email, when } = props;
  const textColor = useColorModeValue("gray.700", "white.300");
  const bgIconColor = useColorModeValue("white.300", "gray.700");

  return (
    <Box mb={"10px"}>
      
      <Text>
        <Avatar w="20px" h="20px" me="15px"/>{email}
        &nbsp;<span style={{color: "#aaa", "font-size": ".8em"}}>{when}</span>
      </Text>
    </Box>
  );
}

export default TimelineRow;
