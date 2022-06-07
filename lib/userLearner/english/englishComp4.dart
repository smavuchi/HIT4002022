import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/userLearner/english/englishCompTwoResult.dart';

class EnglishQuestionAnswerFour extends StatefulWidget {


  @override
  _EnglishQuestionAnswerFourState createState() =>
      _EnglishQuestionAnswerFourState();
}

class _EnglishQuestionAnswerFourState extends State<EnglishQuestionAnswerFour> {
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
                'Comprehension 4',
                style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
              ),

              Text(
                'Read The Story',
                style: TextStyle(
                  fontSize: 14.0,
                ),
              ),
              Text(
                'Vimbai introduces a friend',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),

              Text(
                  "Precious and Zendaya were talking in the street. They saw Vimbai "
                      "with a girl they didn’t know. “Hi,” said Vimbai. “This is Bethsaida. "
                      "She lives near my home.”“Hello,” said Precious. “We were talking "
                      "about what we want to do in five years’ time. We were thinking "
                      "about what jobs we could do.” “And I’ve got two children to look after, "
                      "and chores to do,” said Bethsaida. “That’s like a full-time "
                      "job on its own.” “I know, but try and imagine,” said Precious. "
                      "“I think I’m good at organising things,” said Vimbai. “Maybe I "
                      "could start my own business.” “I’d like to work in a bank,” "
                      "said Bethsaida. “I’m interested in numbers and counting.”"
                      "“I hope you get that job,” said Vimbai. “Then we can come "
                      "to your bank, and you can give us lots of money!” “That would be nice,” "
                      "said Bethsaida, “But it doesn’t work likethat!”“What about you, Precious?” "
                      "asked Zendaya. “I want to work on my family’s land and make it better.” said "
                      "Precious. “I’ll help you!” said Zendaya, with a big smile."

              ),

              Divider(),

              //todo: Needs Boolean on answer fields using radio buttons using yes or no
              SingleChildScrollView(
                child: Column(
                  children: [
                    Text('Multiple Choice', style: TextStyle(
                      fontSize: 16.0,
                      fontWeight: FontWeight.bold,
                    ),),
                    SizedBox(height: 10.0,),
                    Text(
                      'Answer with A, B, C, or D!',
                      style: TextStyle(
                        fontSize: 22.0,
                      ),
                    ),
                    Divider(),
                    Text(
                      'Answer the questions about the story. Match the person with the sentence.',
                      style: TextStyle(
                        fontSize: 13.0,
                      ),
                    ),
                    Divider(),
                    Text('1. She introduces a new friend to her old friends.'),
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
                    Text('2. She has two children.'),
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
                    Text('3. She says she can organise things.'),
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
                    Text('4. She would like to work in a bank.'),
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
                    Text('5. She says that her family has some land.'),
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
                    Text('6. She says she would like to work with Precious.'),
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

                      //Logic for Answer Check

                      if (_question1Answer.contains('D')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question2Answer.contains('D')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question3Answer.contains('C')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question4Answer.contains('D')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question5Answer.contains('A')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question6Answer.contains('B')) {setState(() {
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
