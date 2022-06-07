import 'package:shared_preferences/shared_preferences.dart';

class QuestionStorage {
  //Shared Preferences
  static saveQuestion3(String question3) async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question_3';
    final value = question3;
    prefs.setString(key, value);
  }

  static readQuestion3() async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question_3';
    final value = prefs.get(key) ?? null;
    print('read : $value');
  }

  static saveQuestion4(String question4) async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question_4';
    final value = question4;
    prefs.setString(key, value);
  }

  static readQuestion4() async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question_4';
    final value = prefs.get(key) ?? null;
    print('read : $value');
  }




  //Counters
  static saveQuestion1Counter(String question1Counter) async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question1_counter';
    final value = question1Counter;
    prefs.setString(key, value);
  }

  static readQuestion1Counter() async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question1_counter';
    final value = prefs.get(key) ?? null;
    print('read : $value');
  }


  static saveQuestion2Counter(String question2Counter) async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question2_counter';
    final value = question2Counter;
    prefs.setString(key, value);
  }

  static readQuestion2Counter() async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question2_counter';
    final value = prefs.get(key) ?? null;
    print('read : $value');
  }

  static saveQuestion3Counter(String question3Counter) async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question3_counter';
    final value = question3Counter;
    prefs.setString(key, value);
  }

  static readQuestion3Counter() async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question3_counter';
    final value = prefs.get(key) ?? null;
    print('read : $value');
  }

  static saveQuestion4Counter(String question4Counter) async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question4_counter';
    final value = question4Counter;
    prefs.setString(key, value);
  }

  static readQuestion4Counter() async {
    final prefs = await SharedPreferences.getInstance();
    final key = 'question4_counter';
    final value = prefs.get(key) ?? null;
    print('read : $value');
  }
}