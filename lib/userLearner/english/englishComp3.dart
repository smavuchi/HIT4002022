import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';


import 'englishComp3Result.dart';

class EnglishQuestionAnswerThree extends StatefulWidget {

  @override
  _EnglishQuestionAnswerThreeState createState() =>
      _EnglishQuestionAnswerThreeState();
}

class _EnglishQuestionAnswerThreeState extends State<EnglishQuestionAnswerThree> {
  @override
  Widget build(BuildContext context) {
    TextEditingController _question1Controller = new TextEditingController();
    TextEditingController _question2Controller = new TextEditingController();
    TextEditingController _question3Controller = new TextEditingController();
    TextEditingController _question4Controller = new TextEditingController();
    TextEditingController _question5Controller = new TextEditingController();

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
                'Chiedza takes a taxi',
                style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
              ),
              Text(
                'Read The Story',
                style: TextStyle(
                  fontSize: 14.0,
                ),
              ),

              Text(
                  "Chiedza was staying with her cousin, her uncle and her aunt in "
                      "Harare. She wanted to visit the city centre. “Can I walk there?” "
                      "she asked her aunt.“It’s a long way,” said her aunt. “It’s "
                      "better to take a taxi. I’ll giveyou the money for it.”Chiedza’s "
                      "Aunt called a taxi company on her phone, and a few minutes later a taxi arrived. "
                      "“Hi,” said the taxi driver. Then she asked, “Where do you want to go?” "
                      "“The city centre, please.” said Chiedza. “OK, I’ll take you "
                      "to Africa Unity Square,” said the driver.“Are there many female taxi drivers?” asked Chiedza. "
                      "“Sure there are!” said the driver, and laughed. “You know,"
                      " I read that women are safer drivers than men!” “How did you "
                      "become a taxi driver?” asked Chiedza. “Well, some people have their own taxi,"
                      " but I work for a taxi company. The most difficult part was passing my"
                      " driving test. You have to learn the whole Highway Code.” "
                      "“You mean all the rules for driving?” asked Chiedza. “That’s right,” "
                      "said the driver. “And there are lots of them!”“I want to learn to drive,” "
                      "said Chiedza. “Maybe I could become a taxi driver.”" ),

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
                    //todo: add question heading on admin side
                    // Text(
                    //   'Literacy. Are these sentences about the story true?',
                    //   style: TextStyle(
                    //     fontSize: 13.0,
                    //   ),
                    // ),
                    Divider(),
                    Text('1. Chiedza wants to visit the centre of Harare. '),
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
                    Text('2. Chiedza’s cousin lives in the centre of Harare. '),
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
                    Text('3. There is only one female taxi driver in Harare. '),
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
                    Text('4. The taxi driver has her own taxi.'),
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
                    Text('5. Chiedza would like to learn to drive.'),
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

                    ElevatedButton(onPressed: () {
                      SystemSound.play(SystemSoundType.click);
                      var _question1Answer = _question1Controller.text.toString().toUpperCase();
                      var _question2Answer = _question2Controller.text.toString().toUpperCase();
                      var _question3Answer= _question3Controller.text.toString().toUpperCase();
                      var _question4Answer = _question4Controller.text.toString().toUpperCase();
                      var _question5Answer = _question5Controller.text.toString().toUpperCase();

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

                      if (_question3Answer.contains('NO')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question4Answer.contains('NO')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      if (_question5Answer.contains('YES')) {setState(() {
                        _mark++;
                      });} else {
                        _mark = _mark;
                      }

                      print(_mark);




                      Get.to(EnglishQuestionAnswerThreeResult(mark: _mark, question1Answer: _question1Answer,
                        question2Answer: _question2Answer, question3Answer: _question3Answer,
                        question4Answer: _question4Answer, question5Answer: _question5Answer,
                        ));

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
