import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'ictResultPage.dart';


class ICTQuestionAnswer extends StatefulWidget {


  @override
  _ICTQuestionAnswerState createState() => _ICTQuestionAnswerState();
}

class _ICTQuestionAnswerState extends State<ICTQuestionAnswer> {
  @override
  Widget build(BuildContext context) {
    TextEditingController _questionController = new TextEditingController();
    int _mark = 0;
    return Scaffold(
      appBar: AppBar(
        title: Text('Chapter Quiz'),
      ),
      body: Container(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Text(
              'Whats is the brain of the computer?'
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
                  var _questionAnswer = _questionController.text.toString().toUpperCase();

                  //Logic to add marks if answer is correct
                  if (_questionAnswer.contains('CPU')) {setState(() {
                    _mark++;
                  });} else {
                    _mark = _mark;
                  }
                  SystemSound.play(SystemSoundType.click);
                  Get.to(ICTResult(questionAnswer: _questionAnswer, mark: _mark,),
                    );

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

