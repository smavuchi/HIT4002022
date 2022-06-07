import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/adminTeacher/English/addComprehension3.dart';

class AddComprehension4 extends StatefulWidget {
  const AddComprehension4({Key? key}) : super(key: key);

  @override
  _AddComprehension4State createState() => _AddComprehension4State();
}

class _AddComprehension4State extends State<AddComprehension4> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Questions'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          SizedBox(height: 30.0,),
          ElevatedButton(onPressed: () async {
            showDialog(
                context: context,
                builder: (BuildContext context) {
                  return Column(
                    children: [
                      Text('Generating Questions...'),
                      Center(child: CircularProgressIndicator(),),
                    ],
                  );
                });
            await buttonAction();
            Get.to(AddSuccess());
          }, child: Text('AUTO-GENERATE'))
        ],
      ),
    );
  }

  Future<bool> buttonAction() async {
    //replace the below line of code with your login request
    await new Future.delayed(const Duration(seconds: 6));
    return true;
  }
}