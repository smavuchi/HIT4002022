import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:intelligent_teacher/auth/loginPage.dart';


class RegisterPage extends StatefulWidget {


  @override
  _RegisterPageState createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  bool isVisible = false;
  TextEditingController _usernameController = new TextEditingController();
  TextEditingController _passwordController = new TextEditingController();
  TextEditingController _nameController = new TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
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
                        'Enter Student Registration Details',
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
                              controller: _nameController,
                              style: const TextStyle(color: Colors.white),
                              decoration: InputDecoration(
                                  labelText: 'Full Name',
                                  suffixIcon: IconButton(
                                    icon: Icon(
                                      Icons.person,
                                      color: Colors.grey[300],
                                    ),
                                    onPressed: () {
                                      setState(() {
                                       _nameController = _nameController;
                                      });
                                    },
                                  ),
                                  labelStyle: TextStyle(color: Colors.grey[300]),
                                  border: InputBorder.none),
                            ),
                          ),
                        ),
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
                          ElevatedButton(child: Text('REGISTER'), onPressed: () async {
                            showDialog(
                                context: context,
                                builder: (BuildContext context) {
                                  return Column(
                                    children: [
                                      Text('Registering New user...'),
                                      Center(child: CircularProgressIndicator(),),
                                    ],
                                  );
                                });
                            await buttonAction();

                              Get.to(LoginPage());

                          },),



                        ],
                      ),
                      SizedBox(height: 20.0,),
                      Text('Already have Student Account?', style: TextStyle(
                        color: Colors.white,
                      ),),
                      GestureDetector(
                        onTap: () => Get.to(LoginPage()),
                        child: Text('Click Here to Login!', style: TextStyle(
                            decoration: TextDecoration.underline,
                            color: Colors.blue[900],
                            fontSize: 20.0,
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
      ),
    );
  }

  Future<bool> buttonAction() async {
    //replace the below line of code with your login request
    await new Future.delayed(const Duration(seconds: 3));
    return true;}
}