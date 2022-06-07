import 'package:flutter/material.dart';

class Names extends StatelessWidget {
  const Names({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          SizedBox(height: 20.0,),
          Text('Registered Students'),
          Divider(),
          Text('Pamela Tavonga Mapfumo'),
          Divider(),
          Text("Takudzwa Chigwida"),
        ],
      ),
    );
  }
}
