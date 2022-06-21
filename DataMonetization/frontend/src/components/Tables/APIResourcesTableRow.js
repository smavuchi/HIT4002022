import {
  Avatar,
  Badge,
  Button,
  Flex,
  Td,
  Text,
  Tr,
  useColorModeValue
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
import {displayMoney} from "numbers";
import timeAgo from "timeAgo";

export default function APITableRow(props) {
  const { name, urlName, date, id, select, _delete, actions, status, publish, setOpenDataset } = props;
  const textColor = useColorModeValue("gray.700", "white");
  const bgStatus = useColorModeValue("gray.400", "#1a202c");
  const colorStatus = useColorModeValue("white", "gray.400");

  return (
    <Tr>
      <Td pl="0px">
        <Text fontSize="sm" color="gray.400" fontWeight="normal">
          {name}
        </Text>
      </Td>
      <Td pl="0px">
        <Text fontSize="sm" color="gray.400" fontWeight="normal">
          {urlName}
        </Text>
      </Td>
      <Td pl="0px">
        <Text fontSize="sm" color="gray.400" fontWeight="normal">
          {actions.join(", ")}
        </Text>
      </Td>
      <Td>
        <Badge
          bg={status === "Published" ? "blue.400" : bgStatus}
          color={status === "Published" ? "white" : colorStatus}
          fontSize="xs"
          p="3px 10px"
          borderRadius="8px"
        >
          {status}
        </Badge>
      </Td>
      <Td>
        <Text fontSize="sm" color={textColor} fontWeight="bold" pb=".5rem">
          {timeAgo.format(new Date(date))}
        </Text>
      </Td>
      <Td>
        

        <Menu size="sm">
          <MenuButton as={Button} rightIcon={<ChevronDownIcon />} size="sm" colorScheme="blue" variant="outline">
            Actions
          </MenuButton>
          <MenuList>
            <MenuItem onClick={() => select(id)}>View</MenuItem>
            <MenuItem onClick={() => setOpenDataset(id)}>Dataset</MenuItem>
            <MenuItem onClick={() => publish(id)}>Publish</MenuItem>
            <MenuItem onClick={() => _delete(id)}>Delete</MenuItem>
          </MenuList>
        </Menu>

      </Td>
    </Tr>
  );
}