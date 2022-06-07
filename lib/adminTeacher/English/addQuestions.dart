import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/adminTeacher/English/addComprehension3.dart';
import 'package:intelligent_teacher/adminTeacher/adminDrawer.dart';
import '../../databases/questionStorage.dart';
import 'addComprehension4.dart';


class AdminEnglishAdd extends StatefulWidget {

  @override
  _AdminEnglishAddState createState() => _AdminEnglishAddState();
}

class _AdminEnglishAddState extends State<AdminEnglishAdd> {
  TextEditingController _comprehensionPassageController = new TextEditingController();
  TextEditingController _comprehensionTitleController = new TextEditingController();

  var answerType;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Add Question'),),
      drawer: AppDrawer(),
      body: Column(
       children: <Widget>[
         Text('Add Comprehension Title', style: TextStyle(fontSize: 22),),
         TextField(
           keyboardType: TextInputType.text,
           controller: _comprehensionTitleController,
           textAlign: TextAlign.center,
           decoration: InputDecoration(
             border: OutlineInputBorder(
               borderSide: const BorderSide(color: Colors.blue, width: 2.0),
               borderRadius: BorderRadius.circular(25.0),
             ),
             hintText: 'Enter Comprehension Title Here',
               hintStyle: TextStyle(color: Colors.grey),
           ),
           ),

         Text('Add Comprehension Passage', style: TextStyle(fontSize: 22),),
         TextField(
           keyboardType: TextInputType.text,
           controller: _comprehensionPassageController,
           textAlign: TextAlign.center,
           decoration: InputDecoration(
             border: OutlineInputBorder(
               borderSide: const BorderSide(color: Colors.blue, width: 2.0),
               borderRadius: BorderRadius.circular(25.0),
             ),
             hintText: 'Enter Comprehension Passage Here',
             hintStyle: TextStyle(color: Colors.grey),
           ),
         ),
        SizedBox(height: 30.0),


        ElevatedButton(onPressed: () {
          var _comprehensionPassage = _comprehensionPassageController.text;
          var _comprehensionTitle =  _comprehensionTitleController.text;
          Get.to(EnglishQuestions(comprehensionPassage: _comprehensionPassage, comprehensionTitle: _comprehensionTitle));

        }, child: Text('Next'))
       ],
      ),

    );
  }
}


class EnglishQuestions extends StatefulWidget {
  EnglishQuestions({required this.comprehensionPassage, required this.comprehensionTitle});


  String comprehensionPassage;
  String comprehensionTitle;

  @override
  _EnglishQuestionsState createState() => _EnglishQuestionsState();
}

class _EnglishQuestionsState extends State<EnglishQuestions> {
  @override
  Widget build(BuildContext context) {
    String question3;
    String question4;

    return Scaffold(
      appBar: AppBar(
        title: Text('Add Question Type'),
      ),
      body: Column(
        children: [
         Text(widget.comprehensionTitle),
          SizedBox(height: 20.0,),
          Divider(),
          Text(widget.comprehensionPassage),
          SizedBox(height: 20.0,),
          Divider(),
          Text('Questions Type',style: TextStyle(
            fontSize: 22.0,
            fontWeight: FontWeight.bold
          ),),
          SizedBox(height: 20.0,),
          Container(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(onPressed: () => {
                  if (widget.comprehensionTitle.contains('Chiedza')) {
                    question3 = 'true',
                    QuestionStorage.saveQuestion3(question3),
                    Get.to(AddComprehension3())

                  } else if (widget.comprehensionTitle.contains('Vimbai')) {
                     question4 = 'true',
                     QuestionStorage.saveQuestion4(question4),
                     Get.to(AddComprehension4())
                  } else {
                    Get.to(AdminEnglishAdd())
                  }
                }, child: Text('Written'),),


                SizedBox(width: 20.0,),


                ElevatedButton(onPressed: () => {
                  question4 = 'true',
                  QuestionStorage.saveQuestion4(question4),
                  Get.to(AddComprehension4()),

                }, child: Text('Multiple Choice')),

                SizedBox(width: 20.0,),

                ElevatedButton(onPressed: () => {
                  question3 = 'true',
                QuestionStorage.saveQuestion3(question3),
                  Get.to(AddComprehension3())
                }, child: Text('Yes Or No')),

              ],
            ),
          )
        ],
      ),
    );
  }
}

