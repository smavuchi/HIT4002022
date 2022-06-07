import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'dart:async';
import 'dart:typed_data';
import 'package:webview_flutter/webview_flutter.dart';

import '../../auth/loginPage.dart';


class EnglishVideoContent extends StatefulWidget {
  const EnglishVideoContent({Key? key}) : super(key: key);

  @override
  State<EnglishVideoContent> createState() => _EnglishVideoContentState();
}

class _EnglishVideoContentState extends State<EnglishVideoContent> {
  final Completer<WebViewController> _controller =
  Completer<WebViewController>();

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
      appBar: AppBar(
        title: Text('English Content Page'),
        actions: <Widget>[
          _SampleMenu(_controller.future),
        ],
      ),
      body: Column(
        children: [
          SizedBox(height: 20.0),
          Text( 'Select The Video You Want to Watch' ,style: TextStyle(
            fontSize: 45.0
          )),
          SizedBox(height: 20.0,),
          Expanded(
            child: SingleChildScrollView(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Column(
                    children: [
                      Container(
                        height: 320,
                        width: 480,
                        child: Expanded(
                          child: WebView(
                              initialUrl: 'https://www.youtube.com/embed/s8it_4f6At8',
                              onWebViewCreated: (WebViewController controller) {
                                _controller.complete(controller);
                              }
                          ),
                        ),
                      ),
                      Text('Capital Letters & Full Stops', style: TextStyle(
                        fontSize: 22.0,
                      ),),
                    ],
                  ),
                  SizedBox(height: 20.0),
                  Column(
                    children: [
                      Container(
                        height: 320,
                        width: 480,
                        child: Expanded(
                          child: WebView(
                              initialUrl: 'https://www.youtube.com/embed/DuubQG3gFb8&t=88s',
                              onWebViewCreated: (WebViewController controller) {
                                _controller.complete(controller);
                              }
                          ),
                        ),
                      ),
                      Text('How to Write a Sentence, Verb and Punctuation', style: TextStyle(
                        fontSize: 22.0,
                      ),)
                    ],
                  ),
                  SizedBox(height: 20.0,),
                  Column(
                    children: [
                      Container(
                        height: 320,
                        width: 480,
                        child: Expanded(
                          child: WebView(
                              initialUrl: 'https://www.youtube.com/embed/ZPTV77uIGDw',
                              onWebViewCreated: (WebViewController controller) {
                                _controller.complete(controller);
                              }
                          ),
                        ),
                      ),
                      SizedBox(height: 10.0,),
                      Text('Sounding, Blending & Reading', style: TextStyle(
                        fontSize: 22.0,
                      ),)
                    ],
                  ),
                  SizedBox(height: 20.0,),
                  Column(
                    children: [
                      Container(
                        height: 320,
                        width: 480,
                        child: Expanded(
                          child: WebView(
                              initialUrl: 'https://www.youtube.com/embed/9DudksqYoWw',
                              onWebViewCreated: (WebViewController controller) {
                                _controller.complete(controller);
                              }
                          ),
                        ),
                      ),
                      SizedBox(height: 10.0,),
                      Text('Vocabulary - Animal Sounds', style: TextStyle(
                        fontSize: 22.0,
                      ),)
                    ],
                  ),
                  SizedBox(height: 20.0,),
                  Column(
                    children: [
                      Container(
                        height: 320,
                        width: 480,
                        child: Expanded(
                          child: WebView(
                              initialUrl: 'https://www.youtube.com/embed/saF3-f0XWAY',
                              onWebViewCreated: (WebViewController controller) {
                                _controller.complete(controller);
                              }
                          ),
                        ),
                      ),
                      SizedBox(height: 10.0,),
                      Text('Phonics Song', style: TextStyle(
                        fontSize: 22.0,
                      ),)
                    ],
                  ),

                ],
              ),
            ),
          ),
        ],
      )
    );
  }
}

enum _MenuOptions {
  doPostRequest,
}

class _SampleMenu extends StatelessWidget {
  const _SampleMenu(this.controller);

  final Future<WebViewController> controller;

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<WebViewController>(
      future: controller,
      builder:
          (BuildContext context, AsyncSnapshot<WebViewController> controller) {
        return PopupMenuButton<_MenuOptions>(
          onSelected: (_MenuOptions value) {
            switch (value) {
              case _MenuOptions.doPostRequest:
                _onDoPostRequest(controller.data!, context);
                break;
            }
          },
          itemBuilder: (BuildContext context) =>
          <PopupMenuItem<_MenuOptions>>[
            const PopupMenuItem<_MenuOptions>(
              value: _MenuOptions.doPostRequest,
              child: Text('Post Request'),
            ),
          ],
        );
      },
    );
  }

  Future<void> _onDoPostRequest(WebViewController controller,
      BuildContext context) async {
    final WebViewRequest request = WebViewRequest(
      uri: Uri.parse('https://httpbin.org/post'),
      method: WebViewRequestMethod.post,
      headers: <String, String>{'foo': 'bar', 'Content-Type': 'text/plain'},
      body: Uint8List.fromList('Test Body'.codeUnits),
    );
    await controller.loadRequest(request);
  }
}