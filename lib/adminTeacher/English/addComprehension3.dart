import 'package:flutter/material.dart';
import 'package:get/get.dart';

import 'adminEnglish.dart';

class AddComprehension3 extends StatefulWidget {
  const AddComprehension3({Key? key}) : super(key: key);

  @override
  _AddComprehension3State createState() => _AddComprehension3State();
}

class _AddComprehension3State extends State<AddComprehension3> {
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
    await new Future.delayed(const Duration(seconds: 5));
    return true;
  }
}


class AddSuccess extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Questions Generated Successfully'),
      ),
      body: Column(
        children: [
          SizedBox(height: 35.0,),
          Center(child: Text('Questions Added', style: TextStyle(
            fontSize: 30.0,
            fontWeight: FontWeight.bold,
          ),), ),
          SizedBox(height: 20.0,),
          ElevatedButton(onPressed: () {
            Get.to(AdminEnglish());
          }, child: Text('ADD MORE'))
        ],
      ),
    );
  }
}

