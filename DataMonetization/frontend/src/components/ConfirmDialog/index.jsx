import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Button,
  Input,
  Text,
  FormControl,
  FormLabel,
  FormErrorMessage,
  FormHelperText,
  Textarea,
  Spacer,
  InputGroup,
  InputLeftAddon
} from '@chakra-ui/react'

export default function ConfirmDialog({
	title, text, isOpen, onClose, deletion
}) {
	return (
    <Modal onClose={() => onClose(false)} isOpen={isOpen} isCentered size="xs">
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>{title}</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          <Text fontSize="lg">{text}</Text>
        </ModalBody>
        <ModalFooter>
          <Button onClick={() => onClose(true)} colorScheme={deletion ? "red" : "blue"}>Yes</Button>
          <Spacer/>
          <Button onClick={() => onClose(false)}>No</Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
	);
}