import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/userLearner/english/englishCompTwoResult.dart';

class EnglishQuestionAnswerTwo extends StatefulWidget {





  @override
  _EnglishQuestionAnswerTwoState createState() =>
      _EnglishQuestionAnswerTwoState();
}

class _EnglishQuestionAnswerTwoState extends State<EnglishQuestionAnswerTwo> {
  @override
  Widget build(BuildContext context) {
    TextEditingController _question1Controller = new TextEditingController();
    TextEditingController _question2Controller = new TextEditingController();
    TextEditingController _question3Controller = new TextEditingController();
    TextEditingController _question4Controller = new TextEditingController();
    TextEditingController _question5Controller = new TextEditingController();
    TextEditingController _question6Controller = new TextEditingController();

    int _mark = 0;

    return Scaffold(
      appBar: AppBar(
        title: Text('Chapter Quiz'),
      ),
      body: Container(
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Text(
                'Comprehension 2',
                style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
              ),
              Text(
                'Read The Story',
                style: TextStyle(
                  fontSize: 14.0,
                ),
              ),

              Text(
                  "Do you remember me? I’m Chiedza. I go to MOPSE-SAGE sessions with Vimbai. "
                  "I live with my grandmother. I have to help her at home. I also have to look after Tobe,"
                  " my daughter, and I do most of the work in the house. There are always "
                  "lots of things to do. I also need time for the MOPSE-SAGE sessions and my "
                  "homework. It’s difficult to remember everything. My friend Vimbai said, “You should make a list.”"
                  "“A list?” I said. “Are you crazy? I don’t need to write a list.”“Yes, you do,” she said. "
                  "“It always helps me to remember things.”Then she helped me to write a list of things to do for"
                  " today and tomorrow. I wanted to buy a chicken.“How do you spell ‘chicken’?” I asked.“I don’t know,” "
                  "said Vimbai. “Draw a little picture.”I drew a picture."
                  "“Your chicken looks like a turkey,” said Vimbai. “You mustn’t buy a turkey tomorrow!”"),

              Divider(),

              //todo: Needs Boolean on answer fields using radio buttons using yes or no
              SingleChildScrollView(
                child: Column(
                  children: [
                    Text(
                      'Answer with YES or NO!',
                      style: TextStyle(
                        fontSize: 22.0,
                      ),
                    ),
                    Divider(),
                    Text(
                      'Which of these things does Chiedza have to do?',
                      style: TextStyle(
                        fontSize: 13.0,
                      ),
                    ),
                    Divider(),
                    Text('1. Help Her grandmother'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.text,
                      controller: _question1Controller,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                          borderRadius: BorderRadius.circular(25.0),
                        ),
                        hintText: 'Enter Answer Here',
                        hintStyle: TextStyle(color: Colors.grey),

                      ),),
                    Divider(
                      thickness: 10.0,
                    ),

                    Text('2. Look after her son'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.text,
                      controller: _question2Controller,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                          borderRadius: BorderRadius.circular(25.0),
                        ),
                        hintText: 'Enter Answer Here',
                        hintStyle: TextStyle(color: Colors.grey),

                      ),),
                    Divider(
                      thickness: 10.0,
                    ),

                    Text('3. Do most of the work in the house'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.text,
                      controller: _question3Controller,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                          borderRadius: BorderRadius.circular(25.0),
                        ),
                        hintText: 'Enter Answer Here',
                        hintStyle: TextStyle(color: Colors.grey),

                      ),),
                    Divider(
                      thickness: 10.0,
                    ),

                    Text('4. Do her homework'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.text,
                      controller: _question4Controller,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                          borderRadius: BorderRadius.circular(25.0),
                        ),
                        hintText: 'Enter Answer Here',
                        hintStyle: TextStyle(color: Colors.grey),

                      ),),
                    Divider(
                      thickness: 10.0,
                    ),

                    Text('5. Help Vimbai to cook a chicken'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.text,
                      controller: _question5Controller,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                          borderRadius: BorderRadius.circular(25.0),
                        ),
                        hintText: 'Enter Answer Here',
                        hintStyle: TextStyle(color: Colors.grey),

                      ),),
                    Divider(
                      thickness: 10.0,
                    ),

                    Text('6. Buy a turkey tomorrow'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.text,
                      controller: _question6Controller,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                          borderRadius: BorderRadius.circular(25.0),
                        ),
                        hintText: 'Enter Answer Here',
                        hintStyle: TextStyle(color: Colors.grey),

                      ),),
                    Divider(
                      thickness: 10.0,
                    ),

                    ElevatedButton(onPressed: () {
                      SystemSound.play(SystemSoundType.click);
                      var _question1Answer = _question1Controller.text.toString().toUpperCase();
                      var _question2Answer = _question2Controller.text.toString().toUpperCase();
                      var _question3Answer= _question3Controller.text.toString().toUpperCase();
                      var _question4Answer = _question4Controller.text.toString().toUpperCase();
                      var _question5Answer = _question5Controller.text.toString().toUpperCase();
                      var _question6Answer = _question6Controller.text.toString().toUpperCase();

                      //Logic to add marks if answer is correct
                      if (_question1Answer.contains('YES')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question2Answer.contains('NO')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question3Answer.contains('YES')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question4Answer.contains('YES')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question5Answer.contains('NO')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question6Answer.contains('YES')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      print(_mark);



                      Get.to(EnglishQuestionAnswerTwoResult(mark: _mark, question1Answer: _question1Answer,
                        question2Answer: _question2Answer, question3Answer: _question3Answer,
                        question4Answer: _question4Answer, question5Answer: _question5Answer,
                        question6Answer: _question6Answer,));

                    }, child: Text('SUBMIT'))
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );

  }
}
