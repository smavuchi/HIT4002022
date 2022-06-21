import React from "react";
// Chakra imports
import {
  Box,
  Flex,
  Button,
  FormControl,
  FormLabel,
  Heading,
  Input,
  Link,
  Switch,
  Text,
  useColorModeValue,
} from "@chakra-ui/react";
// Assets

import {frontend, api} from "baseUrl";
import axios from "axios";

import signInImage from "assets/img/profile-banner.jpg";
const signupPage = `${frontend}/auth/signup`

function SignIn() {
  const [fields, setFields] = React.useState({
    email: "",
    password: ""
  });

  const [error, setError] = React.useState();
  const [loading, setLoading] = React.useState();

  // Chakra color mode
  const title1Color = useColorModeValue("black.400", "gray.200");
  const titleColor = useColorModeValue("blue.300", "blue.200");
  const textColor = useColorModeValue("gray.400", "white");

  const setField = (name, value) => {
    setError()
    setFields(values => ({...values, [name]: value}))
  }

  const signin = () => {
    for (let i = 0; i < Object.keys(fields).length; i++) {
      if (!(fields[Object.keys(fields)[i]]).trim()) {
        setError(`field required: ${Object.keys(fields)[i]}`);
        return;
      }
    }

    setLoading(true);
    axios.post(`${api}/auth/email`, {...fields, "returns": "api-key"}).then(({data}) => {
      setLoading(false);
      if (data.status != 200 && data.status != 201) {
        setError(data.message);
        return;
      }
      else {
        localStorage.setItem("api-key", data.data["api-key"]);
        window.location = `${frontend}/admin/dashboard`;
      }
    }).catch(e => {
      setLoading(false);
      setError("network problems. Please retry")
    })
  }

  return (
    <Flex position='relative' mb='40px'>
      <Flex
        h={{ sm: "initial", md: "75vh", lg: "85vh" }}
        w='100%'
        maxW='1044px'
        mx='auto'
        justifyContent='space-between'
        mb='30px'
        pt={{ sm: "100px", md: "0px" }}>
        <Flex
          alignItems='center'
          justifyContent='start'
          style={{ userSelect: "none" }}
          w={{ base: "100%", md: "50%", lg: "42%" }}>
          <Flex
            direction='column'
            w='100%'
            background='transparent'
            p='48px'
            mt={{ md: "150px", lg: "80px" }}>
            <Heading color={title1Color} fontSize='20px' mb='30px'>
              DATA APIs
            </Heading>
            <Heading color={titleColor} fontSize='32px' mb='10px'>
              Welcome Back
            </Heading>
            <Text
              mb='36px'
              ms='4px'
              color={textColor}
              fontWeight='bold'
              fontSize='14px'>
              Enter your email and password to sign in
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
                Email
              </FormLabel>
              <Input
                backgroundColor="white"
                borderRadius='15px'
                mb='24px'
                fontSize='sm'
                type='text'
                placeholder='Your email adress'
                size='lg'
                onChange={(e) => setField("email", e.target.value)}
              />
              <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
                Password
              </FormLabel>
              <Input
                backgroundColor="white"
                borderRadius='15px'
                mb='36px'
                fontSize='sm'
                type='password'
                placeholder='Your password'
                size='lg'
                onChange={(e) => setField("password", e.target.value)}
              />
              <Button
                fontSize='10px'
                type='submit'
                bg='blue.400'
                w='100%'
                h='45'
                mb='20px'
                color='white'
                mt='20px'
                _hover={{
                  bg: "blue.200",
                }}
                _active={{
                  bg: "blue.400",
                }}
                onClick={signin}
              >
                {loading ? "SIGNING IN..." : "SIGN IN"}
              </Button>
            </FormControl>
            <Flex
              flexDirection='column'
              justifyContent='center'
              alignItems='center'
              maxW='100%'
              mt='0px'>
              <Text color={textColor} fontWeight='medium'>
                Don't have an account?
                <Link color={titleColor} as='a' ms='5px' fontWeight='bold' href={signupPage}>
                  Sign Up
                </Link>
              </Text>
            </Flex>
          </Flex>
        </Flex>
        <Box
          display={{ base: "none", md: "block" }}
          overflowX='hidden'
          h='100%'
          w='40vw'
          position='absolute'
          right='0px'>
          <Box
            bgImage={signInImage}
            w='100%'
            h='100%'
            bgSize='cover'
            bgPosition='50%'
            position='absolute'
            borderBottomLeftRadius='20px'></Box>
        </Box>
      </Flex>
    </Flex>
  );
}

export default SignIn;
