import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/adminTeacher/English/UploadContent/uploadEnglishPDF.dart';
import 'package:intelligent_teacher/adminTeacher/English/UploadContent/uploadEnglishVideo.dart';
import 'package:intelligent_teacher/adminTeacher/adminDrawer.dart';


class  AdminUploadContentEnglish extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Upload Content'),),
      drawer: AppDrawer(),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          SizedBox(height: 20.0,),
          Text('Select Content Type', style: TextStyle(
            fontSize: 30.0,
            fontWeight: FontWeight.bold,
          ),),
          SizedBox(height: 20.0,),
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                GestureDetector(
                onTap: () => Get.to(UploadEnglishPDF()),
                  child: Container(
                    child: Column(
                      children: [
                        Icon(Icons.backup, size: 60.0, color: Colors.purple,),
                        Text('Upload Documents'),
                      ],
                    ),
                  ),
                ),
                SizedBox(child: VerticalDivider(
                  color: Colors.cyanAccent,
                  indent: 10,
                  endIndent: 400,
                ),width: 20.0,),
                GestureDetector(
                  onTap: () => Get.to(UploadEnglishVideo()),
                  child: Container(
                    child: Column(
                      children: [
                        Icon(Icons.backup_sharp, size: 60.0, color: Colors.lightGreenAccent),
                        Text('Upload Videos')
                      ],
                    ),
                  ),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }
}
