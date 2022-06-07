import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/userLearner/english/englishCategory.dart';

import '../../databases/questionStorage.dart';
import 'englishComprehension2.dart';
import 'englishVideoContentPage.dart';


class EnglishQuestionAnswerTwoResult extends StatefulWidget {
  EnglishQuestionAnswerTwoResult({required this.question1Answer, required this.question2Answer,
    required this.question3Answer, required this.question4Answer, required this.question5Answer, required this.question6Answer, required this.mark});

  final String question1Answer;
  final String question2Answer;
  final String question3Answer;
  final String question4Answer;
  final String question5Answer;
  final String question6Answer;
  final int mark;



  @override
  _EnglishQuestionAnswerTwoResultState createState() => _EnglishQuestionAnswerTwoResultState();
}

class _EnglishQuestionAnswerTwoResultState extends State<EnglishQuestionAnswerTwoResult> {

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
            (widget.mark >= 5) ? Get.to(EnglishComprehensionTwoSuccess()) : Get.to(EnglishComprehensionTwoFailer());
          },
            child: Text('Continue', ),)
        ],
      ),
    );
  }
}







class EnglishComprehensionTwoSuccess extends StatefulWidget {

  @override
  _EnglishComprehensionTwoSuccessState createState() => _EnglishComprehensionTwoSuccessState();
}

class _EnglishComprehensionTwoSuccessState extends State<EnglishComprehensionTwoSuccess> {
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
              ElevatedButton(onPressed: () => Get.to(EnglishQuestionAnswerTwo()), child: Text('Redo')),

            ],
          ),
        ],
      ),
    );
  }
}



class EnglishComprehensionTwoFailer extends StatefulWidget {
  const EnglishComprehensionTwoFailer({Key? key}) : super(key: key);

  @override
  _EnglishComprehensionTwoFailerState createState() => _EnglishComprehensionTwoFailerState();
}

class _EnglishComprehensionTwoFailerState extends State<EnglishComprehensionTwoFailer> {
  @override
  Widget build(BuildContext context) {
    var _counter;
    return Scaffold(
      appBar: AppBar(title: Text('Please Try Again'),),
      body: Column(
        children: <Widget>[
          Text('You Tried Your Best!'),
          SizedBox(height: 15.0,),
          Text('Please Try the Exercise Again'),
          ElevatedButton(onPressed: () {
      Get.to(EnglishQuestionAnswerTwo());
    }, child: Text('Try Again'))

        ],
      ),

    );
  }
}

class EnglishComprehensionLimiter2 extends StatefulWidget {

  @override
  _EnglishComprehensionLimiter2State createState() => _EnglishComprehensionLimiter2State();
}

class _EnglishComprehensionLimiter2State extends State<EnglishComprehensionLimiter2> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body:Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Text('Unfortunately You Cant Try the Exercise Again'),
          SizedBox(height: 15.0,),
          Text('Go back to Lessons Page to learn more'),
          SizedBox(height: 15.0,),
          ElevatedButton(onPressed: () {
            var _counter;
            QuestionStorage.readQuestion2Counter();
            _counter <= 3 ? Get.to(EnglishQuestionAnswerTwo()) : Get.to(EnglishVideoContent());
            QuestionStorage.saveQuestion2Counter(_counter);
          },
            child: Text('Try Again'),)

        ],
      ),

    );
  }
}


