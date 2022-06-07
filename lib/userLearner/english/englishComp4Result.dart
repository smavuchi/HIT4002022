import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/userLearner/english/englishCategory.dart';

import '../../databases/questionStorage.dart';
import 'englishComp4.dart';
import 'englishVideoContentPage.dart';


class EnglishQuestionAnswerFourResult extends StatefulWidget {
  EnglishQuestionAnswerFourResult({required this.question1Answer, required this.question2Answer,
    required this.question3Answer, required this.question4Answer, required this.question5Answer, required this.question6Answer, required this.mark});

  final String question1Answer;
  final String question2Answer;
  final String question3Answer;
  final String question4Answer;
  final String question5Answer;
  final String question6Answer;
  final int mark;



  @override
  _EnglishQuestionAnswerFourResultState createState() => _EnglishQuestionAnswerFourResultState();
}

class _EnglishQuestionAnswerFourResultState extends State<EnglishQuestionAnswerFourResult> {

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(title: Text('Chapter Result'),),
      body: Column(
        children: <Widget>[
          Text((widget.mark >= 5) ? 'You Have Successfully Completed the exercise' : 'Good Try. Please Try Again', style: TextStyle(
            fontSize: 24.0,
            fontWeight: FontWeight.bold,
          ),),
          SizedBox(height: 20.0,),
          Text(' ${widget.mark}/6', style: TextStyle(fontSize: 30.0, ),),
          SizedBox(height: 20.0,),
          ElevatedButton(onPressed: () {
            SystemSound.play(SystemSoundType.alert);
            (widget.mark >= 5) ? Get.to(EnglishComprehensionFourSuccess()) : Get.to(EnglishComprehensionFourFailer());
          },
            child: Text('Continue', ),)
        ],
      ),
    );
  }
}







class EnglishComprehensionFourSuccess extends StatefulWidget {

  @override
  _EnglishComprehensionFourSuccessState createState() => _EnglishComprehensionFourSuccessState();
}

class _EnglishComprehensionFourSuccessState extends State<EnglishComprehensionFourSuccess> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Options'),),
      body: Column(
        children: <Widget>[
          Text('Do you Want to Redo The Exercise Again or Try Another One'),
          SizedBox(height: 20.0,),
          Row(
            children: <Widget>[
              ElevatedButton(onPressed: () => Get.to(UserEnglishSelector()), child: Text('Try Another One')),
              SizedBox(width: 20.0,),
              ElevatedButton(onPressed: () => Get.to(EnglishQuestionAnswerFour()), child: Text('Redo')),

            ],
          ),
        ],
      ),
    );
  }
}





class EnglishComprehensionFourFailer extends StatefulWidget {
  const EnglishComprehensionFourFailer({Key? key}) : super(key: key);

  @override
  _EnglishComprehensionFourFailerState createState() => _EnglishComprehensionFourFailerState();
}

class _EnglishComprehensionFourFailerState extends State<EnglishComprehensionFourFailer> {
  @override
  Widget build(BuildContext context) {
    var _counter;
    return Scaffold(
      appBar: AppBar(title: Text('Please Try Again'),),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Text('You Tried Your Best!'),
          SizedBox(height: 15.0,),
          Text('Please Try the Exercise Again'),
          SizedBox(height: 20.0,),
          ElevatedButton(onPressed: () {
            // _counter = int.parse( QuestionStorage.readQuestion4Counter()) + _counter + 1;
            // if (_counter >= 3) {
            //   Get.to(EnglishComprehensionLimiter());
            // } else
              Get.to(EnglishQuestionAnswerFour());
           // QuestionStorage.saveQuestion4Counter(_counter);
    },
            child: Text('Try Again'))

        ],
      ),

    );
  }
}

class EnglishComprehensionLimiter4 extends StatefulWidget {

  @override
  _EnglishComprehensionLimiter4State createState() => _EnglishComprehensionLimiter4State();
}

class _EnglishComprehensionLimiter4State extends State<EnglishComprehensionLimiter4> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body:Column(
        children: <Widget>[
          Text('Unfortunately You Cant Try the Exercise Again'),
          SizedBox(height: 15.0,),
          Text('Go back to Lessons Page to learn more'),
          SizedBox(height: 15.0,),
          ElevatedButton(onPressed: () {
            var _counter;
            QuestionStorage.readQuestion4Counter();
            _counter <= 3 ? Get.to(EnglishQuestionAnswerFour()) : Get.to(EnglishVideoContent());
          },
            child: Text('Try Again'),)

        ],
      ),

    );
  }
}