import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/auth/registrationPage.dart';
import 'package:intelligent_teacher/userLearner/categoryPage.dart';
import '../adminTeacher/adminSubjectCategory.dart';

class LoginPage extends StatefulWidget {


  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  bool isVisible = false;
  TextEditingController _usernameController = new TextEditingController();
  TextEditingController _passwordController = new TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery
            .of(context)
            .size
            .width,
        decoration: const BoxDecoration(
          image: DecorationImage(
            image: AssetImage('asset/images/login_01.jpg'),
            fit: BoxFit.cover,
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.only(left: 150, top: 150),
          child: Row(
            children: [
              Expanded(
                flex: 1,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [

                    Padding(
                      padding: const EdgeInsets.symmetric(vertical: 20),
                      child: Text(
                        'Intelligent Teacher',
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontSize: 40,
                            color: Colors.grey[300]),
                      ),
                    ),
                    Text(
                      'Enter Login Details',
                      style: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 20,
                          color: Colors.grey[500]),
                    ),


                    const SizedBox(
                      height: 20,
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(vertical: 6),
                      child: Card(
                        color: Colors.grey.withOpacity(.4),
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(18)),
                        child: Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 8),
                          child: TextField(
                            controller: _usernameController,
                            style: const TextStyle(color: Colors.white),
                            decoration: InputDecoration(
                                labelText: 'username',
                                suffixIcon: IconButton(
                                  icon: Icon(
                                    Icons.email,
                                    color: Colors.grey[300],
                                  ),
                                  onPressed: () {
                                    // setState(() {
                                    //   emailController = emailController;
                                    // });
                                  },
                                ),
                                labelStyle: TextStyle(color: Colors.grey[300]),
                                border: InputBorder.none),
                          ),
                        ),
                      ),
                    ),
                    Card(
                      color: Colors.grey.withOpacity(.4),
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18)),
                      child: Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 8),
                        child: TextField(
                          controller: _passwordController,
                          style: const TextStyle(color: Colors.white),
                          obscureText: isVisible,
                          decoration: InputDecoration(
                              labelText: 'password',
                              suffixIcon: IconButton(
                                icon: Icon(
                                  isVisible ? Icons.visibility : Icons
                                      .visibility_off,
                                  color: Colors.grey[300],
                                ),
                                onPressed: () {
                                  setState(() {
                                    isVisible = !isVisible;
                                  });
                                },
                              ),
                              labelStyle: TextStyle(color: Colors.grey[300]),
                              border: InputBorder.none),
                        ),
                      ),
                    ),
                    const SizedBox(
                      height: 40,
                    ),
                    Row(
                      children: [
                        const SizedBox(width: 20),
                        ElevatedButton(child: Text('LOGIN'), onPressed: () {
                          if (_usernameController.text.contains('user')) {
                            Get.to(UserCategories());
                          } else if (_usernameController.text.contains('admin')){
                            Get.to(AdminCategories());
                          } else if (_usernameController.text.contains('takudzwa')) {
                            Get.to(UserCategories());
                          } else if (_usernameController.text.contains('pamela')) {
                            Get.to(UserCategories());
                          }
                        },),
                        SizedBox(width: 20.0),


                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Text('Dont have an Account?', style: TextStyle(
                      color: Colors.white,
                    ),),
                    GestureDetector(
                      onTap: () => Get.to(RegisterPage()),
                      child: Text('Register Here', style: TextStyle(
                          decoration: TextDecoration.underline,
                          color: Colors.blue[900],
                          fontSize: 20.0
                      ),),
                    ),
                  ],
                ),
              ),
              const Expanded(flex: 2, child: Card())
            ],
          ),
        ),
      ),
    );
  }
}