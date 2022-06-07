import 'package:flutter/material.dart';
import 'package:get/get.dart';

class AddSubtraction extends StatefulWidget {



  @override
  _AddSubtractionState createState() => _AddSubtractionState();
}

class _AddSubtractionState extends State<AddSubtraction> {
  @override
  Widget build(BuildContext context) {
    TextEditingController _value1Controller = new TextEditingController();
    TextEditingController _value2Controller = new TextEditingController();
    return Scaffold(
      appBar: AppBar(title: Text('Add Subtraction Question')),
      body: Column(
        children: <Widget>[
          Text('Add Values', style: TextStyle(
              fontWeight: FontWeight.bold,
            fontSize: 16.0,
          ),),
          SizedBox(height: 10.0),
          Text('NB: Value 1 Must Be Greater Than Value 2'),
          SizedBox(height: 10.0,),
          Row(
            children: <Widget>[
              Container(
                child: TextField(
                  keyboardType: TextInputType.text,
                  controller: _value1Controller,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                      borderRadius: BorderRadius.circular(25.0),
                    ),
                    hintText: 'Value 1',
                    hintStyle: TextStyle(color: Colors.grey),

                  ),),
              ),
              SizedBox(width: 20.0),

              Container(
                child: Icon(Icons.remove, size: 20.0),
              ),
              SizedBox(width: 20.0),

              Container(
                child: TextField(
                  keyboardType: TextInputType.text,
                  controller: _value2Controller,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderSide: const BorderSide(color: Colors.blue, width: 2.0),
                      borderRadius: BorderRadius.circular(25.0),
                    ),
                    hintText: 'Value 2',
                    hintStyle: TextStyle(color: Colors.grey),

                  ),),
              ),
            ],
          ),
          ElevatedButton(
            onPressed: () {
              Get.to(AddSubtractionSuccess(value2: _value2Controller.text, value1: _value1Controller.text));
              //todo: Add question to shared prefernces via iteraion
            },
            child: Text('SUBMIT'),
          )


        ]
      ),
    );
  }
}

class AddSubtractionSuccess extends StatefulWidget {
  String value2;
  String value1;
  AddSubtractionSuccess({required this.value2, required this.value1});

  @override
  State<AddSubtractionSuccess> createState() => _AddSubtractionSuccessState();
}

class _AddSubtractionSuccessState extends State<AddSubtractionSuccess> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Question Added Successfully'),
      ),
      body: Column(
        children: [
          Text('Question'),
          Row(
            children: [
              Text('${int.parse(widget.value1)}'),
              Text('-'),
              Text('${int.parse(widget.value2)}'),
              Text('='),
              Text('${int.parse(widget.value1)-int.parse(widget.value2)}')
            ],
          )
        ],
      ),
    );
  }
}