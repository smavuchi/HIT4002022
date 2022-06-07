import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import '../../auth/loginPage.dart';
import 'englishComp3.dart';
import 'englishComp4.dart';
import 'englishComprehension2.dart';
import 'englishComprehensionOne.dart';

class UserEnglishSelector extends StatefulWidget {

  @override
  _UserEnglishSelectorState createState() => _UserEnglishSelectorState();
}


// Future init() async {
//
//   QuestionStorage.readQuestion3();
//   QuestionStorage.readQuestion4();
// }
class _UserEnglishSelectorState extends State<UserEnglishSelector> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(child: Text('Menu')),

            GestureDetector(
              onTap: () {
                Get.to(LoginPage());
              },
              child: ListTile(
                title: Text('Logout'), trailing: Icon(Icons.logout),
              ),
            ),
          ],
        ),
      ),
      appBar: AppBar(title: Text('English Exercises'),),
      body: Column(
              children: [
                SizedBox(height: 20.0,),
                Text('Select The Exercise You Want to Attempt', style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 22.0,
                ),),
                SizedBox(height: 30.0,),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    GestureDetector(
                      onTap: () {
                        SystemSound.play(SystemSoundType.click);
                        Get.to(EnglishQuestionAnswerOne());
                      },
                      child: Container(
                        decoration: BoxDecoration(
                            border: Border.all(color: Colors.purpleAccent)
                        ),
                        child: Text('1', style: TextStyle(
                          fontSize: 46.0,
                        ),),
                      ),
                    ),

                    SizedBox(width: 20.0,),

                    GestureDetector(
                      onTap: () {
                        SystemSound.play(SystemSoundType.click);
                        Get.to(EnglishQuestionAnswerTwo());
                      },
                      child: Container(
                        decoration: BoxDecoration(
                          border: Border.all(color: Colors.blueAccent)
                        ),
                        child: Text('2', style: TextStyle(
                            fontSize: 46.0
                        ),),
                      ),
                    ),

                    SizedBox(width: 20.0,),

                    GestureDetector(
                      onTap: () =>
                      {
                        SystemSound.play(SystemSoundType.click),
                        Get.to(EnglishQuestionAnswerThree())},
                      child: Container(
                        decoration: BoxDecoration(
                            border: Border.all(color: Colors.redAccent)
                        ),
                        child: Text('3', style: TextStyle(
                            fontSize: 46.0
                        ),),
                      ),
                    ),

                    SizedBox(width: 20.0,),

                    GestureDetector(
                      onTap: () {
                        SystemSound.play(SystemSoundType.click);
                        Get.to(EnglishQuestionAnswerFour());
                      },
                      child: Container(
                        decoration: BoxDecoration(
                            border: Border.all(
                                color: Colors.yellowAccent)
                        ),
                        child: Text('4', style: TextStyle(
                            fontSize: 46.0
                        ),),
                      ),
                    ),

                  ],
                ),
              ],
            ));
          }

  }

