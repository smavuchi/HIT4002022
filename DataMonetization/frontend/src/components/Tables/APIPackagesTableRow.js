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
import React from "react";
import {displayMoney} from "numbers";
import timeAgo from "timeAgo";

export default function APITableRow(props) {
  const { name, requests, pricing, date, id, select, _delete } = props;
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
          {requests}
        </Text>
      </Td>
      <Td minWidth={{ sm: "50px" }} pl="0px">
        <Text fontSize="sm" color="gray.400" fontWeight="normal">
          {displayMoney(pricing)}
        </Text>
      </Td>

      <Td>
        <Text fontSize="sm" color={textColor} fontWeight="bold" pb=".5rem">
          {timeAgo.format(new Date(date))}
        </Text>
      </Td>
      <Td>
        <Button p="0px" bg="transparent" variant="no-hover" onClick={() => select(id)}>
          <Text
            fontSize="sm"
            color="blue.400"
            fontWeight="bold"
            cursor="pointer"
          >
            View
          </Text>
        </Button>
      </Td>
      <Td>
        <Button p="0px" bg="transparent" variant="no-hover" onClick={() => _delete(id)}>
          <Text
            fontSize="sm"
            color="red.400"
            fontWeight="bold"
            cursor="pointer"
          >
            Delete
          </Text>
        </Button>
      </Td>
    </Tr>
  );
}
