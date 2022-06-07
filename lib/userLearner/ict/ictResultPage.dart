import 'package:flutter/material.dart';


class ICTResult extends StatefulWidget {
  String questionAnswer;
  int mark;

  ICTResult({required this.questionAnswer, required this.mark });
  _ICTResultState createState() => _ICTResultState();
}

class _ICTResultState extends State<ICTResult> {
  @override
  Widget build(BuildContext context) {

    return Scaffold(
      body: Column(
        children: <Widget>[
         Center(
           child: Text('Your Mark is ${widget.mark}'),
         )
        ],
      ),
    );
  }
}
