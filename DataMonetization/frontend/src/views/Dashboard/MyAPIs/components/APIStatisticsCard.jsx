// Chakra imports
import {
  Flex,
  Stat,
  StatHelpText,
  StatLabel,
  StatNumber,
  useColorModeValue,
} from "@chakra-ui/react";
// Custom components
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import IconBox from "components/Icons/IconBox";
import React from "react";

export default function APIStatisticsCard({ title, value, icon, loading }) {
  const iconblue = useColorModeValue("#06f", "#06f");
  const textColor = useColorModeValue("gray.700", "white");

  return (
    <Card minH='83px' border="1px solid #aaa">
      <CardBody>
        <Flex flexDirection='row' align='center' justify='center' w='100%'>
          <Stat me='auto'>
            <StatLabel
              fontSize='sm'
              color='gray.400'
              fontWeight='bold'
              pb='.1rem'>
              {title}
            </StatLabel>
              <StatNumber fontSize='lg' color={textColor}>
                {(!loading) && value}
              </StatNumber>
              <StatHelpText
                alignSelf='flex-end'
                justifySelf='flex-end'
                m='0px'
                color={"blue.400"}
                fontWeight='bold'
                ps='3px'
                fontSize='xs'
              >
                {loading && "...loading"} 
              </StatHelpText>
          </Stat>
          <IconBox as='box' h={"45px"} w={"45px"} bg={iconblue}>
            {icon}
          </IconBox>
        </Flex>
      </CardBody>
    </Card>
  );
};
