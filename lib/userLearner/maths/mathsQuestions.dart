import 'package:flutter/material.dart';

class MathsQuestionAnswer extends StatefulWidget {



  @override
  _MathsQuestionAnswerState createState() => _MathsQuestionAnswerState();
}

class _MathsQuestionAnswerState extends State<MathsQuestionAnswer> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Chapter Quiz'),
      ),
      body: Container(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Text(
                '10+10'
            ),
            Divider(),
            Form(
              child: TextFormField(
                  decoration: InputDecoration(
                      labelText: "Put In the Correct Answer Here!",
                      labelStyle: TextStyle(color: Colors.blueGrey)
                  ),

                  ),
            ),

            Padding(
              padding: const EdgeInsets.symmetric(vertical: 16.0),
              child: ElevatedButton(
                onPressed: () {

                }, child: Text(
                  'SUBMIT'
              ),
              ),



            ),
          ],
        ),
      ),
    );
  }
}

