import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../auth/loginPage.dart';
import 'names.dart';

class AppDrawer extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          DrawerHeader(child: Text('Menu')),
          ListTile(
            title: Text('Add Questions'), trailing: Icon(Icons.queue_sharp),
          ),
          ListTile(
            title: Text('Delete Questions'), trailing: Icon(Icons.delete),
          ),
          ListTile(
            title: Text('View Questions'), trailing: Icon(Icons.view_list_sharp),
          ),
          GestureDetector(
            onTap: () => Get.to(Names()),
            child: ListTile(
              title: Text('View Students'), trailing: Icon(Icons.list_outlined),
            ),
          ),

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
    );
  }
}
