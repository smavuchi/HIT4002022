import {
  Avatar,
  Badge,
  Button,
  Flex,
  Td,
  Text,
  Tr,
  useColorModeValue,
} from "@chakra-ui/react";


import {
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  MenuItemOption,
  MenuGroup,
  MenuOptionGroup,
  MenuDivider,
} from '@chakra-ui/react'

import {
  ChevronDownIcon
} from "@chakra-ui/icons";

import React from "react";

function TablesTableRow(props) {
  const { name, title, requests, date, id, select, expires } = props;
  const textColor = useColorModeValue("gray.700", "white");
  const bgStatus = useColorModeValue("gray.400", "#1a202c");
  const colorStatus = useColorModeValue("white", "gray.400");

  return (
    <Tr>
      <Td minWidth={{ sm: "250px" }} pl="0px">
        <Text fontSize="sm" color="gray.400" fontWeight="normal">
          {name}
        </Text>
      </Td>

      <Td minWidth={{ sm: "250px" }} pl="0px">
        <Flex align="center" py=".4rem" minWidth="100%" flexWrap="nowrap">
          <Flex direction="column">
            <Text fontSize="sm" color="gray.400" fontWeight="normal">
              {title}
            </Text>
          </Flex>
        </Flex>
      </Td>

      <Td>
        <Text fontSize="sm" color={textColor} fontWeight="bold" pb=".5rem">
          {requests}
        </Text>
      </Td>
      <Td>
        <Text fontSize="sm" color={textColor} fontWeight="bold" pb=".5rem">
          {expires}
        </Text>
      </Td>
    </Tr>
  );
}

export default TablesTableRow;
