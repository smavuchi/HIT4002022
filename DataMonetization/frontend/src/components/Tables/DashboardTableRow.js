import {
  Avatar,
  AvatarGroup,
  Flex,
  Icon,
  Progress,
  Td,
  Text,
  Tr,
  useColorModeValue,
} from "@chakra-ui/react";
import React from "react";

function DashboardTableRow(props) {
  const { subscriber, amount, package: _package, api } = props;
  const textColor = useColorModeValue("gray.700", "white");
  return (
    <Tr>
      <Td>
        <Text fontSize="md" color={textColor} pb=".5rem">
          {subscriber}
        </Text>
      </Td>
      <Td>
        <Text fontSize="md" color={textColor} pb=".5rem">
          {api}
        </Text>
      </Td>
      <Td>
        <Text fontSize="md" color={textColor} pb=".5rem">
          {_package}
        </Text>
      </Td>
    </Tr>
  );
}

export default DashboardTableRow;
