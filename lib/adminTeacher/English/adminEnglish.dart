import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/adminTeacher/English/UploadContent/uploadContent.dart';
import 'package:intelligent_teacher/adminTeacher/adminDrawer.dart';
import 'package:intelligent_teacher/adminTeacher/English/addQuestions.dart';

class  AdminEnglish extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: AppDrawer(),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              GestureDetector(
                onTap: () => Get.to(AdminEnglishAdd()),
                child: Container(
                  child: Column(
                    children: [
                      Icon(Icons.queue, size: 60.0,),
                      Text('Add Questions')
                    ],
                  ),
                ),
              ),
              SizedBox(width: 20.0,),
              Container(
                child: Column(
                  children: [
                    Icon(Icons.queue, size: 60.0,),
                    Text('View Questions')
                  ],
                ),
              ),
              SizedBox(width: 20.0,),
              Container(
                child: Column(
                  children: [
                    Icon(Icons.queue, size: 60.0,),
                    Text('Delete Questions')
                  ],
                ),
              ),
              SizedBox(width: 20.0,),
              GestureDetector(
                onTap: () => Get.to(AdminUploadContentEnglish()),
                child: Container(
                  child: Column(
                    children: [
                      Icon(Icons.backup_sharp, size: 60.0,),
                      Text('Add Learning Content')
                    ],
                  ),
                ),
              ),
            ],
          )
        ],
      ),
    );
  }
}
