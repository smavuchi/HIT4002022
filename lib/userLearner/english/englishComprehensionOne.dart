import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/userLearner/english/englishCompOneResult.dart';
import 'package:flutter/services.dart';


class EnglishQuestionAnswerOne extends StatefulWidget {



  @override
  _EnglishQuestionAnswerOneState createState() => _EnglishQuestionAnswerOneState();
}

class _EnglishQuestionAnswerOneState extends State<EnglishQuestionAnswerOne> {
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
                  'Comprehension 1', style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
              ),
              Text(
                'Read The Story', style: TextStyle(
                fontSize: 14.0,
              ),

              ),

              Text(
                'My Homstead', style: TextStyle(
                fontSize: 15.0,
              ),

              ),



              Text(
                "Hello again! This is my home. We grow some vegetables and we keep some animals."
                    " I’ve got two more new friends from the sessions. Their names are Precious and Zendaya. Precious is 12 and Zendaya is 13. It is difficult for Zendaya to learn new things,"
                    " but she always smiles and she always says nice things. She loves animals.“How many animals have you got, Vimbai?” Zendaya asks.“We’ve got nine chickens and two goats,” "
                    "I say.“Girls, go and look for eggs,” says my mother.We go outside and look for eggs.“Here’s an egg!” says Precious, but then she drops it and the egg breaks.“Oh, no!” she says. "
                    "“I’m very sorry!”“Don’t worry,” I say. “There are lots more.”Precious finds one more egg, I find two eggs and Zendaya finds four eggs. “Wow, Zendaya!” says Precious."
                    " “You’re very good at finding eggs!”“I want to be a farmer!” says Zendaya, with a big smile. Match the questions with the numbers."
              ),
              Divider(),
              Text('Enter the Correct Number In The Answer'),

              SizedBox(height: 10.0,),

              SingleChildScrollView(
                child: Column(
                  children: [
                    Text('1. How old  is Precious?'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.number,
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
                    Divider(thickness: 10.0,),

                    Text('2. How old  is Zendaya?'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.number,
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
                    Divider(thickness: 10.0,),

                    Text('3. How many chickens does Vimbai have?'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.number,
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
                    Divider(thickness: 10.0,),

                    Text('4. How many goats does Vimbai have?'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.number,
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
                    Divider(thickness: 10.0,),

                    Text('5. How many eggs does Zendaya find?'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.number,
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
                    Divider(thickness: 10.0,),

                    Text('6. How many eggs do all the girls have?'),
                    Divider(),
                    TextField(
                      keyboardType: TextInputType.number,
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
                    Divider(thickness: 10.0,),


                      ElevatedButton(onPressed: () {
                        SystemSound.play(SystemSoundType.click);
                        var _question1Answer = _question1Controller.text.toString();
                        var _question2Answer = _question2Controller.text.toString();
                        var _question3Answer= _question3Controller.text.toString();
                        var _question4Answer = _question4Controller.text.toString();
                        var _question5Answer = _question5Controller.text.toString();
                        var _question6Answer = _question6Controller.text.toString();

                        //Logic to add marks if answer is correct
                        if (_question1Answer.contains('12')) {setState(() {
                          _mark++;
                        });} else {
                          _mark = _mark;
                        }

                        if (_question2Answer.contains('13')) {setState(() {
                          _mark++;
                        });} else {
                          _mark = _mark;
                        }

                        if (_question3Answer.contains('9')) {setState(() {
                          _mark++;
                        });} else {
                          _mark = _mark;
                        }

                        if (_question4Answer.contains('2')) {setState(() {
                          _mark++;
                        });} else {
                          _mark = _mark;
                        }

                        if (_question5Answer.contains('4')) {setState(() {
                          _mark++;
                        });} else {
                          _mark = _mark;
                        }

                        if (_question6Answer.contains('6')) {setState(() {
                          _mark++;
                        });} else {
                          _mark = _mark;
                        }

                        print(_mark);

                        //Pass Variables to Next Page
                        Get.to(EnglishQuestionAnswerOneResult(question1Answer: _question1Answer,
                          question2Answer: _question2Answer, question3Answer: _question3Answer,
                          question4Answer: _question4Answer, question5Answer: _question5Answer,
                          question6Answer: _question6Answer, mark: _mark,));

                        //Store Failed Questions

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

