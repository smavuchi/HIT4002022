// Chakra imports
import {
  Box,
  Button,
  Flex,
  FormControl,
  FormLabel,
  HStack,
  Icon,
  Input,
  Link,
  Switch,
  Text,
  useColorModeValue,
} from "@chakra-ui/react";
// Assets
import BgSignUp from "assets/img/profile-banner.jpg";
import React from "react";
import { FaApple, FaFacebook, FaGoogle } from "react-icons/fa";
import axios from "axios";

import {frontend, api} from "baseUrl";
const signInHref = `${frontend}/auth/signin`;

function SignUp() {
  const [fields, setFields] = React.useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    "confirmation_password": ""
  });

  const [error, setError] = React.useState();
  const [loading, setLoading] = React.useState();

  const titleColor = useColorModeValue("blue.300", "blue.200");
  const textColor = useColorModeValue("gray.700", "white");
  const bgColor = useColorModeValue("white", "gray.700");
  const bgIcons = useColorModeValue("blue.200", "rgba(255, 255, 255, 0.5)");
  
  const setField = (name, value) => {
    setError()
    setFields(values => ({...values, [name]: value}))
  }

  const signup = () => {
    for (let i = 0; i < Object.keys(fields).length; i++) {
      if (!(fields[Object.keys(fields)[i]]).trim()) {
        setError(`field required: ${Object.keys(fields)[i]}`);
        return;
      }
    }

    setLoading(true);
    axios.post(`${api}/users/register`, fields).then(({data}) => {
      setLoading(false);
      if (data.status != 200 && data.status != 201) {
        setError(data.message);
        return;
      }
      else {
        window.location = `${frontend}/auth/signin`;
      }
    }).catch(e => {
      setLoading(false);
      setError("network problems. Please retry")
    })
  }

  return (
    <Flex
      direction='column'
      alignSelf='center'
      justifySelf='center'
      overflow='hidden'>
      <Box
        position='absolute'
        minH={{ base: "70vh", md: "50vh" }}
        w={{ md: "calc(100vw - 50px)" }}
        borderRadius={{ md: "15px" }}
        left='0'
        right='0'
        bgRepeat='no-repeat'
        overflow='hidden'
        zIndex='-1'
        top='0'
        bgImage={BgSignUp}
        bgSize='cover'
        mx={{ md: "auto" }}
        mt={{ md: "14px" }}></Box>
      <Flex
        direction='column'
        textAlign='center'
        justifyContent='center'
        align='center'
        mt='6.5rem'
        mb='30px'>
        <Text fontSize='1xl' color='white' fontWeight='bold' textDecoration="underline">
          DATA APIs
        </Text>

        <Text fontSize='4xl' color='white' fontWeight='bold'>
          Welcome!
        </Text>
        <Text
          fontSize='md'
          color='white'
          fontWeight='normal'
          mt='10px'
          mb='26px'
          w={{ base: "90%", sm: "60%", lg: "40%", xl: "30%" }}>
          Enter your details below to sign up for an account
        </Text>
      </Flex>
      <Flex alignItems='center' justifyContent='center' mb='60px' mt='20px'>
        <Flex
          direction='column'
          w='445px'
          background='transparent'
          borderRadius='15px'
          p='40px'
          mx={{ base: "100px" }}
          bg={bgColor}
          boxShadow='0 20px 27px 0 rgb(0 0 0 / 5%)'>
          <Text
            fontSize='xl'
            color={textColor}
            fontWeight='bold'
            textAlign='center'
            mb='22px'>
            Sign up
          </Text>
          {error && <Text
            fontSize='xs'
            color="red"
            fontWeight='bold'
            textAlign='center'
            mb='22px'>
            {error}
          </Text>}
          <FormControl>
            <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
              First Name
            </FormLabel>
            <Input
              fontSize='sm'
              ms='4px'
              borderRadius='15px'
              type='text'
              placeholder='Your first name'
              mb='24px'
              size='lg'
              onChange={(e) => setField("first_name", e.target.value)}
            />
            <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
              Last Name
            </FormLabel>
            <Input
              fontSize='sm'
              ms='4px'
              borderRadius='15px'
              type='text'
              placeholder='Your last name'
              mb='24px'
              size='lg'
              onChange={(e) => setField("last_name", e.target.value)}
            />
            <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
              Email
            </FormLabel>
            <Input
              fontSize='sm'
              ms='4px'
              borderRadius='15px'
              type='email'
              placeholder='Your email address'
              mb='24px'
              size='lg'
              onChange={(e) => setField("email", e.target.value)}
            />
            <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
              Password
            </FormLabel>
            <Input
              fontSize='sm'
              ms='4px'
              borderRadius='15px'
              type='password'
              placeholder='Your password'
              mb='24px'
              size='lg'
              onChange={(e) => setField("password", e.target.value)}
            />
            <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
              Confirmation Password
            </FormLabel>
            <Input
              fontSize='sm'
              ms='4px'
              borderRadius='15px'
              type='password'
              placeholder='Confirm your password'
              mb='24px'
              size='lg'
              onChange={(e) => setField("confirmation_password", e.target.value)}
            />
            <Button
              type='submit'
              bg='blue.400'
              fontSize='10px'
              color='white'
              fontWeight='bold'
              w='100%'
              h='45'
              mb='24px'
              _hover={{
                bg: "blue.200",
              }}
              _active={{
                bg: "blue.400",
              }}
              onClick={signup}
            >
              {loading ? "SIGNING UP..." : "SIGN UP"}
            </Button>
          </FormControl>
          <Flex
            flexDirection='column'
            justifyContent='center'
            alignItems='center'
            maxW='100%'
            mt='0px'>
            <Text color={textColor} fontWeight='medium'>
              Already have an account?
              <Link
                color={titleColor}
                as='a'
                ms='5px'
                href='#'
                fontWeight='bold'
                href={signInHref}
              >
                Sign In
              </Link>
            </Text>
          </Flex>
        </Flex>
      </Flex>
    </Flex>
  );
}

export default SignUp;
