import 'package:flutter/material.dart';
import 'package:get/get.dart';

class Controller extends GetxController {
  final textController = TextEditingController();

  RxString controllerText = ''.obs;

  @override
  void onInit() {
    super.onInit();
    textController.addListener(() {
      controllerText.value = textController.text;
    });
  }


}