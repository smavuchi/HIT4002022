import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import '../../databases/questionStorage.dart';
import 'package:intelligent_teacher/userLearner/english/englishCategory.dart';
import 'englishComprehensionOne.dart';
import 'englishVideoContentPage.dart';

class EnglishQuestionAnswerOneResult extends StatefulWidget {
EnglishQuestionAnswerOneResult({required this.question1Answer, required this.question2Answer,
  required this.question3Answer, required this.question4Answer, required this.question5Answer, required this.question6Answer, required this.mark});

final String question1Answer;
final String question2Answer;
final String question3Answer;
final String question4Answer;
final String question5Answer;
final String question6Answer;
final int mark;

  @override
  _EnglishQuestionAnswerOneResultState createState() => _EnglishQuestionAnswerOneResultState();
}

class _EnglishQuestionAnswerOneResultState extends State<EnglishQuestionAnswerOneResult> {

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
            (widget.mark >= 5) ? Get.to(EnglishComprehensionOneSuccess()) : Get.to(EnglishComprehensionOneFailer());
          },
          child: Text('Continue', ),)
        ],
    ),
    );
  }
}




class EnglishComprehensionOneSuccess extends StatefulWidget {
  const EnglishComprehensionOneSuccess({Key? key}) : super(key: key);

  @override
  _EnglishComprehensionOneSuccessState createState() => _EnglishComprehensionOneSuccessState();
}

class _EnglishComprehensionOneSuccessState extends State<EnglishComprehensionOneSuccess> {
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
              ElevatedButton(onPressed: () => Get.to(EnglishQuestionAnswerOne()), child: Text('Redo')),

            ],
          ),
        ],
      ),
    );
  }
}


class EnglishComprehensionOneFailer extends StatefulWidget {
  const EnglishComprehensionOneFailer({Key? key}) : super(key: key);

  @override
  _EnglishComprehensionOneFailerState createState() => _EnglishComprehensionOneFailerState();
}

class _EnglishComprehensionOneFailerState extends State<EnglishComprehensionOneFailer> {
  @override
  Widget build(BuildContext context) {
    var _counter;
    return Scaffold(
      appBar: AppBar(),
      body:Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Text('You Tried Your Best!'),
          SizedBox(height: 15.0,),
          Text('Please Try the Exercise Again'),
          SizedBox(height: 15.0,),
          ElevatedButton(onPressed: () {
            // _counter = int.parse( QuestionStorage.readQuestion1Counter()) + _counter + 1;
            // QuestionStorage.saveQuestion1Counter(_counter);
            // if (_counter >= 3) {
            //   Get.to(EnglishComprehensionLimiter());
            // } else
            Get.to(EnglishQuestionAnswerOne());
    },
            child: Text('Try Again'),)

        ],
      ),

    );
  }
}


class EnglishComprehensionLimiter extends StatefulWidget {

  @override
  _EnglishComprehensionLimiterState createState() => _EnglishComprehensionLimiterState();
}

class _EnglishComprehensionLimiterState extends State<EnglishComprehensionLimiter> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body:Column(
        children: <Widget>[
          Text('Unfortunately You Cant Try the Exercise Again'),
          SizedBox(height: 15.0,),
          Text('Go back to Lessons Page to learn more'),
          ElevatedButton(onPressed: () {
            var _counter;
            QuestionStorage.readQuestion1Counter();
            _counter <= 3 ? Get.to(EnglishQuestionAnswerOne()) : Get.to(EnglishVideoContent());
          },
            child: Text('Try Again'),)

        ],
      ),

    );
  }
}
