import 'package:flutter/material.dart';
import 'package:get/get.dart';

import 'addAddition.dart';
import 'addSubtraction.dart';

class AdminMaths extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Questions'),

      ),
        body: Column(
            children: <Widget>[
              Text('Choose Question Type'),
              Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                 GestureDetector(
                   onTap: () => Get.to(AddAddition()),
                   child: Column(
                     children: [
                       Icon(Icons.add, size: 30.0),
                       Text('Addition')
                     ],
                   ),
                 ),
                GestureDetector(
                  onTap: () => Get.to(AddSubtraction()),
                  child: Column(
                    children: [
                      Icon(Icons.remove, size: 30.0,),
                      Text('Subtraction'),
                    ],
                  ),
                ),
                ],
              ),
            ],
        )
    );
  }
}
