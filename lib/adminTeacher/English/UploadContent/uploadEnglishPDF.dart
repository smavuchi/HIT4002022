import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_dropzone/flutter_dropzone.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/adminTeacher/English/UploadContent/uploadContent.dart';

class UploadEnglishPDF extends StatefulWidget {
  @override
  State<UploadEnglishPDF> createState() => _UploadEnglishPDFState();
}

class _UploadEnglishPDFState extends State<UploadEnglishPDF> {

  late DropzoneViewController controller1;
  String message1 = 'Drop Documents here';
  bool highlighted1 = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Upload English Documents Learning Content'),),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          RichText(text: TextSpan(
            children: <TextSpan>[
              TextSpan(
                text: 'Drag Files to Upload In Container Below 👇👇👇',
                style: TextStyle(
                  fontSize: 30.0,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ]
          ), ),
          SizedBox(height: 10.0,),
          Center(
            child: Container(
              alignment: Alignment.center,
              width: 600.0,
              height: 400.0,
              padding: EdgeInsets.only(left: 200.0, top: 100.0),
              decoration: BoxDecoration(
                color: highlighted1 ? Colors.green : Colors.transparent,
                  border: Border.all(color: Colors.purpleAccent)
              ),
              child: Stack(children: <Widget>[
                buildZone1(context),
                Icon(Icons.upload_rounded, size: 200.0, color: Colors.cyanAccent,),


              ]),
            ),
          ),
          SizedBox(height: 20.0),
          ElevatedButton(onPressed: () => Get.to(UploadPDFSuccess(fileName: 'PDF',)),
            child: Text('UPLOAD', style: TextStyle(
              fontSize: 30.0,
            ),), ),
        ],
      )
    );
  }

  Future<bool> buttonAction() async {
    //replace the below line of code with your login request
    await new Future.delayed(const Duration(seconds: 5));
    return true;
  }

  Widget buildZone1(BuildContext context) => Builder(
    builder: (context) => DropzoneView(
      operation: DragOperation.copy,
      cursor: CursorType.grab,
      onCreated: (ctrl) => controller1 = ctrl,
      onLoaded: () => print('Zone 1 loaded'),
      onError: (ev) => print('Zone 1 error: $ev'),
      onHover: () {
        setState(() => highlighted1 = true);
        print('Zone 1 hovered');
      },
      onLeave: () {
        setState(() => highlighted1 = false);
        print('Zone 1 left');
      },
      onDrop: (ev) async {
        print('Zone 1 drop: ${ev.name}');
        setState(() {
          message1 = '${ev.name} dropped';
          highlighted1 = false;
        });


      },
    ),
  );

}

class UploadPDFSuccess extends StatefulWidget {
  final String fileName;
  const UploadPDFSuccess({required this.fileName});

  @override
  State<UploadPDFSuccess> createState() => _UploadPDFSuccessState();
}

class _UploadPDFSuccessState extends State<UploadPDFSuccess> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Successful Upload'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            SizedBox(height: 20.0),
            Text('${widget.fileName} has been uploaded successfully', style: TextStyle(
              fontSize: 40.0,
              fontWeight: FontWeight.bold,
            ),),
            SizedBox(height: 20.0),
            ElevatedButton(onPressed: () {
              SystemSound.play(SystemSoundType.alert);
              Get.to(AdminUploadContentEnglish());
            }, child: Text('Add More Content', style: TextStyle(
              fontSize: 30.0,
            ),))
          ],
        ),
      ),
    );
  }

  void showAlert(BuildContext context) {
    showDialog(
        context: context,
        builder: (BuildContext context) {

          return Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Text('Uploading...'),
              Center(child: CircularProgressIndicator(),),
            ],
          );
        });
  }
}



