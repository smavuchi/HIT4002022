import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/userLearner/ict/ictQuestionAndAnswer.dart';

import 'english/englishNavigator.dart';
import 'maths/mathsQuestions.dart';


class UserCategories extends StatelessWidget {


  @override
  Widget build(BuildContext context) {
    var size = MediaQuery
        .of(context)
        .size;
    return Scaffold(
      appBar: AppBar(
        title: Text('Intelligent Teacher'),
      ),
      body: SizedBox(
        width: size.width,
        height: size.height,
        child: Column(
          children: [
            SizedBox(height: 20.0,),
            Text('Welcome to Intelligent Teacher', style: TextStyle(
              fontSize: 20.0,
              fontWeight: FontWeight.bold,
            ),),
            SizedBox(height: 20.0,),
            Center(
              child: Container(
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    SizedBox(
                      height: 250,
                      width: 250,
                      child: GestureDetector(
                        onTap: () => Get.to(
                          EnglishNavigator()
                        ),
                        child: Column(
                          children: [
                            Image.asset('asset/images/english.jpg'),
                            Text('English', style: TextStyle(
                              fontSize: 20.0
                            ),),
                          ],
                        ),
                      ),
                    ),

                    // Column(
                    //   children: [
                    //     Image.asset('asset/images/familyHeritage.jpg'),
                    //     Text('Family Heritage', style: TextStyle(
                    //         fontSize: 20.0
                    //     ),),
                    //
                    //   ],
                    // ),
                    SizedBox(width: 20.0,),

                    SizedBox(
                      height: 280,
                      width: 250,
                      child: GestureDetector(
                        onTap: () => Get.to(ICTQuestionAnswer()) ,
                        child: Column(
                          children: [
                            Image.asset('asset/images/ict.jpg',),
                            Text('ICT', style: TextStyle(
                                fontSize: 20.0
                            ),),

                          ],
                        ),
                      ),
                    ),

                    SizedBox(width: 20.0,),

                    SizedBox(
                      height: 250,
                      width: 250,
                      child: GestureDetector(
                        onTap: () => Get.to(MathsQuestionAnswer()) ,
                        child: Column(
                          children: [
                            Image.asset('asset/images/maths.jpg',),
                            Text('Mathematics', style: TextStyle(
                                fontSize: 20.0
                            ),),

                          ],
                        ),
                      ),
                    ),



                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
