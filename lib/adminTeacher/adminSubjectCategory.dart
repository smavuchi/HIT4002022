import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/adminTeacher/English/adminEnglish.dart';
import 'package:intelligent_teacher/userLearner/ict/ictQuestionAndAnswer.dart';

import 'Maths/adminMaths.dart';


class AdminCategories extends StatelessWidget {


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          SizedBox(height: 20.0,),
          Text('Admin Dashboard', style: TextStyle(
            fontSize: 20.0,
            fontWeight: FontWeight.bold
          ),),
          SizedBox(height: 20.0,),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                height: 300,
                width: 300,
                child: GestureDetector(
                  onTap: () => Get.to(AdminEnglish()),
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

              Container(
                height: 300,
                width: 300,
                child: GestureDetector(
                  onTap: () => Get.to(AdminMaths()),
                  child: Column(
                    children: [
                      Image.asset('asset/images/maths.jpg'),
                      Text('Mathematics', style: TextStyle(
                          fontSize: 20.0
                      ),),

                    ],
                  ),
                ),
              ),

              Container(
                height: 300,
                width: 300,
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


            ],
          ),
        ],
      ),
    );
  }
}

