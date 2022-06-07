import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/userLearner/english/englishCategory.dart';
import '../../auth/loginPage.dart';
import 'englishVideoContentPage.dart';

class EnglishNavigator extends StatefulWidget {

  @override
  _EnglishNavigatorState createState() => _EnglishNavigatorState();
}

class _EnglishNavigatorState extends State<EnglishNavigator> {

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
        body:  Column(
                children: [
                  SizedBox(height: 20.0,),
                  Text('Learn English or Select English Exercises', style: TextStyle(
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
                          Get.to(UserEnglishSelector());
                        },
                        child: Container(
                          decoration: BoxDecoration(
                              border: Border.all(color: Colors.purpleAccent)
                          ),
                          child: Text('Exercises', style: TextStyle(
                            fontSize: 46.0,
                          ),),
                        ),
                      ),

                      SizedBox(width: 20.0,),

                      GestureDetector(
                        onTap: () {
                          SystemSound.play(SystemSoundType.click);
                          Get.to(EnglishVideoContent());
                        },
                        child: Container(
                          decoration: BoxDecoration(
                              border: Border.all(color: Colors.blueAccent)
                          ),
                          child: Text('Lessons', style: TextStyle(
                              fontSize: 46.0
                          ),),
                        ),
                      ),

                    ],
                  ),
                ],
              )

    );
  }
}
